"""
Abstracción de base de datos para SOMA.
Soporta SQLite (desarrollo local) y PostgreSQL (producción en Render).
Fallback automático: si PostgreSQL no está disponible, usa SQLite.
"""
import os
import sqlite3
import json

_pg_available = None  # None = no probado, True/False

def _get_db_url():
    for key in ('SUPABASE_URL', 'DATABASE_URL'):
        url = os.environ.get(key, '')
        prefix = f'{key}='
        if url.startswith(prefix):
            url = url[len(prefix):]
        if url and (url.startswith('postgresql://') or url.startswith('postgres://')):
            return url
    return ''

def _get_sqlite_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proyecto_dir = os.path.dirname(base_dir)
    return os.path.join(proyecto_dir, "web", "EjemploBD", "proyectos_arquitectonicos.db")

def _use_postgres():
    return _pg_available is True

def get_connection():
    global _pg_available
    url = _get_db_url()
    if url and _pg_available is not False:
        try:
            import psycopg2
            from psycopg2.extras import RealDictCursor
            conn = psycopg2.connect(url, cursor_factory=RealDictCursor, connect_timeout=5)
            _pg_available = True
            return conn
        except Exception as e:
            print(f"[DB] PostgreSQL no disponible ({e}). Usando SQLite local.")
            _pg_available = False
    db_path = _get_sqlite_path()
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def adapt_sql(sql):
    if _use_postgres():
        sql = sql.replace('?', '%s')
        sql = sql.replace('IFNULL(', 'COALESCE(')
        sql = sql.replace("datetime('now')", "NOW()")
        if sql.lstrip().upper().startswith("INSERT") and "RETURNING ID" not in sql.upper():
            sql += " RETURNING id"
    return sql

def execute(conn, sql, params=None):
    cur = conn.cursor()
    sql = adapt_sql(sql)
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    return cur

def fetchone(conn, sql, params=None):
    cur = execute(conn, sql, params)
    return cur.fetchone()

def fetchall(conn, sql, params=None):
    cur = execute(conn, sql, params)
    return cur.fetchall()

def get_lastrowid(cur):
    if _use_postgres():
        row = cur.fetchone()
        if row:
            return row[0] if isinstance(row, (list, tuple)) else row.get('id')
        return None
    return cur.lastrowid

def dictify(row):
    if row is None:
        return None
    return dict(row)

def json_dumps(val):
    if val is None:
        return None
    return json.dumps(val, ensure_ascii=False)

def json_loads(val):
    if val is None:
        return None
    if isinstance(val, (dict, list)):
        return val
    try:
        return json.loads(val)
    except (TypeError, json.JSONDecodeError):
        return val
