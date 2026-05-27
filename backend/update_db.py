import sqlite3

db_path = "/home/juan/Documentos/PROYECTO SOMA/web/EjemploBD/proyectos_arquitectonicos.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Crear tabla de capturas temporales de la web
c.execute('''CREATE TABLE IF NOT EXISTS captura_web 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              temp_id TEXT,
              contacto TEXT, 
              m2 REAL,
              honorarios_diseno REAL,
              inversion_obra_estimada REAL,
              nivel_proyecto TEXT,
              respuestas_json TEXT, 
              analisis_procesado TEXT,
              fecha TEXT,
              estado TEXT DEFAULT 'pendiente')''')

conn.commit()
conn.close()
print("Tabla 'captura_web' creada exitosamente.")
