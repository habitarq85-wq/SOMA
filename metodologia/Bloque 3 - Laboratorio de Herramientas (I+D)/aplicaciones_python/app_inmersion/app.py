from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import datetime
import json
import sqlite3
import subprocess
import threading

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTO_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
AUDIO_DIR = os.path.join(BASE_DIR, 'static', 'audio')
PROYECTOS_DIR = os.path.join(PROYECTO_DIR, 'backend', 'proyectos')
DB_PATH = os.path.join(PROYECTO_DIR, "web", "EjemploBD", "proyectos_arquitectonicos.db")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(PROYECTOS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('entrevista.html')

@app.route('/crear_proyecto', methods=['POST'])
def crear_proyecto():
    data = request.json
    cliente = data.get('cliente', 'Anonimo')
    fecha = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    proyecto_id = f"SOMA-{fecha}"

    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    os.makedirs(carpeta, exist_ok=True)

    info = {
        "proyecto_id": proyecto_id,
        "cliente": cliente,
        "fecha_entrevista": datetime.datetime.now().isoformat(),
        "tiene_audio": False,
        "tiene_transcripcion": False,
        "tiene_analisis": False,
        "estado": "entrevista_realizada"
    }
    with open(os.path.join(carpeta, "info.json"), 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    return jsonify({"status": "success", "proyecto_id": proyecto_id}), 200

@app.route('/guardar_entrevista', methods=['POST'])
def guardar_entrevista():
    proyecto_id = request.form.get('proyecto_id', 'SOMA-desconocido')
    audio = request.files.get('audio')

    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    os.makedirs(carpeta, exist_ok=True)

    if audio:
        filename = f"entrevista_{proyecto_id}.wav"
        filepath = os.path.join(carpeta, filename)
        audio.save(filepath)

    info_path = os.path.join(carpeta, "info.json")
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            info = json.load(f)
    else:
        info = {"proyecto_id": proyecto_id, "cliente": "Anonimo"}

    info["tiene_audio"] = True
    info["estado"] = "audio_guardado"
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    return jsonify({"status": "success", "proyecto_id": proyecto_id}), 200

@app.route('/guardar_datos_entrevista', methods=['POST'])
def guardar_datos_entrevista():
    data = request.json
    proyecto_id = data.get('proyecto_id')
    if not proyecto_id:
        return jsonify({"status": "error", "message": "proyecto_id requerido"}), 400

    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    os.makedirs(carpeta, exist_ok=True)

    info_path = os.path.join(carpeta, "info.json")
    info = {"proyecto_id": proyecto_id}
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            info = json.load(f)

    info["cliente"] = data.get("cliente", info.get("cliente", "Anonimo"))
    info["contacto"] = data.get("contacto", "")
    info["notas_arquitecto"] = data.get("notas", {})
    info["tiene_audio"] = info.get("tiene_audio", False)
    info["estado"] = "datos_capturados"

    activity_matrix = data.get("activity_matrix", [])
    if activity_matrix:
        datos_path = os.path.join(carpeta, "datos_estructurados.json")
        with open(datos_path, 'w', encoding='utf-8') as f:
            json.dump({"activity_matrix": activity_matrix}, f, indent=2, ensure_ascii=False)
        info["tiene_activity_matrix"] = True
        guardar_activity_matrix_db(proyecto_id, activity_matrix)

    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    return jsonify({"status": "success", "proyecto_id": proyecto_id}), 200

def guardar_activity_matrix_db(proyecto_id, matrix):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        for hab in matrix:
            nombre = hab.get("nombre", "Sin nombre")
            c.execute("INSERT INTO habitantes (proyecto_id, nombre) VALUES (?, ?)",
                      (None, nombre))
            hab_id = c.lastrowid
            for slot in hab.get("slots", []):
                hora = slot.get("hora", 0)
                zona = slot.get("zona", "x")
                zona_map = {"s": "Social", "d": "Descanso", "o": "Operativa",
                           "p": "Soporte", "t": "Transicion", "x": "Sin asignar"}
                c.execute("""INSERT INTO actividades
                    (habitante_id, hora, actividad_principal, aislamiento_necesario, iluminacion_deseada, espacio_sugerido)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (hab_id, hora, zona_map.get(zona, "Sin asignar"),
                     3 if zona != "x" else 0,
                     "Natural" if zona in ("s","o") else "Tenue" if zona in ("d","t") else "Variable",
                     zona_map.get(zona, "")))
        conn.commit()
        conn.close()
        print(f"  [SOMA] Activity matrix guardada en DB para {proyecto_id}")
    except Exception as e:
        print(f"  [SOMA] Error DB activity matrix: {e}")

@app.route('/procesar_entrevista', methods=['POST'])
def procesar_entrevista():
    data = request.json
    proyecto_id = data.get('proyecto_id')
    if not proyecto_id:
        return jsonify({"status": "error", "message": "proyecto_id requerido"}), 400

    threading.Thread(target=procesar_en_background, args=(proyecto_id,), daemon=True).start()
    return jsonify({"status": "processing", "message": "Procesando entrevista..."}), 202

def procesar_en_background(proyecto_id):
    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    audio_path = os.path.join(carpeta, f"entrevista_{proyecto_id}.wav")
    info_path = os.path.join(carpeta, "info.json")

    if not os.path.exists(info_path):
        return

    with open(info_path, 'r', encoding='utf-8') as f:
        info = json.load(f)

    if not os.path.exists(audio_path):
        print(f"  [SOMA] No hay audio para {proyecto_id}")
        return

    try:
        from faster_whisper import WhisperModel
        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio_path, language="es")
        transcripcion = " ".join(seg.text for seg in segments)
    except Exception as e:
        transcripcion = f"[Error de transcripción: {e}]"

    with open(os.path.join(carpeta, "transcripcion.txt"), 'w', encoding='utf-8') as f:
        f.write(transcripcion)

    info["tiene_transcripcion"] = True
    info["estado"] = "transcrito"

    try:
        guia = analizar_con_deepseek(proyecto_id, transcripcion, info)
        with open(os.path.join(carpeta, "guia_de_diseno.md"), 'w', encoding='utf-8') as f:
            f.write(guia)

        datos_path = os.path.join(carpeta, "datos_estructurados.json")
        if os.path.exists(datos_path):
            with open(datos_path, 'r', encoding='utf-8') as f:
                info["actividades"] = json.load(f)

        info["tiene_analisis"] = True
        info["estado"] = "completo"
    except Exception as e:
        info["estado"] = f"error_analisis: {e}"
        print(f"  [SOMA] Error DeepSeek: {e}")

    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, ensure_ascii=False)

    guardar_en_db(proyecto_id, info, transcripcion)
    print(f"  [SOMA] Proyecto {proyecto_id} procesado completamente")

def analizar_con_deepseek(proyecto_id, transcripcion, info):
    import requests

    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        return f"""# Guía de Diseño: {proyecto_id}

> Transcripción disponible en `transcripcion.txt`
> DeepSeek no configurado. Define DEEPSEEK_API_KEY para activar el análisis automático.

---

## Transcripción Cruda

{transcripcion}
"""

    prompt = f"""Eres el arquitecto principal de SOMA, un taller de diseño que aplica:
- Psicología Ambiental
- Lenguaje de Patrones (Christopher Alexander)
- Space Syntax
- Environmental Behavior
- Evaluación Post-Ocupación (POE)
- Proxémica

A partir de la siguiente transcripción de entrevista con un cliente, genera:

## 1. PERFIL DEL PROYECTO
Resumen del cliente, tipo de proyecto, necesidades principales.

## 2. HABITANTES
Lista de habitantes con edades, roles, necesidades de accesibilidad.

## 3. PROGRAMA ARQUITECTÓNICO
Espacios solicitados y espacios complementarios sugeridos.

## 4. ACTIVITY MATRIX (24 SLOTS)
Para cada habitante, tabla hora por hora con: actividad, nivel de aislamiento (1-5), tipo de iluminación, zona SOMA (Social/Descanso/Operativa/Soporte/Transición).

## 5. ANÁLISIS MULTIDIMENSIONAL
- Psicología Ambiental aplicada
- Patrones de Alexander relevantes
- Space Syntax: conectividad, integración
- Environmental Behavior: rutinas, territorialidad
- POE: recomendaciones post-ocupación
- Proxémica: distancias, burbujas personales

## 6. EJES DE INMERSIÓN (10 ejes)
Posicionamiento en cada eje Fachada, Habitaciones, Ambiente, Luz, Acabados, Altura, Exterior, Sensación, Vida Social, Color.

## 7. RECOMENDACIONES DE DISEÑO
Directrices específicas para el proyecto.

Información del cliente: {json.dumps(info, ensure_ascii=False)}

TRANSCRIPCIÓN:
{transcripcion}

Devuelve SOLO el documento en formato Markdown."""
    
    try:
        resp = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 8000
            },
            timeout=120
        )
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"]
        else:
            return f"# Error DeepSeek\nCódigo: {resp.status_code}\n{resp.text}"
    except Exception as e:
        return f"# Error de conexión\n{str(e)}"

def guardar_en_db(proyecto_id, info, transcripcion):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("""UPDATE captura_web SET
            analisis_procesado = ?,
            fecha = ?
            WHERE temp_id = ?""",
            (transcripcion[:5000], datetime.datetime.now().isoformat(), proyecto_id))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"  [SOMA] Error DB: {e}")

@app.route('/proyectos', methods=['GET'])
def listar_proyectos():
    proyectos = []
    if os.path.exists(PROYECTOS_DIR):
        for p in sorted(os.listdir(PROYECTOS_DIR), reverse=True):
            info_path = os.path.join(PROYECTOS_DIR, p, "info.json")
            if os.path.exists(info_path):
                with open(info_path, 'r', encoding='utf-8') as f:
                    info = json.load(f)
                info["carpeta"] = p
                datos_path = os.path.join(PROYECTOS_DIR, p, "datos_estructurados.json")
                if os.path.exists(datos_path):
                    with open(datos_path, 'r', encoding='utf-8') as f:
                        info["datos"] = json.load(f)
                proyectos.append(info)
    return jsonify(proyectos), 200

@app.route('/proyectos/<proyecto_id>/guia')
def descargar_guia(proyecto_id):
    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    return send_from_directory(carpeta, "guia_de_diseno.md", mimetype="text/markdown")

@app.route('/proyectos/<proyecto_id>/audio')
def descargar_audio(proyecto_id):
    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    return send_from_directory(carpeta, f"entrevista_{proyecto_id}.wav")

@app.route('/proyectos/<proyecto_id>/datos')
def obtener_datos(proyecto_id):
    carpeta = os.path.join(PROYECTOS_DIR, proyecto_id)
    datos_path = os.path.join(carpeta, "datos_estructurados.json")
    if os.path.exists(datos_path):
        with open(datos_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f)), 200
    return jsonify({"status": "no_data"}), 200

if __name__ == '__main__':
    app.run(port=5050, debug=True)
