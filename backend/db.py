"""
Abstracción de base de datos para SOMA.
Soporta SQLite (desarrollo local) y PostgreSQL (producción en Render).
Selecciona automáticamente según la variable DATABASE_URL.
"""
import os
import sqlite3
import json

DATABASE_URL = os.environ.get('DATABASE_URL', '')
USE_POSTGRES = bool(DATABASE_URL)

def _get_sqlite_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proyecto_dir = os.path.dirname(base_dir)
    return os.path.join(proyecto_dir, "web", "EjemploBD", "proyectos_arquitectonicos.db")

def get_connection():
    if USE_POSTGRES:
        import psycopg2
        from psycopg2.extras import RealDictCursor
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    else:
        db_path = _get_sqlite_path()
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

def adapt_sql(sql):
    if USE_POSTGRES:
        sql = sql.replace('?', '%s')
        sql = sql.replace('IFNULL(', 'COALESCE(')
        sql = sql.replace("datetime('now')", "NOW()")
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
    if USE_POSTGRES:
        row = cur.fetchone()
        if row:
            return row[0] if isinstance(row, (list, tuple)) else row.get('id')
        return None
    return cur.lastrowid

def dictify(row):
    if row is None:
        return None
    if USE_POSTGRES:
        return dict(row)
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
