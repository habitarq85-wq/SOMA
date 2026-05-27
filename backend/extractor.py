import re
import json
import sqlite3

# Diccionario de palabras clave por eje para el análisis de sentimientos/posicionamiento
KEYWORDS_EJES = {
    "Fachada": {"abierta": 1.0, "transparente": 1.0, "vidrio": 0.8, "cerrada": -1.0, "privada": -0.8, "muro": -1.0, "ciego": -1.0, "privacidad": -0.8},
    "Privacidad": {"abierta": 1.0, "visible": 1.0, "todo se ve": 0.9, "transparente": 0.8, "recibidor": -1.0, "vestíbulo": -1.0, "filtro": -0.9, "insinuar": -0.8, "descubrir": -0.7},
    "Planta": {"espacios únicos": 1.0, "abierta": 1.0, "libre": 1.0, "flexible": 0.7, "fraccionada": -1.0, "muros": -1.0, "dividida": -0.8},
    "Iluminación": {"directa": 1.0, "claro": 0.8, "sol": 0.7, "tenue": -1.0, "penumbra": -1.0, "controlada": -0.8},
    "Tacto": {"textura": 1.0, "rugoso": 1.0, "piedra": 0.8, "liso": -1.0, "uniforme": -1.0, "minimalista": -0.5},
    "Niveles": {"varios": 1.0, "escaleras": 0.8, "vertical": 0.7, "uno": -1.0, "un solo": -1.0, "planta baja": -0.9, "horizontal": -0.8},
    "Paisaje": {"verde": 1.0, "vegetación": 1.0, "jardín": 0.8, "pétreo": -1.0, "mineral": -0.9, "plaza": -0.8},
    "Escala": {"acogedor": -1.0, "fresco": -0.8, "amplio": 1.0, "abierto": 0.8, "monumental": 1.0},
    "Perfil Social": {"activo": 1.0, "fiestas": 1.0, "invitados": 1.0, "visitas": 1.0, "privado": -1.0, "relajación": -0.9, "íntimo": -0.8},
    "Color": {"carácter": 1.0, "acento": 0.9, "vibrante": 0.9, "neutral": -1.0, "calma": -1.0, "blanco": -1.0, "gris": -1.0}

}

def extract_from_text(text):
    results = {}
    for eje, keywords in KEYWORDS_EJES.items():
        score = 0
        matches = 0
        for word, val in keywords.items():
            count = len(re.findall(r'\b' + re.escape(word) + r'\b', text.lower()))
            if count > 0:
                score += val * count
                matches += count
        
        if matches > 0:
            results[eje] = max(-1.0, min(1.0, score / matches))
        else:
            results[eje] = 0.0 # Neutral si no hay keywords
            
    return results

def process_interview_file(file_path, proyecto_id):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        analisis = extract_from_text(content)
        
        # Guardar en DB
        DB_PATH = "/home/juan/Documentos/PROYECTO SOMA/web/EjemploBD/proyectos_arquitectonicos.db"
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        for eje, valor in analisis.items():
            c.execute("""
                INSERT INTO ejes_diseno (proyecto_id, eje, valor_polar, justificacion)
                VALUES (?, ?, ?, ?)
            """, (proyecto_id, eje, valor, f"Extraído automáticamente del archivo: {file_path}"))
            
        conn.commit()
        conn.close()
        return analisis
    except Exception as e:
        print(f"Error procesando entrevista: {e}")
        return None

if __name__ == "__main__":
    # Prueba de extracción
    analisis = process_interview_file("/home/juan/Documentos/PROYECTO SOMA/metodologia/entrevista_prueba.txt", 1)
    if analisis:
        print("Análisis exitoso:")
        for eje, valor in analisis.items():
            print(f"- {eje}: {valor:.2f}")
    else:
        print("Falló la extracción.")
