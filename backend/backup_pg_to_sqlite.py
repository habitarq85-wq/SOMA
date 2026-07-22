"""
Backup: PostgreSQL (Supabase) → SQLite local.
Uso: python backup_pg_to_sqlite.py

Guarda en: backups_sqlite/proyectos_arquitectonicos_AAAAMMDD_HHMMSS.db
También actualiza: web/EjemploBD/proyectos_arquitectonicos.db (fallback local)
"""
import os
import sys
import json
import shutil
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db import _get_db_url

BACKUP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "antecedentes", "backups_sqlite")
FALLBACK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web", "EjemploBD", "proyectos_arquitectonicos.db")

TABLAS = [
    "captura_web",
    "cobros",
    "config_fiscal",
    "programa_arquitectonico",
    "matriz_inversion",
    "habitantes",
    "actividades",
    "ejes_diseno",
    "algoritmo_progreso",
    "egresos",
    "fondos",
    "movimientos_fondo",
]


def get_columns(pg_cur, table):
    pg_cur.execute(f"SELECT column_name, data_type, is_nullable, column_default FROM information_schema.columns WHERE table_name = '{table}' AND table_schema = 'public' ORDER BY ordinal_position")
    return pg_cur.fetchall()


def pg_to_sqlite_type(pg_type):
    t = pg_type.lower()
    if 'serial' in t or 'integer' in t or 'int' in t:
        return 'INTEGER'
    if 'real' in t or 'float' in t or 'double' in t or 'numeric' in t or 'decimal' in t:
        return 'REAL'
    if 'bool' in t:
        return 'INTEGER'
    if 'json' in t or 'text' in t or 'char' in t or 'varchar' in t:
        return 'TEXT'
    if 'timestamp' in t or 'date' in t:
        return 'TEXT'
    if 'bytea' in t:
        return 'BLOB'
    return 'TEXT'


def clean_pg_default(default_str):
    if not default_str:
        return None
    d = str(default_str)
    if 'nextval' in d.lower():
        return None
    if d == 'now()' or d == 'CURRENT_DATE' or d == 'CURRENT_TIMESTAMP':
        return None
    import re
    d = re.sub(r"::\w+(\[\])?", "", d)
    d = d.strip()
    if d == "''":
        return "''"
    return d


def migrate_pg_to_sqlite(pg_conn, sqlite_conn, table):
    pg_cur = pg_conn.cursor()
    columns = get_columns(pg_cur, table)
    if not columns:
        print(f"  Tabla {table} no encontrada en PostgreSQL, saltando.")
        return 0

    col_names = [c[0] for c in columns]
    col_defs = []
    has_serial = False
    for c in columns:
        name = c[0]
        pg_type = c[1]
        nullable = c[2]
        default = c[3]
        stype = pg_to_sqlite_type(pg_type)
        # SERIAL → INTEGER PRIMARY KEY AUTOINCREMENT
        is_pk = 'serial' in pg_type.lower() or default and 'nextval' in str(default).lower()
        if is_pk and not has_serial:
            has_serial = True
            col_defs.append(f'"{name}" INTEGER PRIMARY KEY AUTOINCREMENT')
            continue
        nullable_str = "" if nullable == "NO" else ""
        default_clean = clean_pg_default(default)
        default_str = f"DEFAULT {default_clean}" if default_clean else ""
        col_defs.append(f'"{name}" {stype} {nullable_str} {default_str}'.strip())

    create_sql = f'CREATE TABLE IF NOT EXISTS "{table}" (\n  ' + ",\n  ".join(col_defs) + "\n)"
    sqlite_cur = sqlite_conn.cursor()
    sqlite_cur.execute(f'DROP TABLE IF EXISTS "{table}"')
    sqlite_cur.execute(create_sql)

    pg_cur.execute(f'SELECT * FROM "{table}" ORDER BY 1')
    rows = pg_cur.fetchall()
    if not rows:
        print(f"  {table}: 0 registros")
        pg_cur.close()
        return 0

    placeholders = ",".join(["?"] * len(col_names))
    cols_str = ",".join(f'"{n}"' for n in col_names)

    count = 0
    batch = []
    BATCH_SIZE = 100

    for row in rows:
        processed = []
        for val in row:
            if val is None:
                processed.append(None)
            elif isinstance(val, (int, float)):
                processed.append(val)
            elif isinstance(val, bool):
                processed.append(1 if val else 0)
            elif isinstance(val, (dict, list)):
                processed.append(json.dumps(val, ensure_ascii=False))
            elif isinstance(val, bytes):
                processed.append(val.decode('utf-8', errors='replace'))
            else:
                processed.append(str(val))
        batch.append(tuple(processed))
        count += 1

        if len(batch) >= BATCH_SIZE:
            for r in batch:
                sqlite_cur.execute(f'INSERT INTO "{table}" ({cols_str}) VALUES ({placeholders})', r)
            batch = []

    if batch:
        for r in batch:
            sqlite_cur.execute(f'INSERT INTO "{table}" ({cols_str}) VALUES ({placeholders})', r)

    sqlite_conn.commit()
    sqlite_cur.close()
    print(f"  {table}: {count} registros")
    pg_cur.close()
    return count


def main():
    url = _get_db_url()
    if not url:
        print("ERROR: No hay DATABASE_URL. Define la variable de entorno.")
        sys.exit(1)

    import psycopg2
    from psycopg2.extras import RealDictCursor

    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(FALLBACK_PATH), exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"proyectos_arquitectonicos_{timestamp}.db")

    print(f"Conectando a PostgreSQL...")
    pg_conn = psycopg2.connect(url)
    pg_conn.autocommit = False
    print("Conectado.\n")

    import sqlite3
    sqlite_conn = sqlite3.connect(backup_path)
    total = 0

    for table in TABLAS:
        try:
            n = migrate_pg_to_sqlite(pg_conn, sqlite_conn, table)
            total += n
        except Exception as e:
            print(f"  ERROR en {table}: {e}")
            pg_conn.rollback()

    sqlite_conn.close()
    pg_conn.close()

    shutil.copy2(backup_path, FALLBACK_PATH)
    print(f"\n=== Backup completado: {total} registros en {total} tablas ===")
    print(f"Backup: {backup_path}")
    print(f"Fallback: {FALLBACK_PATH}")


if __name__ == "__main__":
    main()
