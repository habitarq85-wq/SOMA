import sqlite3
import os

DB_PATH = "/home/juan/Documentos/PROYECTO SOMA/web/EjemploBD/proyectos_arquitectonicos.db"

def update_schema():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 1. Tabla de Habitantes (UserEntity)
    c.execute("""
    CREATE TABLE IF NOT EXISTS habitantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER,
        nombre TEXT,
        edad INTEGER,
        genero TEXT,
        estatura_cm REAL,
        peso_kg REAL,
        hobbies TEXT,
        rol_poder TEXT, -- Ejemplo: Principal, Secundario, Dependiente
        observaciones TEXT,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
    )
    """)

    # 2. Tabla de Actividades (ActivityMatrix)
    # Representa los 24 slots por habitante
    c.execute("""
    CREATE TABLE IF NOT EXISTS actividades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habitante_id INTEGER,
        hora INTEGER, -- 0 a 23
        actividad_principal TEXT,
        aislamiento_necesario INTEGER, -- 1 a 5
        iluminacion_deseada TEXT, -- Natural, Artificial, Tenue, etc.
        espacio_sugerido TEXT,
        FOREIGN KEY (habitante_id) REFERENCES habitantes(id)
    )
    """)

    # 3. Tabla de Ejes de Diseño (CreativeCore / Inmersión)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ejes_diseno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER,
        eje TEXT, -- Ejemplo: 'Fachada', 'Privacidad', etc.
        valor_polar REAL, -- -1.0 a 1.0 (ej: -1 = Cerrado, 1 = Abierto)
        justificacion TEXT,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
    )
    """)

    # 4. Tabla de Matriz de Inversión (Finanzas)
    c.execute("""
    CREATE TABLE IF NOT EXISTS matriz_inversion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proyecto_id INTEGER,
        categoria TEXT, -- Estructura, Acabados, Instalaciones, Paisaje
        prioridad_gasto INTEGER, -- 1 a 3 (Esencial, Integral, Complejo)
        porcentaje_asignado REAL,
        monto_estimado REAL,
        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
    )
    """)

    conn.commit()
    conn.close()
    print("Esquema actualizado exitosamente: Habitantes, Actividades, Ejes y Finanzas.")

if __name__ == "__main__":
    update_schema()
