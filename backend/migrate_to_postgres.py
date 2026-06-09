"""
Script de migración: SQLite → PostgreSQL para SOMA.
Uso: DATABASE_URL=<postgres_url> python migrate_to_postgres.py

Exporta datos de SQLite y los importa a PostgreSQL.
La tabla de destino se crea automáticamente si no existe.
"""
import os
import sqlite3
import json
import sys

SQLITE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "web", "EjemploBD", "proyectos_arquitectonicos.db"
)

TABLAS = [
    "captura_web",
    "cobros",
    "config_fiscal",
    "programa_arquitectonico",
    "matriz_inversion",
    "habitantes",
    "actividades",
    "ejes_diseno",
]


def get_pg_conn():
    import psycopg2
    from psycopg2.extras import RealDictCursor

    url = os.environ.get("DATABASE_URL")
    if not url:
        print("ERROR: Define DATABASE_URL como variable de entorno")
        sys.exit(1)
    conn = psycopg2.connect(url)
    conn.autocommit = False
    return conn


def sqlite_to_pg_type(sqlite_type):
    t = sqlite_type.upper()
    if "INTEGER PRIMARY KEY AUTOINCREMENT" in t:
        return "SERIAL PRIMARY KEY"
    if "INTEGER" in t:
        return "INTEGER"
    if "REAL" in t:
        return "REAL"
    if "TEXT" in t or "VARCHAR" in t:
        return "TEXT"
    return t


def get_sqlite_schema(conn, table):
    cur = conn.execute(f"SELECT sql FROM sqlite_master WHERE name = ? AND type='table'", (table,))
    row = cur.fetchone()
    if row:
        return row[0]


def extract_columns(sql):
    """Extrae definiciones de columnas del CREATE TABLE SQL."""
    # Remove SQL comments (-- to end of line)
    lines = sql.split('\n')
    clean_lines = []
    for line in lines:
        idx = line.find('--')
        if idx >= 0:
            line = line[:idx]
        clean_lines.append(line)
    sql = '\n'.join(clean_lines)

    cols_start = sql.index("(") + 1
    cols_end = sql.rindex(")")
    cols_section = sql[cols_start:cols_end]

    cols = []
    current = ""
    depth = 0
    in_str = None
    for ch in cols_section:
        if in_str:
            current += ch
            if ch == in_str and (not current or current[-2:-1] != '\\'):
                in_str = None
        elif ch in ("'", '"'):
            current += ch
            in_str = ch
        elif ch == '(':
            current += ch
            depth += 1
        elif ch == ')':
            current += ch
            depth -= 1
        elif ch == ',' and depth == 0:
            cols.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        cols.append(current.strip())

    result = []
    for col in cols:
        upper = col.upper().strip()
        if upper.startswith("FOREIGN KEY") or upper.startswith("PRIMARY KEY"):
            continue
        result.append(col)
    return result


def create_pg_table(pg_conn, table_name, columns_defs):
    """Crea tabla en PostgreSQL a partir de columnas SQLite."""
    pg_cols = []
    for col_def in columns_defs:
        parts = col_def.split()
        if not parts:
            continue
        col_name = parts[0]
        sqlite_type = " ".join(parts[1:])
        pg_type = sqlite_to_pg_type(sqlite_type)
        default_part = ""
        for p in parts:
            if p.upper() in ("DEFAULT",):
                idx = parts.index(p)
                default_val = " ".join(parts[idx:])
                default_part = f" {default_val}"
                break
        pg_cols.append(f"{col_name} {pg_type}{default_part}")

    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  " + ",\n  ".join(pg_cols) + "\n)"
    cur = pg_conn.cursor()
    cur.execute(create_sql)
    pg_conn.commit()
    cur.close()


def migrate_table(sqlite_conn, pg_conn, table):
    print(f"\n--- Migrando tabla: {table} ---")

    schema_sql = get_sqlite_schema(sqlite_conn, table)
    if not schema_sql:
        print(f"  Tabla {table} no encontrada en SQLite, saltando.")
        return 0

    columns_defs = extract_columns(schema_sql)
    create_pg_table(pg_conn, table, columns_defs)

    sqlite_cur = sqlite_conn.execute(f"SELECT * FROM {table}")
    rows = sqlite_cur.fetchall()
    if not rows:
        print(f"  Sin datos en {table}.")
        return 0

    col_names = [desc[0] for desc in sqlite_cur.description]
    placeholders = ",".join(["%s"] * len(col_names))
    columns = ",".join(col_names)

    pg_cur = pg_conn.cursor()

    # Limpiar tabla destino antes de insertar
    pg_cur.execute(f"DELETE FROM {table}")

    # Si SERIAL, reiniciar secuencia
    try:
        pg_cur.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
    except Exception:
        pass

    count = 0
    batch = []
    BATCH_SIZE = 100

    for row in rows:
        processed = []
        for val in row:
            if isinstance(val, str):
                processed.append(val)
            elif isinstance(val, (int, float)):
                processed.append(val)
            elif val is None:
                processed.append(None)
            else:
                processed.append(str(val))
        batch.append(tuple(processed))
        count += 1

        if len(batch) >= BATCH_SIZE:
            for r in batch:
                pg_cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", r)
            batch = []

    if batch:
        for r in batch:
            pg_cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", r)

    pg_conn.commit()
    pg_cur.close()
    print(f"  {count} registros migrados.")
    return count


def main():
    if not os.path.exists(SQLITE_PATH):
        print(f"No se encontró SQLite DB en: {SQLITE_PATH}")
        print("Creando base de datos vacía...")
        conn = sqlite3.connect(SQLITE_PATH)
        conn.close()
        print("BD vacía creada. No hay datos para migrar.")
        return

    sqlite_conn = sqlite3.connect(SQLITE_PATH)
    pg_conn = get_pg_conn()

    total = 0
    for table in TABLAS:
        try:
            n = migrate_table(sqlite_conn, pg_conn, table)
            total += n
        except Exception as e:
            print(f"  ERROR migrando {table}: {e}")
            pg_conn.rollback()

    sqlite_conn.close()
    pg_conn.close()
    print(f"\n=== Migración completada: {total} registros migrados ===")


if __name__ == "__main__":
    main()
