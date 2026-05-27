import sqlite3

db_path = "/home/juan/Documentos/PROYECTO SOMA/web/EjemploBD/proyectos_arquitectonicos.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Obtener nombres de las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"Tablas encontradas: {tables}")

for table in tables:
    print(f"\nEsquema de la tabla {table[0]}:")
    cursor.execute(f"PRAGMA table_info({table[0]})")
    columns = cursor.fetchall()
    for col in columns:
        print(col)

conn.close()
