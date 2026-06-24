from flask import Flask, request, jsonify, send_from_directory, send_file, Response, redirect
from flask_cors import CORS
import datetime
import json
import os
import re
import sys
import urllib.request
import urllib.error
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db import get_connection, execute, fetchone, fetchall, get_lastrowid, dictify, json_loads

app = Flask(__name__)
CORS(app)

# Basic Auth to protect dashboard and admin/API endpoints
def check_auth(username, password):
    expected_user = os.environ.get('DASHBOARD_USER', 'admin')
    expected_pass = os.environ.get('DASHBOARD_PASS', 'Yucata85')
    return username == expected_user and password == expected_pass

def authenticate():
    return Response(
        'Acceso restringido. Introduce las credenciales correctas.', 401,
        {'WWW-Authenticate': 'Basic realm="Login SOMA"'}
    )

@app.before_request
def require_login():
    public_paths = ['/', '/save_immersion', '/tarjeta']
    public_prefixes = ['/web/', '/css/', '/recursos_graficos/', '/backend/']
    path = request.path
    if path in public_paths or any(path.startswith(pref) for pref in public_prefixes):
        return None
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTO_DIR = os.path.dirname(BASE_DIR)
DIAGNOSTICOS_PATH = os.path.join(BASE_DIR, "diagnosticos_master.json")
REPORTES_DIR = os.path.join(BASE_DIR, "reportes")
EMAIL_DESTINO = "habitarq85@gmail.com"

SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com").strip()
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587").strip())
SMTP_USER = os.environ.get("SMTP_USER", "").strip()
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "").strip()
SMTP_USE_SSL = os.environ.get("SMTP_USE_SSL", "false").strip().lower() == "true"
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "").strip()

MINIMO_TALLER = 6500
RANGOS_OBRA = {
    250: {"min": 14000, "max": 16500},
    350: {"min": 18500, "max": 23000},
    850: {"min": 28000, "max": 40000}
}

os.makedirs(REPORTES_DIR, exist_ok=True)

UNIDADES = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
DIEZ_DIECINUEVE = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
DECENAS = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
CENTENAS = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def num_to_words(n):
    if n == 0: return "cero"
    entero = int(n)
    decimal = round((n - entero) * 100)
    def convertir(num):
        if num == 0: return ""
        if num < 10: return UNIDADES[num]
        if num < 20: return DIEZ_DIECINUEVE[num - 10]
        if num < 100:
            d = num // 10
            u = num % 10
            if u == 0: return DECENAS[d]
            if d == 2: return f"veinti{u}" if u > 0 else "veinte"
            return f"{DECENAS[d]} y {UNIDADES[u]}"
        if num < 1000:
            c = num // 100
            resto = num % 100
            if c == 1 and resto == 0: return "cien"
            base = "cien" if c == 1 else CENTENAS[c]
            return f"{base} {convertir(resto)}".strip() if resto else base
        if num < 1000000:
            miles = num // 1000
            resto = num % 1000
            base = convertir(miles) + (" mil" if miles > 1 else "mil")
            return f"{base} {convertir(resto)}".strip() if resto else base
        mill = num // 1000000
        resto = num % 1000000
        base = convertir(mill) + (" millones" if mill > 1 else " millón")
        return f"{base} {convertir(resto)}".strip() if resto else base
    resultado = convertir(entero)
    if decimal > 0:
        resultado += f" con {decimal:02d}/100"
    else:
        resultado += " con 00/100"
    return resultado.upper()

def init_db():
    conn = get_connection()
    use_pg = bool(os.environ.get('DATABASE_URL', ''))
    tables = {
        'captura_web': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('temp_id', 'TEXT'), ('contacto', 'TEXT'),
            ('respuestas_json', 'TEXT'), ('analisis_procesado', 'TEXT'),
            ('fecha', 'TEXT'), ('estado', 'TEXT'), ('m2', 'REAL'),
            ('honorarios_diseno', 'REAL'), ('inversion_obra_estimada', 'REAL'),
            ('nivel_proyecto', 'TEXT'), ("pipeline_estado", "TEXT DEFAULT 'lead'"),
            ('nombre_cliente', 'TEXT'), ('nombre_proyecto', 'TEXT'),
            ('tipo_proyecto', 'TEXT'), ('ubicacion', 'TEXT'),
            ("estado_contacto", "TEXT DEFAULT 'pendiente'"),
        ],
        'cobros': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('concepto', 'TEXT'), ('monto', 'REAL'),
            ('fecha_vencimiento', 'TEXT'), ('fecha_pago', 'TEXT'),
            ("estado", "TEXT DEFAULT 'pendiente'"), ('metodo_pago', 'TEXT'), ('notas', 'TEXT'),
        ],
        'programa_arquitectonico': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('lead_id', 'INTEGER'), ('tipo', 'TEXT'), ('espacio', 'TEXT'), ('area', 'REAL'),
            ('zona', 'INTEGER'), ('horario_inicio', 'TEXT'), ('horario_fin', 'TEXT'),
            ('mobiliario', 'TEXT'), ('acontecimientos', 'TEXT'), ('patrones_espaciales', 'TEXT'),
            ('usuarios', 'INTEGER'), ('clave', 'TEXT'), ('relacion_directa', 'TEXT'),
        ],
        'egresos': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('categoria', 'TEXT'), ('concepto', 'TEXT'), ('monto', 'REAL'),
            ('fecha', 'TEXT'),
        ],
        'matriz_inversion': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('categoria', 'TEXT'), ('prioridad_gasto', 'INTEGER'),
            ('porcentaje_asignado', 'REAL'), ('monto_estimado', 'REAL'),
        ],
        'fondos': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('nombre', 'TEXT'), ('monto_mensual', 'REAL DEFAULT 0'),
            ('balance_actual', 'REAL DEFAULT 0'),
        ],
        'movimientos_fondo': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('fondo_id', 'INTEGER'), ('tipo', 'TEXT'),
            ('monto', 'REAL'), ('fecha', 'TEXT'), ('concepto', 'TEXT'),
        ],
        'algoritmo_progreso': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('seccion', 'INTEGER'),
            ('paso', 'TEXT'), ('estado', 'TEXT DEFAULT \'PENDIENTE\''),
            ('updated_at', 'TEXT'),
        ],
    }
    for table_name, columns in tables.items():
        cols_sql = ", ".join(f"{name} {typ}" for name, typ in columns)
        execute(conn, f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_sql})")

    # Migración: agregar columnas faltantes
    nuevas_columnas = [
        ('m2_original', 'REAL'), ('nivel_original', 'TEXT'),
        ('honorarios_original', 'REAL'),
        ('calle_numero', 'TEXT DEFAULT \'\''),
        ('colonia', 'TEXT DEFAULT \'\''),
        ('ciudad', 'TEXT DEFAULT \'\''),
        ('estado_ubic', 'TEXT DEFAULT \'\''),
    ]
    for col_name, col_type in nuevas_columnas:
        try:
            if use_pg:
                execute(conn, f"ALTER TABLE captura_web ADD COLUMN IF NOT EXISTS {col_name} {col_type}")
            else:
                execute(conn, f"ALTER TABLE captura_web ADD COLUMN {col_name} {col_type}")
        except Exception:
            pass
    conn.commit()
    conn.close()

init_db()

try:
    with open(DIAGNOSTICOS_PATH, 'r', encoding='utf-8') as f:
        MASTER_DIAGNOSTICOS = json.load(f)
except Exception as e:
    print(f"Error cargando base de conocimiento: {e}")
    MASTER_DIAGNOSTICOS = {}

def enviar_correo(destinatario, asunto, cuerpo):
    filename = f"reporte_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(REPORTES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Para: {destinatario}\n")
        f.write(f"Asunto: {asunto}\n")
        f.write("="*60 + "\n\n")
        f.write(cuerpo)
    print(f"\n--- REPORTE GUARDADO: {filepath} ---")

    if not SENDGRID_API_KEY:
        print("--- SENDGRID_API_KEY no configurada ---")
        return False, "SENDGRID_API_KEY no configurada"

    try:
        message = Mail(
            from_email="info@soma-arquitectura.com",
            to_emails=destinatario,
            subject=asunto,
            plain_text_content=cuerpo
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code in (200, 201, 202):
            print(f"--- CORREO ENVIADO a {destinatario} via SendGrid ---")
            return True, None
        else:
            print(f"--- ERROR SENDGRID: status {response.status_code} ---")
            return False, f"SendGrid status {response.status_code}"
    except Exception as e:
        print(f"--- ERROR AL ENVIAR CORREO: {e} ---")
        return False, str(e)

def enviar_whatsapp(contacto, temp_id, nivel_key, m2):
    mensaje = f"🔔 NUEVO LEAD SOMA\nID: {temp_id}\nCliente: {contacto}\nPaquete: {nivel_key.upper()}\nEscala: {m2:.0f} m²"
    wa_host = os.environ.get("WA_SERVICE_HOST", "http://127.0.0.1:3001")
    try:
        payload = json.dumps({"message": mensaje}).encode()
        req = urllib.request.Request(
            f"{wa_host}/send",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        resp = urllib.request.urlopen(req, timeout=5)
        if resp.status == 200:
            print("--- WHATSAPP ENVIADO (Baileys) ---")
            return True
    except Exception as e:
        print(f"--- WHATSAPP NO DISPONIBLE (Baileys): {e} ---")
        return False

@app.route('/save_immersion', methods=['POST'])
def save_immersion():
    data = request.json
    respuestas = data.get('respuestas', {})
    contacto = data.get('contacto', 'Anónimo')
    cotizacion = data.get('cotizacion', {})
    fecha_hoy = datetime.datetime.now().strftime("%d%m%Y-%H%M")
    temp_id = f"SOMA-{fecha_hoy}"

    m2 = cotizacion.get('m2', 0)
    precio_diseno_m2 = cotizacion.get('precioDiseno', 0)

    nivel_map = {250: "esencial", 350: "integral", 850: "ejecutivo"}
    nivel_key = nivel_map.get(precio_diseno_m2, "esencial")

    total_diseno = m2 * precio_diseno_m2
    if 0 < total_diseno < MINIMO_TALLER:
        total_diseno = MINIMO_TALLER

    rango = RANGOS_OBRA.get(precio_diseno_m2, {"min": 18500, "max": 23000})
    obra_min = m2 * rango["min"]
    obra_max = m2 * rango["max"]

    # --- CONSTRUCCIÓN DEL REPORTE ---
    reporte = f"========== REPORTE TÉCNICO DE INMERSIÓN ==========\n"
    reporte += f"ID: {temp_id}\n"
    reporte += f"Cliente: {contacto}\n"
    reporte += f"Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"

    reporte += "--- ANÁLISIS MULTIDIMENSIONAL ---\n"
    for step, val in respuestas.items():
        if step in MASTER_DIAGNOSTICOS and val in MASTER_DIAGNOSTICOS[step]:
            d = MASTER_DIAGNOSTICOS[step][val]
            reporte += f"\n▶ {d['titulo']}\n"
            reporte += f"   Psicología Ambiental: {d['psicologia_ambiental']}\n"
            reporte += f"   Lenguaje de Patrones: {d['lenguaje_patrones']}\n"
            reporte += f"   Space Syntax: {d['space_syntax']}\n"
            reporte += f"   Conducta Ambiental: {d['environmental_behavior']}\n"
            reporte += f"   POE: {d['poe']}\n"

    reporte += f"\n--- VIABILIDAD ECONÓMICA (Nivel: {nivel_key.upper()}) ---\n"
    reporte += f"Escala Estimada: {m2:.2f} m²\n"
    reporte += f"Honorarios Diseño SOMA: ${total_diseno:,.2f}\n"
    reporte += f"Inversión de Obra (Paramétrica): ${obra_min:,.2f} - ${obra_max:,.2f}\n"
    reporte += "\n*Nota: Costos paramétricos regionales para Yucatán.\n"

    # --- GUARDAR EN BASE DE DATOS ---
    try:
        conn = get_connection()
        cur = execute(conn, """INSERT INTO captura_web
                     (temp_id, contacto, m2, honorarios_diseno, inversion_obra_estimada, nivel_proyecto, respuestas_json, analisis_procesado, fecha, m2_original, nivel_original, honorarios_original)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (temp_id, contacto, m2, total_diseno, obra_min, nivel_key,
                   json.dumps(respuestas), reporte, datetime.datetime.now().isoformat(),
                   m2, nivel_key, total_diseno))
        proyecto_id = get_lastrowid(cur)

        obra_promedio = (obra_min + obra_max) / 2
        inversion_total = total_diseno + obra_promedio

        execute(conn, """INSERT INTO matriz_inversion
                     (proyecto_id, categoria, prioridad_gasto, porcentaje_asignado, monto_estimado)
                     VALUES (?, ?, ?, ?, ?)""",
                  (proyecto_id, "Alcance Construcción (Promedio)", 5,
                   obra_promedio / inversion_total if inversion_total > 0 else 0, obra_promedio))

        execute(conn, """INSERT INTO matriz_inversion
                     (proyecto_id, categoria, prioridad_gasto, porcentaje_asignado, monto_estimado)
                     VALUES (?, ?, ?, ?, ?)""",
                  (proyecto_id, f"Diseño SOMA ({nivel_key.capitalize()})", 5,
                   total_diseno / inversion_total if inversion_total > 0 else 0, total_diseno))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error DB: {e}")
        try: conn.close()
        except: pass

    # --- ENVÍO SINCRÓNICO (confiable) ---
    asunto = f"NUEVO LEAD SOMA: {temp_id}"
    cuerpo = f"Se ha registrado una nueva inmersión.\n\nContacto: {contacto}\nID: {temp_id}\n\n{reporte}"
    email_ok, smtp_error = enviar_correo(EMAIL_DESTINO, asunto, cuerpo)
    whatsapp_ok = enviar_whatsapp(contacto, temp_id, nivel_key, m2)

    print(f"\n{'='*50}")
    print(f"🔔 NUEVO LEAD SOMA")
    print(f"   ID: {temp_id}")
    print(f"   Contacto: {contacto}")
    print(f"   Reporte: backend/reportes/")
    print(f"{'='*50}\n")

    return jsonify({
        "status": "success",
        "temp_id": temp_id,
        "email": "sent" if email_ok else "failed",
        "smtp_error": smtp_error,
        "whatsapp": "sent" if whatsapp_ok else "failed"
    }), 200

@app.route('/activity_matrix/<temp_id>', methods=['GET'])
def get_activity_matrix(temp_id):
    carpeta = os.path.join(PROYECTO_DIR, "backend", "proyectos", temp_id)
    datos_path = os.path.join(carpeta, "datos_estructurados.json")
    try:
        with open(datos_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        matrix = data.get("activity_matrix", [])
        if matrix:
            return jsonify({"status": "success", "matrix": matrix}), 200
    except FileNotFoundError:
        pass
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    # Fallback: leer actividades desde DB
    try:
        conn = get_connection()
        rows = fetchall(conn, """
            SELECT h.nombre, a.hora, a.actividad_principal,
                   a.aislamiento_necesario, a.iluminacion_deseada, a.espacio_sugerido
            FROM actividades a
            JOIN habitantes h ON h.id = a.habitante_id
            ORDER BY h.id, a.hora
        """)
        conn.close()

        if not rows:
            return jsonify({"status": "empty", "matrix": []}), 200

        habitantes = {}
        for r in rows:
            nombre = r["nombre"] or "Habitante"
            if nombre not in habitantes:
                habitantes[nombre] = {"nombre": nombre, "slots": []}
            z = r["espacio_sugerido"] or ""
            zona_clave = {
                "social": "s", "descanso": "d", "operativa": "o",
                "soporte": "p", "transición": "t", "transicion": "t"
            }.get(z.lower().strip(), "x")
            habitantes[nombre]["slots"].append({
                "hora": r["hora"],
                "actividad": r["actividad_principal"] or "",
                "aislamiento": r["aislamiento_necesario"],
                "iluminacion": r["iluminacion_deseada"] or "",
                "zona": zona_clave
            })

        return jsonify({"status": "success", "matrix": list(habitantes.values())}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---- PROGRAMA ARQUITECTONICO ----
PRECIOS_M2 = {"esencial": 250, "integral": 350, "ejecutivo": 850}

INMERSION_PREGUNTAS = {
    "step1": {"pregunta": "Fachada", "A": "Abierta", "B": "Cerrada"},
    "step2": {"pregunta": "Privacidad", "A": "Abiertos y francos", "B": "Protegidos"},
    "step3": {"pregunta": "Espacios", "A": "Amplios e integrados", "B": "Divididos por muros"},
    "step4": {"pregunta": "Iluminación", "A": "Mucha luz natural", "B": "Luz suave"},
    "step5": {"pregunta": "Estilo", "A": "Texturas y ornamentos", "B": "Lisos y sobrios"},
    "step6": {"pregunta": "Niveles", "A": "Un nivel", "B": "Varios niveles"},
    "step7": {"pregunta": "Exteriores", "A": "Mucho jardín", "B": "Plaza pétrea"},
    "step8": {"pregunta": "Sensación", "A": "Abiertos y altos", "B": "Acogedores e íntimos"},
    "step9": {"pregunta": "Vida Social", "A": "Activa", "B": "Introvertida"},
    "step10": {"pregunta": "Color", "A": "Neutros", "B": "Llamativos"},
}

@app.route('/programa/<int:lead_id>', methods=['GET'])
def get_programa(lead_id):
    try:
        conn = get_connection()
        rows = fetchall(conn, "SELECT * FROM programa_arquitectonico WHERE lead_id = ? ORDER BY tipo, id", (lead_id,))
        conn.close()
        return jsonify([dictify(row) for row in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/programa/espacio', methods=['POST'])
def crear_espacio():
    try:
        data = request.json
        conn = get_connection()
        cur = execute(conn, """INSERT INTO programa_arquitectonico
                     (lead_id, tipo, espacio, area, zona, horario_inicio, horario_fin,
                      mobiliario, acontecimientos, patrones_espaciales, usuarios, clave, relacion_directa)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                  (data['lead_id'], data['tipo'], data['espacio'], data.get('area', 0),
                   data.get('zona', 1), data.get('horario_inicio', ''),
                   data.get('horario_fin', ''), json.dumps(data.get('mobiliario', [])),
                   json.dumps(data.get('acontecimientos', [])),
                   json.dumps(data.get('patrones_espaciales', [])),
                   data.get('usuarios', 0), data.get('clave', ''),
                   json.dumps(data.get('relacion_directa', []))))
        conn.commit()
        esp_id = get_lastrowid(cur)
        conn.close()
        return jsonify({"status": "success", "id": esp_id}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/programa/espacio/<int:espacio_id>', methods=['PUT'])
def actualizar_espacio(espacio_id):
    try:
        data = request.json
        conn = get_connection()
        execute(conn, """UPDATE programa_arquitectonico SET
                     espacio=?, area=?, zona=?, horario_inicio=?, horario_fin=?,
                     mobiliario=?, acontecimientos=?, patrones_espaciales=?,
                     usuarios=?, clave=?, relacion_directa=?
                     WHERE id=?""",
                  (data['espacio'], data.get('area', 0), data.get('zona', 1),
                   data.get('horario_inicio', ''), data.get('horario_fin', ''),
                   json.dumps(data.get('mobiliario', [])),
                   json.dumps(data.get('acontecimientos', [])),
                   json.dumps(data.get('patrones_espaciales', [])),
                   data.get('usuarios', 0), data.get('clave', ''),
                   json.dumps(data.get('relacion_directa', [])), espacio_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/programa/espacio/<int:espacio_id>/relaciones', methods=['PUT'])
def guardar_relaciones_espacio(espacio_id):
    try:
        data = request.json
        relaciones = data.get('relaciones', [])
        conn = get_connection()
        execute(conn, "UPDATE programa_arquitectonico SET relacion_directa=? WHERE id=?",
                (json.dumps(relaciones), espacio_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/programa/espacio/<int:espacio_id>', methods=['DELETE'])
def eliminar_espacio(espacio_id):
    try:
        conn = get_connection()
        execute(conn, "DELETE FROM programa_arquitectonico WHERE id=?", (espacio_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cotizacion/<int:lead_id>', methods=['GET'])
def get_cotizacion(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT id, contacto, nombre_cliente, nombre_proyecto, m2, nivel_proyecto, honorarios_diseno FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return jsonify({"status": "error", "message": "Lead no encontrado"}), 404

        totales_rows = fetchall(conn, "SELECT tipo, SUM(area) as total FROM programa_arquitectonico WHERE lead_id=? GROUP BY tipo", (lead_id,))
        totales_por_tipo = {r["tipo"]: r["total"] for r in totales_rows}

        total_m2_row = fetchone(conn, "SELECT SUM(area) as total FROM programa_arquitectonico WHERE lead_id=?", (lead_id,))
        total_m2 = (total_m2_row["total"] or 0) if total_m2_row else 0
        conn.close()

        contacto = lead["contacto"]
        nombre_cliente = lead["nombre_cliente"]
        nombre_proyecto = lead["nombre_proyecto"]
        m2_lead = lead["m2"]
        nivel = lead["nivel_proyecto"]
        honorarios_lead = lead["honorarios_diseno"]
        nivel_key = nivel or "esencial"
        precio_m2 = PRECIOS_M2.get(nivel_key, 250)
        honorarios_reales = max(total_m2 * precio_m2, MINIMO_TALLER)
        rango = RANGOS_OBRA.get(precio_m2, {"min": 18500, "max": 23000})

        return jsonify({
            "lead_id": lead_id,
            "contacto": contacto,
            "nombre_cliente": nombre_cliente,
            "nombre_proyecto": nombre_proyecto,
            "nivel": nivel_key,
            "m2_lead_original": m2_lead,
            "m2_programa_real": total_m2,
            "totales_por_tipo": totales_por_tipo,
            "precio_m2": precio_m2,
            "honorarios_reales": honorarios_reales,
            "honorarios_lead_original": honorarios_lead,
            "obra_min_estimada": total_m2 * rango["min"],
            "obra_max_estimada": total_m2 * rango["max"]
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cotizacion/<int:lead_id>/pdf', methods=['GET'])
def cotizacion_pdf(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT id, contacto, nombre_cliente, nombre_proyecto, m2, nivel_proyecto, honorarios_diseno, temp_id FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Lead no encontrado", 404
        contacto = lead["contacto"]
        nombre_cliente = lead["nombre_cliente"] or lead["nombre_proyecto"] or contacto
        m2_lead = lead["m2"]
        nivel = lead["nivel_proyecto"]
        honorarios_lead = lead["honorarios_diseno"]
        temp_id = lead["temp_id"]
        nivel_key = nivel or "esencial"
        precio_m2 = PRECIOS_M2.get(nivel_key, 250)
        espacios_rows = fetchall(conn, "SELECT tipo, espacio, area, zona, clave FROM programa_arquitectonico WHERE lead_id=? ORDER BY tipo, id", (lead_id,))
        espacios = [(r["tipo"], r["espacio"], r["area"], r["zona"], r["clave"]) for r in espacios_rows]
        total_m2 = sum(e[2] or 0 for e in espacios)
        honorarios = max(total_m2 * precio_m2, MINIMO_TALLER)
        rango = RANGOS_OBRA.get(precio_m2, {"min": 18500, "max": 23000})
        conn.close()

        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        filas = "".join(
            f"<tr><td>{e[0]}</td><td>{e[1] or '?'}</td><td style='text-align:right'>{e[2] or 0:.1f}</td>"
            f"<td style='text-align:center'>{e[3]}</td><td style='text-align:center'>{e[4] or '--'}</td></tr>"
            for e in espacios
        )

        html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'>
<title>COTIZACIÓN SOMA — {contacto}</title>
<style>
@page {{ margin: 2cm; }}
body {{ font-family: 'Helvetica', 'Arial', sans-serif; color: #1a1a1a; font-size: 11pt; line-height: 1.5; }}
.header {{ text-align: center; margin-bottom: 30px; }}
.header h1 {{ font-size: 28pt; letter-spacing: 4px; margin: 0; }}
.header h2 {{ font-size: 10pt; color: #a6937c; font-weight: normal; margin: 5px 0 0; }}
hr {{ border: none; border-top: 2px solid #000; margin: 20px 0; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9pt; margin: 15px 0; }}
th {{ background: #1a1a1a; color: #fff; padding: 6px; text-align: left; font-size: 8pt; text-transform: uppercase; }}
td {{ padding: 5px 6px; border-bottom: 1px solid #ddd; }}
.total-row td {{ border-top: 2px solid #000; font-weight: bold; }}
.resumen {{ background: #f4f1ea; padding: 15px; margin: 15px 0; }}
.resumen div {{ display: flex; justify-content: space-between; padding: 3px 0; }}
.esquema-pagos {{ margin: 15px 0; padding: 12px; border: 1px solid #1a1a1a; }}
.esquema-pagos h4 {{ margin: 0 0 8px 0; font-size: 9pt; text-transform: uppercase; }}
.esquema-pagos table {{ font-size: 8.5pt; }}
.esquema-pagos td {{ padding: 4px 6px; }}
.footer {{ margin-top: 30px; font-size: 8pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }}
</style></head><body>
<div class='header'>
<h1>SOMA</h1>
<h2>COTIZACIÓN DE DISEÑO ARQUITECTÓNICO</h2>
<hr>
</div>
<p><strong>Cliente:</strong> {nombre_cliente}</p>
<p><strong>ID:</strong> {temp_id or '---'} &nbsp;|&nbsp; <strong>Fecha:</strong> {fecha}</p>
<p><strong>Paquete:</strong> {nivel_key.upper()}</p>
<hr>
<h3>PROGRAMA ARQUITECTÓNICO</h3>
<table>
<tr><th>Tipo</th><th>Espacio</th><th style='text-align:right'>m²</th><th style='text-align:center'>Zona</th><th style='text-align:center'>Clave</th></tr>
{filas}
<tr class='total-row'><td colspan='2'><strong>TOTAL</strong></td>
<td style='text-align:right'><strong>{total_m2:.1f} m²</strong></td><td></td><td></td></tr>
</table>
<div class='resumen'>
<div><span>Honorarios de Diseño SOMA ({nivel_key.capitalize()})</span><span><strong>${honorarios:,.2f}</strong></span></div>
</div>
<div class='esquema-pagos'>
<h4>Esquema de Pagos</h4>
<table>
<tr><th>Pago</th><th>Porcentaje</th><th style='text-align:right'>Monto</th><th>Disparador</th></tr>
<tr><td>Anticipo</td><td>30%</td><td style='text-align:right'>${honorarios*0.3:,.2f}</td><td>Firma de contrato</td></tr>
<tr><td>Segundo pago</td><td>40%</td><td style='text-align:right'>${honorarios*0.4:,.2f}</td><td>Entrega de anteproyecto</td></tr>
<tr><td>Tercer pago</td><td>30%</td><td style='text-align:right'>${honorarios*0.3:,.2f}</td><td>Entrega final</td></tr>
<tr style='font-weight:bold;border-top:2px solid #000;'><td>Total</td><td>100%</td><td style='text-align:right'>${honorarios:,.2f}</td><td></td></tr>
</table>
</div>
<div class='footer'>
<p>SOMA Arquitectura — {fecha}</p>
<p>Arq. Juan Carlos · info@soma-arquitectura.com</p>
<p style='margin-top:8px;font-size:7.5pt;color:#666;'>Cotización válida por 30 días. Los honorarios se ajustarán si el programa arquitectónico final difiere del presentado. Esta cotización cubre únicamente servicios de diseño arquitectónico; los costos de construcción son estimados paramétricos referenciales.</p>
</div>
</body></html>"""
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/lead/<int:lead_id>/cierre-pdf', methods=['GET'])
def cierre_pdf(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT * FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Proyecto no encontrado", 404
        cobros_rows = fetchall(conn, "SELECT concepto, monto, estado, fecha_pago FROM cobros WHERE proyecto_id=? ORDER BY id", (lead_id,))
        prog_rows = fetchall(conn, "SELECT espacio, area, tipo, clave FROM programa_arquitectonico WHERE lead_id=? ORDER BY id", (lead_id,))
        conn.close()

        contacto = lead["contacto"] or "—"
        nombre_cliente = lead["nombre_cliente"] or contacto
        nombre_proyecto = lead["nombre_proyecto"] or "—"
        tipo_proyecto = lead["tipo_proyecto"] or "—"
        nivel = lead["nivel_proyecto"] or "—"
        m2_lead = lead["m2"] or 0
        honorarios = lead["honorarios_diseno"] or 0
        nivel_orig = lead["nivel_original"] or "—"
        m2_orig = lead["m2_original"] or 0
        honorarios_orig = lead["honorarios_original"] or 0
        temp_id = lead["temp_id"] or "—"
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        parts = [lead.get("calle_numero","") or "", lead.get("colonia","") or "",
                 lead.get("ciudad","") or "", lead.get("estado_ubic","") or ""]
        ubic_str = ", ".join(p for p in parts if p)

        filas_cobros = "".join(
            f"<tr><td>{r['concepto'] or '—'}</td><td style='text-align:right'>${r['monto']:,.2f}</td>"
            f"<td style='text-align:center'>{r['estado'] or 'pendiente'}</td>"
            f"<td style='text-align:center'>{r['fecha_pago'] or '—'}</td></tr>"
            for r in cobros_rows
        )
        total_pagado = sum(r['monto'] for r in cobros_rows if r['estado'] == 'pagado')
        total_pendiente = sum(r['monto'] for r in cobros_rows if r['estado'] == 'pendiente')

        filas_prog = "".join(
            f"<tr><td>{r['tipo'] or '—'}</td><td>{r['espacio'] or '—'}</td>"
            f"<td style='text-align:right'>{r['area'] or 0:.1f}</td><td style='text-align:center'>{r['clave'] or '—'}</td></tr>"
            for r in prog_rows
        )

        respuestas_lines2 = ""
        try:
            raw = json.loads(lead["respuestas_json"] or "{}")
            for k, v in raw.items():
                num = k.replace("step","").replace("Pregunta ","")
                if isinstance(v, dict):
                    r = (v.get("r") or v.get("selected") or "")
                    lbl = (v.get("label") or "")
                    respuestas_lines2 += f"<div>Pregunta {num}: {r.upper() if r else '?'}. {lbl}</div>"
                elif isinstance(v, str) and v.strip():
                    info = INMERSION_PREGUNTAS.get(k)
                    if info:
                        opt = info.get(v.strip().upper(), "")
                        respuestas_lines2 += f"<div>Pregunta {num}: {v.strip().upper()}. {opt}</div>"
                    else:
                        respuestas_lines2 += f"<div>Pregunta {num}: {v.strip().upper()}</div>"
        except:
            pass

        espacio_count = len(prog_rows)
        html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'>
<title>CIERRE DE PROYECTO — {nombre_cliente}</title>
<style>
@page {{ margin: 1.8cm; }}
body {{ font-family: 'Helvetica', 'Arial', sans-serif; color: #1a1a1a; font-size: 10pt; line-height: 1.5; }}
.header {{ text-align: center; margin-bottom: 25px; border-bottom: 3px solid #1b5e20; padding-bottom: 15px; }}
.header h1 {{ font-size: 24pt; letter-spacing: 4px; margin: 0; color: #1b5e20; }}
.header h2 {{ font-size: 9pt; color: #666; font-weight: normal; margin: 5px 0 0; }}
.section {{ margin: 15px 0; }}
.section h3 {{ font-size: 9pt; text-transform: uppercase; color: #1b5e20; border-bottom: 1px solid #ccc; padding-bottom: 4px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9pt; margin: 8px 0; }}
th {{ background: #1b5e20; color: #fff; padding: 5px; text-align: left; font-size: 7.5pt; text-transform: uppercase; }}
td {{ padding: 4px 5px; border-bottom: 1px solid #ddd; }}
.total-row td {{ border-top: 2px solid #000; font-weight: bold; }}
.resumen {{ background: #f4f1ea; padding: 12px; margin: 10px 0; }}
.resumen div {{ display: flex; justify-content: space-between; padding: 3px 0; }}
.footer {{ margin-top: 30px; font-size: 7.5pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }}
</style></head><body>
<div class='header'>
<h1>SOMA</h1>
<h2>CIERRE DE PROYECTO</h2>
</div>
<div class='section'>
<h3>Datos del Proyecto</h3>
<table>
<tr><td style='width:140px;font-weight:600;'>Cliente</td><td>{nombre_cliente}</td></tr>
<tr><td style='font-weight:600;'>Contacto</td><td>{contacto}</td></tr>
<tr><td style='font-weight:600;'>Proyecto</td><td>{nombre_proyecto}</td></tr>
<tr><td style='font-weight:600;'>Tipo</td><td>{tipo_proyecto}</td></tr>
<tr><td style='font-weight:600;'>Ubicación</td><td>{ubic_str}</td></tr>
<tr><td style='font-weight:600;'>ID</td><td>{temp_id}</td></tr>
<tr><td style='font-weight:600;'>Inmersión (cliente)</td><td>{nivel_orig.upper()} · {m2_orig:.0f} m² · ${honorarios_orig:,.2f}</td></tr>
<tr><td style='font-weight:600;'>Programa (definitivo)</td><td>{nivel.upper()} · {m2_lead:.0f} m² · ${honorarios:,.2f}</td></tr>
<tr><td style='font-weight:600;'>Fecha de cierre</td><td>{fecha}</td></tr>
</table>
</div>
<div class='section'>
<h3>Programa Arquitectónico</h3>
<table>
<tr><th>Tipo</th><th>Espacio</th><th style='text-align:right'>m²</th><th style='text-align:center'>Clave</th></tr>
{filas_prog}
</table>
</div>
<div class='section'>
<h3>Análisis Multidimensional</h3>
<pre style="font-family:'Courier New',monospace;font-size:7.5pt;line-height:1.4;background:#f9f9f9;padding:10px;border:1px solid #ddd;white-space:pre-wrap;">{lead['analisis_procesado'] or 'Sin análisis disponible.'}</pre>
</div>
<div class='section'>
<h3>Respuestas de Inmersión</h3>
                <div style="font-family:'Courier New',monospace;font-size:8pt;line-height:1.6;background:#f9f9f9;padding:10px;border:1px solid #ddd;">{respuestas_lines2 or 'Sin respuestas.'}</div>
</div>
<div class='section'>
<h3>Resumen Financiero</h3>
<div class='resumen'>
<div><span>Honorarios de Diseño</span><span><strong>${honorarios:,.2f}</strong></span></div>
<div><span>Total Pagado</span><span style='color:#2e7d32;'><strong>${total_pagado:,.2f}</strong></span></div>
<div><span>Total Pendiente</span><span style='color:#c62828;'><strong>${total_pendiente:,.2f}</strong></span></div>
</div>
<h3 style='margin-top:12px;'>Detalle de Cobros</h3>
<table>
<tr><th>Concepto</th><th style='text-align:right'>Monto</th><th style='text-align:center'>Estado</th><th style='text-align:center'>Fecha Pago</th></tr>
{filas_cobros}
</table>
</div>
<div class='footer'>
<p>SOMA Taller Virtual de Arquitectura — {fecha}</p>
<p>info@soma-arquitectura.com</p>
</div>
</body></html>"""
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/lead/<int:lead_id>/expediente-pdf', methods=['GET'])
def expediente_pdf(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT * FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Proyecto no encontrado", 404
        prog_rows = fetchall(conn, "SELECT espacio, area, tipo, clave FROM programa_arquitectonico WHERE lead_id=? ORDER BY id", (lead_id,))
        conn.close()

        nombre_cliente = lead["nombre_proyecto"] or lead["nombre_cliente"] or lead["contacto"] or "—"
        temp_id = lead["temp_id"] or "—"
        nivel = lead["nivel_proyecto"] or "—"
        m2_lead = lead["m2"] or 0
        honorarios = lead["honorarios_diseno"] or 0
        nivel_orig = lead["nivel_original"] or "—"
        m2_orig = lead["m2_original"] or 0
        honorarios_orig = lead["honorarios_original"] or 0
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")
        parts = [lead.get("calle_numero","") or "", lead.get("colonia","") or "",
                 lead.get("ciudad","") or "", lead.get("estado_ubic","") or ""]
        ubic_str = ", ".join(p for p in parts if p)

        respuestas_lines = ""
        try:
            raw = json.loads(lead["respuestas_json"] or "{}")
            for k, v in raw.items():
                num = k.replace("step","").replace("Pregunta ","")
                if isinstance(v, dict):
                    r = (v.get("r") or v.get("selected") or "")
                    lbl = (v.get("label") or "")
                    respuestas_lines += f"<div>Pregunta {num}: {r.upper() if r else '?'}. {lbl}</div>"
                elif isinstance(v, str) and v.strip():
                    info = INMERSION_PREGUNTAS.get(k)
                    if info:
                        opt = info.get(v.strip().upper(), "")
                        respuestas_lines += f"<div>Pregunta {num}: {v.strip().upper()}. {opt}</div>"
                    else:
                        respuestas_lines += f"<div>Pregunta {num}: {v.strip().upper()}</div>"
        except:
            pass

        filas_prog = "".join(
            f"<tr><td>{r['tipo'] or '—'}</td><td>{r['espacio'] or '—'}</td>"
            f"<td style='text-align:right'>{r['area'] or 0:.1f}</td><td style='text-align:center'>{r['clave'] or '—'}</td></tr>"
            for r in prog_rows
        )

        html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'>
<title>EXPEDIENTE — {nombre_cliente}</title>
<style>
@page {{ margin: 1.8cm; }}
body {{ font-family: 'Helvetica', 'Arial', sans-serif; color: #1a1a1a; font-size: 10pt; line-height: 1.5; }}
.header {{ text-align: center; margin-bottom: 25px; border-bottom: 3px solid #a6937c; padding-bottom: 15px; }}
.header h1 {{ font-size: 24pt; letter-spacing: 4px; margin: 0; color: #a6937c; }}
.header h2 {{ font-size: 9pt; color: #666; font-weight: normal; margin: 5px 0 0; }}
.section {{ margin: 15px 0; }}
.section h3 {{ font-size: 9pt; text-transform: uppercase; color: #a6937c; border-bottom: 1px solid #ccc; padding-bottom: 4px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 9pt; margin: 8px 0; }}
th {{ background: #a6937c; color: #fff; padding: 5px; text-align: left; font-size: 7.5pt; text-transform: uppercase; }}
td {{ padding: 4px 5px; border-bottom: 1px solid #ddd; }}
.resumen {{ background: #f9f9f9; padding: 12px; margin: 10px 0; display: grid; grid-template-columns: repeat(3,1fr); gap: 10px; }}
.resumen .item {{ text-align: center; }}
.resumen .item .val {{ font-size: 16pt; font-weight: bold; color: #a6937c; }}
.resumen .item .lbl {{ font-size: 7pt; text-transform: uppercase; color: #999; }}
.footer {{ margin-top: 30px; font-size: 7.5pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 10px; }}
</style></head><body>
<div class='header'>
<h1>SOMA</h1>
<h2>EXPEDIENTE TÉCNICO</h2>
</div>
<div class='section'>
<h3>Datos del Proyecto</h3>
<table>
<tr><td style='width:140px;font-weight:600;'>Cliente</td><td>{nombre_cliente}</td></tr>
<tr><td style='font-weight:600;'>ID</td><td>{temp_id}</td></tr>
<tr><td style='font-weight:600;'>Contacto</td><td>{lead["contacto"] or "—"}</td></tr>
<tr><td style='font-weight:600;'>Inmersión (cliente)</td><td>{nivel_orig.upper()} · {m2_orig:.0f} m² · ${honorarios_orig:,.2f}</td></tr>
<tr><td style='font-weight:600;'>Programa (definitivo)</td><td>{nivel.upper()} · {m2_lead:.0f} m² · ${honorarios:,.2f}</td></tr>
<tr><td style='font-weight:600;'>Ubicación</td><td>{ubic_str}</td></tr>
</table>
</div>
<div class='section'>
<h3>Análisis Multidimensional</h3>
<pre style="font-family:'Courier New',monospace;font-size:7.5pt;line-height:1.4;background:#f9f9f9;padding:10px;border:1px solid #ddd;white-space:pre-wrap;">{lead['analisis_procesado'] or 'Sin análisis disponible.'}</pre>
</div>
<div class='section'>
<h3>Respuestas de Inmersión</h3>
<div style="font-family:'Courier New',monospace;font-size:8pt;line-height:1.6;background:#f9f9f9;padding:10px;border:1px solid #ddd;">{respuestas_lines or 'Sin respuestas.'}</div>
</div>
{f"""
<div class='section'>
<h3>Programa Arquitectónico</h3>
<table>
<tr><th>Tipo</th><th>Espacio</th><th style='text-align:right'>m²</th><th style='text-align:center'>Clave</th></tr>
{filas_prog}
</table>
</div>""" if prog_rows else ""}
<div class='footer'>
<p>SOMA Taller Virtual de Arquitectura — {fecha}</p>
<p>info@soma-arquitectura.com</p>
</div>
</body></html>"""
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500

MESES = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

@app.route('/metrics/bloque01', methods=['GET'])
def metrics_bloque01():
    try:
        now = datetime.datetime.now()
        year = request.args.get('year', str(now.year))
        month = request.args.get('month', '')
        year = int(year)
        
        if month:
            start_date = f"{year}-{int(month):02d}-01"
            end_date = f"{year}-{int(month)+1:02d}-01" if int(month) < 12 else f"{year+1}-01-01"
        else:
            start_date = f"{year}-01-01"
            end_date = f"{year+1}-01-01"
        
        conn = get_connection()
        
        # Solo clientes ACTIVOS (excluye terminados)
        leads = fetchall(conn, "SELECT id, pipeline_estado, honorarios_diseno FROM captura_web WHERE pipeline_estado IN ('contratado', 'primera_entrega', 'entrega_final')")
        total_clientes = len(leads)
        total_honorarios = sum(dictify(r)['honorarios_diseno'] or 0 for r in leads)
        
        # Cobros pagados en el periodo
        date_params = [start_date, end_date]
        cobros_pagados = fetchall(conn, f"SELECT concepto, monto FROM cobros WHERE estado = 'pagado' AND fecha_pago >= ? AND fecha_pago < ?", date_params)
        
        anticipos = 0.0
        primera_entrega = 0.0
        pagos_finales = 0.0
        ingresos_periodo = 0.0
        for r in cobros_pagados:
            row = dictify(r)
            monto = row['monto'] or 0
            ingresos_periodo += monto
            concepto_lower = (row['concepto'] or '').lower()
            if '30%' in row['concepto'] and 'anticipo' in concepto_lower:
                anticipos += monto
            elif '40%' in row['concepto'] and 'segundo' in concepto_lower:
                primera_entrega += monto
            elif '30%' in row['concepto'] and 'tercer' in concepto_lower:
                pagos_finales += monto
        
        # Egresos en el periodo
        gastos = fetchall(conn, "SELECT monto FROM egresos WHERE fecha >= ? AND fecha < ?", date_params)
        gasto_operacion = sum(dictify(r)['monto'] or 0 for r in gastos)
        
        # Fondo acumulado
        fondos = fetchall(conn, "SELECT balance_actual FROM fondos")
        fondo_acumulado = sum(dictify(r)['balance_actual'] or 0 for r in fondos)
        
        conn.close()
        
        periodo_label = f"{MESES[int(month)-1]} {year}" if month else str(year)
        
        return jsonify({
            "total_clientes": total_clientes,
            "anticipos": round(anticipos, 2),
            "primera_entrega": round(primera_entrega, 2),
            "pagos_finales": round(pagos_finales, 2),
            "ingresos_periodo": round(ingresos_periodo, 2),
            "gasto_operacion": round(gasto_operacion, 2),
            "fondo_acumulado": round(fondo_acumulado, 2),
            "total_honorarios": round(total_honorarios, 2),
            "periodo": periodo_label,
            "year": year,
            "month": month or None
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_leads', methods=['GET'])
def get_leads():
    try:
        conn = get_connection()
        rows = fetchall(conn, "SELECT * FROM captura_web ORDER BY fecha DESC")
        conn.close()
        return jsonify([dictify(row) for row in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

PIPELINE_ESTADOS = ['lead', 'entrevistado', 'programado', 'cotizado', 'contratado', 'primera_entrega', 'entrega_final', 'terminado']

@app.route('/leads/kanban', methods=['GET'])
def get_leads_kanban():
    try:
        conn = get_connection()
        leads_raw = fetchall(conn, "SELECT * FROM captura_web ORDER BY fecha DESC")
        leads = [dictify(row) for row in leads_raw]
        conn.close()
        grouped = {e: [] for e in PIPELINE_ESTADOS}
        for l in leads:
            st = l.get('pipeline_estado', 'lead') or 'lead'
            if st not in grouped:
                st = 'lead'
            grouped[st].append(l)
        return jsonify({"grouped": grouped, "estados": PIPELINE_ESTADOS}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>/estado-contacto', methods=['PATCH'])
def update_estado_contacto(lead_id):
    try:
        data = request.json
        nuevo = data.get('estado_contacto', '').strip()
        if nuevo not in ('no programado', 'programado', 'no localizado'):
            return jsonify({"status": "error", "message": f"Estado inválido: {nuevo}"}), 400
        conn = get_connection()
        execute(conn, "UPDATE captura_web SET estado_contacto = ? WHERE id = ?", (nuevo, lead_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "estado_contacto": nuevo}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>/contratar', methods=['POST'])
def contratar_lead(lead_id):
    try:
        conn = get_connection()
        execute(conn, "UPDATE captura_web SET pipeline_estado='contratado' WHERE id=?", (lead_id,))
        # Generar esquema de pagos 30/40/30 automático
        lead = fetchone(conn, "SELECT m2, nivel_proyecto, honorarios_diseno FROM captura_web WHERE id=?", (lead_id,))
        if lead:
            m2 = lead["m2"] or 0
            nivel = lead["nivel_proyecto"] or "esencial"
            honorarios = lead["honorarios_diseno"] or max(m2 * PRECIOS_M2.get(nivel, 250), MINIMO_TALLER)
            if honorarios > 0:
                esquema = [
                    ("Anticipo 30%", honorarios * 0.3),
                    ("Segundo pago 40%", honorarios * 0.4),
                    ("Tercer pago 30%", honorarios * 0.3),
                ]
                for concepto, monto in esquema:
                    execute(conn, "INSERT INTO cobros (proyecto_id, concepto, monto, estado) VALUES (?, ?, ?, ?)",
                            (lead_id, concepto, round(monto, 2), "pendiente"))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "pipeline_estado": "contratado"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>/recibo-anticipo', methods=['GET'])
def recibo_anticipo(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT * FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Lead no encontrado", 404
        html = _recibo_pago_html(lead, 0.3, "ANTICIPO", conn)
        conn.close()
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500

def _recibo_pago_html(lead, pct, label, conn):
    nombre = lead["nombre_cliente"] or lead["contacto"] or "—"
    proyecto = lead["nombre_proyecto"] or "—"
    temp_id = lead["temp_id"] or "—"
    nivel = lead["nivel_proyecto"] or "esencial"
    m2_lead = lead["m2"] or 0
    precio_m2 = PRECIOS_M2.get(nivel, 250)
    espacios_rows = fetchall(conn, "SELECT area FROM programa_arquitectonico WHERE lead_id=?", (lead["id"],))
    if espacios_rows:
        total_m2_prog = sum(r["area"] for r in espacios_rows)
        honorarios = max(total_m2_prog * precio_m2, MINIMO_TALLER)
    elif lead["honorarios_diseno"] and lead["honorarios_diseno"] > 0:
        honorarios = lead["honorarios_diseno"]
    else:
        honorarios = max(m2_lead * precio_m2, MINIMO_TALLER)
    monto_pago = honorarios * pct
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    folio = f"REC-{temp_id}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    return f"""<!DOCTYPE html><html><head><meta charset='utf-8'>
<title>RECIBO DE {label} — {nombre}</title>
<style>
@page {{ margin: 1.5cm; }}
body {{ font-family: 'Helvetica', 'Arial', sans-serif; color: #1a1a1a; font-size: 10pt; line-height: 1.5; }}
.header {{ text-align: center; margin-bottom: 30px; border-bottom: 3px double #000; padding-bottom: 15px; }}
.header h1 {{ font-size: 26pt; letter-spacing: 4px; margin: 0; }}
.header h2 {{ font-size: 9pt; color: #a6937c; font-weight: normal; margin: 3px 0 0; }}
.header .folio {{ font-family: monospace; font-size: 7.5pt; color: #999; margin-top: 5px; }}
.info {{ margin: 20px 0; }}
.info table {{ width: 100%; font-size: 9pt; }}
.info td {{ padding: 3px 5px; }}
.info .label {{ font-weight: 600; width: 130px; color: #555; }}
.monto-box {{ border: 2px solid #000; padding: 20px; text-align: center; margin: 25px 0; }}
.monto-box .cantidad {{ font-size: 28pt; font-weight: bold; letter-spacing: 2px; }}
.monto-box .concepto {{ font-size: 9pt; color: #666; margin-top: 5px; }}
.monto-box .letra {{ font-size: 8pt; color: #888; margin-top: 8px; }}
.detalle {{ margin: 20px 0; font-size: 8.5pt; }}
.detalle table {{ width: 100%; border-collapse: collapse; }}
.detalle td {{ padding: 4px 5px; border-bottom: 1px solid #eee; }}
.detalle .total-row td {{ border-top: 2px solid #000; font-weight: bold; }}
.firma {{ margin-top: 35px; text-align: center; }}
.firma .line {{ width: 250px; border-top: 1px solid #000; margin: 25px auto 5px; }}
.firma p {{ font-size: 8pt; color: #666; margin: 0; }}
.footer {{ margin-top: 30px; font-size: 7pt; color: #999; text-align: center; border-top: 1px solid #ddd; padding-top: 8px; }}
</style></head><body>
<div class='header'>
<h1>SOMA</h1>
<h2>RECIBO DE {label}</h2>
<div class='folio'>Folio: {folio}</div>
</div>
<div class='info'>
<table>
<tr><td class='label'>Cliente</td><td>{nombre}</td></tr>
<tr><td class='label'>Proyecto</td><td>{proyecto}</td></tr>
<tr><td class='label'>ID Proyecto</td><td>{temp_id}</td></tr>
<tr><td class='label'>Paquete</td><td>{nivel.upper()} · {m2_lead:.0f} m²</td></tr>
<tr><td class='label'>Fecha de emisión</td><td>{fecha}</td></tr>
</table>
</div>
<div class='monto-box'>
<div class='cantidad'>${monto_pago:,.2f}</div>
<div class='concepto'>{label.upper()} — {int(pct*100)}% DE HONORARIOS DE DISEÑO</div>
<div class='letra'>Son: {num_to_words(monto_pago)} MXN</div>
</div>
<div class='detalle'>
<table>
<tr><td style='font-weight:600;'>Concepto</td><td style='text-align:right;font-weight:600;'>Monto</td></tr>
<tr><td>Honorarios de Diseño ({nivel.capitalize()})</td><td style='text-align:right;'>${honorarios:,.2f}</td></tr>
<tr><td>{label} ({int(pct*100)}%)</td><td style='text-align:right;font-weight:600;color:#2e7d32;'>${monto_pago:,.2f}</td></tr>
<tr><td>Saldo pendiente por cubrir ({int((1-pct)*100)}%)</td><td style='text-align:right;'>${honorarios * (1-pct):,.2f}</td></tr>
</table>
</div>
<div class='firma'>
<div class='line'></div>
<p>Recibí conforme</p>
<p style='margin-top:2px;font-size:7pt;'>SOMA Taller Virtual de Arquitectura</p>
</div>
<div class='footer'>
<p>info@soma-arquitectura.com — {fecha}</p>
<p style='margin-top:4px;font-size:6.5pt;color:#bbb;'>Este recibo no sustituye una factura fiscal. Generado automáticamente por el sistema SOMA.</p>
</div>
</body></html>"""


@app.route('/lead/<int:lead_id>/recibo-segundo-pago', methods=['GET'])
def recibo_segundo_pago(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT * FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Lead no encontrado", 404
        html = _recibo_pago_html(lead, 0.4, "SEGUNDO PAGO", conn)
        conn.close()
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500


@app.route('/lead/<int:lead_id>/recibo-tercer-pago', methods=['GET'])
def recibo_tercer_pago(lead_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, "SELECT * FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Lead no encontrado", 404
        html = _recibo_pago_html(lead, 0.3, "TERCER PAGO", conn)
        conn.close()
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return f"Error: {e}", 500


@app.route('/lead/<int:lead_id>/datos-proyecto', methods=['PATCH'])
def update_datos_proyecto(lead_id):
    try:
        data = request.json
        nombre_cliente = (data.get('nombre_cliente') or '').strip()
        nombre_proyecto = (data.get('nombre_proyecto') or '').strip()
        tipo_proyecto = (data.get('tipo_proyecto') or '').strip()
        nivel_proyecto = (data.get('nivel_proyecto') or '').strip()
        m2 = data.get('m2')
        honorarios = data.get('honorarios_diseno')
        calle_numero = (data.get('calle_numero') or '').strip()
        colonia = (data.get('colonia') or '').strip()
        ciudad = (data.get('ciudad') or '').strip()
        estado_ubic = (data.get('estado_ubic') or data.get('estado') or '').strip()
        # Rebuild ubicacion JSON from individual fields for backward compat
        ubicacion_obj = {"calle_numero": calle_numero, "colonia": colonia, "ciudad": ciudad, "estado": estado_ubic}
        ubicacion_json = json.dumps(ubicacion_obj)

        PRECIOS = {'esencial': 250, 'integral': 350, 'ejecutivo': 850}
        precio_m2 = PRECIOS.get(nivel_proyecto, 250)
        if m2 is not None and nivel_proyecto:
            m2 = float(m2)
            honorarios_calc = max(m2 * precio_m2, 6500)
        else:
            honorarios_calc = None
        
        conn = get_connection()
        base_sql = " UPDATE captura_web SET nombre_cliente=?, nombre_proyecto=?, tipo_proyecto=?, nivel_proyecto=?, m2=?, honorarios_diseno=?, ubicacion=?, calle_numero=?, colonia=?, ciudad=?, estado_ubic=? WHERE id=?"
        params = [nombre_cliente, nombre_proyecto, tipo_proyecto, nivel_proyecto, m2, honorarios_calc, ubicacion_json, calle_numero, colonia, ciudad, estado_ubic, lead_id]
        execute(conn, base_sql, params)
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>/regresar', methods=['POST'])
def regresar_lead(lead_id):
    try:
        conn = get_connection()
        execute(conn, "DELETE FROM cobros WHERE proyecto_id = ?", (lead_id,))
        execute(conn, "UPDATE captura_web SET pipeline_estado = 'lead' WHERE id = ?", (lead_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "pipeline_estado": "lead"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>/pipeline', methods=['PATCH'])
def update_pipeline(lead_id):
    try:
        data = request.json
        nuevo_estado = data.get('pipeline_estado', '').strip().lower()
        if nuevo_estado not in PIPELINE_ESTADOS:
            return jsonify({"status": "error", "message": f"Estado inválido: {nuevo_estado}"}), 400
        conn = get_connection()
        execute(conn, "UPDATE captura_web SET pipeline_estado = ? WHERE id = ?", (nuevo_estado, lead_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "pipeline_estado": nuevo_estado}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/lead/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    try:
        conn = get_connection()
        execute(conn, "DELETE FROM cobros WHERE proyecto_id = ?", (lead_id,))
        execute(conn, "DELETE FROM matriz_inversion WHERE proyecto_id = ?", (lead_id,))
        execute(conn, "DELETE FROM algoritmo_progreso WHERE proyecto_id = ?", (lead_id,))
        execute(conn, "DELETE FROM programa_arquitectonico WHERE lead_id = ?", (lead_id,))
        execute(conn, "DELETE FROM captura_web WHERE id = ?", (lead_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/egresos', methods=['GET', 'POST'])
def egresos():
    try:
        conn = get_connection()
        if request.method == 'POST':
            data = request.json
            execute(conn, "INSERT INTO egresos (categoria, concepto, monto, fecha) VALUES (?, ?, ?, ?)",
                    (data['categoria'], data['concepto'], data['monto'], data.get('fecha', '')))
            conn.commit()
            conn.close()
            return jsonify({"status": "success"}), 201
        rows = fetchall(conn, "SELECT * FROM egresos ORDER BY fecha DESC, id DESC")
        conn.close()
        result = []
        for r in rows:
            item = dictify(r)
            fecha = item.get('fecha')
            if hasattr(fecha, 'strftime'):
                item['fecha'] = fecha.strftime('%Y-%m-%d')
            result.append(item)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/egresos/<int:egreso_id>', methods=['DELETE'])
def eliminar_egreso(egreso_id):
    try:
        conn = get_connection()
        execute(conn, "DELETE FROM egresos WHERE id = ?", (egreso_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cobros/<int:proyecto_id>', methods=['GET', 'DELETE'])
def get_cobros(proyecto_id):
    try:
        conn = get_connection()
        if request.method == 'DELETE':
            execute(conn, "DELETE FROM cobros WHERE proyecto_id = ?", (proyecto_id,))
            conn.commit()
            conn.close()
            return jsonify({"status": "success"}), 200
        rows = fetchall(conn, "SELECT * FROM cobros WHERE proyecto_id = ? ORDER BY fecha_vencimiento ASC", (proyecto_id,))
        conn.close()
        return jsonify([dictify(row) for row in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cobros', methods=['POST'])
def crear_cobro():
    try:
        data = request.json
        conn = get_connection()
        cur = execute(conn, """INSERT INTO cobros (proyecto_id, concepto, monto, fecha_vencimiento, estado, notas)
                     VALUES (?, ?, ?, ?, ?, ?)""",
                  (data['proyecto_id'], data['concepto'], data['monto'],
                   data.get('fecha_vencimiento', ''), data.get('estado', 'pendiente'), data.get('notas', '')))
        conn.commit()
        cobro_id = get_lastrowid(cur)
        conn.close()
        return jsonify({"status": "success", "id": cobro_id}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cobros/generar_esquema/<int:proyecto_id>', methods=['POST'])
def generar_esquema_pagos(proyecto_id):
    try:
        conn = get_connection()
        proy = fetchone(conn, "SELECT id, honorarios_diseno, temp_id FROM captura_web WHERE id = ?", (proyecto_id,))
        if not proy:
            conn.close()
            return jsonify({"status": "error", "message": "Proyecto no encontrado"}), 404

        total = proy["honorarios_diseno"] or 0
        if total <= 0:
            conn.close()
            return jsonify({"status": "error", "message": "El proyecto no tiene honorarios calculados"}), 400

        execute(conn, "DELETE FROM cobros WHERE proyecto_id = ? AND estado = 'pendiente'", (proyecto_id,))

        esquema = [
            ("Anticipo (30%) — Firma de contrato", round(total * 0.3, 2)),
            ("Segundo pago (40%) — Entrega de anteproyecto", round(total * 0.4, 2)),
            ("Tercer pago (30%) — Entrega final", round(total * 0.3, 2)),
        ]

        creados = []
        for concepto, monto in esquema:
            cur = execute(conn, """INSERT INTO cobros (proyecto_id, concepto, monto, estado, notas)
                         VALUES (?, ?, ?, 'pendiente', ?)""",
                      (proyecto_id, concepto, monto, f"Lead: {proy['temp_id']}"))
            creados.append(get_lastrowid(cur))

        conn.commit()
        conn.close()
        return jsonify({"status": "success", "cobros_ids": creados, "total": total}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/cobros/<int:cobro_id>/pagar', methods=['PATCH'])
def pagar_cobro(cobro_id):
    try:
        data = request.json
        conn = get_connection()
        execute(conn, """UPDATE cobros SET estado = 'pagado', fecha_pago = ?, metodo_pago = ?
                     WHERE id = ?""",
                  (data.get('fecha_pago', datetime.datetime.now().isoformat()),
                   data.get('metodo_pago', ''), cobro_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/resumen_financiero', methods=['GET'])
def resumen_financiero():
    try:
        conn = get_connection()
        rows = fetchall(conn, """SELECT c.id, c.temp_id, c.contacto, c.m2, c.nivel_proyecto, c.honorarios_diseno,
                            IFNULL(SUM(CASE WHEN cb.estado = 'pagado' THEN cb.monto ELSE 0 END), 0) as pagado,
                            IFNULL(SUM(CASE WHEN cb.estado = 'pendiente' THEN cb.monto ELSE 0 END), 0) as pendiente
                     FROM captura_web c
                     LEFT JOIN cobros cb ON cb.proyecto_id = c.id
                     GROUP BY c.id
                     ORDER BY c.fecha DESC""")
        conn.close()
        total_pagado = sum(r["pagado"] or 0 for r in rows)
        total_pendiente = sum(r["pendiente"] or 0 for r in rows)
        return jsonify({
            "proyectos": [{
                "id": r["id"], "temp_id": r["temp_id"], "contacto": r["contacto"],
                "m2": r["m2"], "nivel": r["nivel_proyecto"], "honorarios": r["honorarios_diseno"],
                "pagado": r["pagado"] or 0, "pendiente": r["pendiente"] or 0
            } for r in rows],
            "total_pagado": total_pagado,
            "total_pendiente": total_pendiente
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/tarjeta')
def tarjeta_redirect():
    return redirect('/', 302)

@app.route('/')
def index():
    web_path = os.path.join(PROYECTO_DIR, "web", "Pagina Web 6.html")
    if os.path.exists(web_path):
        with open(web_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Pagina no encontrada", 404

@app.route('/dashboard')
def serve_dashboard():
    dashboard_path = os.path.join(PROYECTO_DIR, "web", "dashboard.html")
    if os.path.exists(dashboard_path):
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Dashboard no encontrado", 404

@app.route('/web/<path:filename>')
def serve_web_static(filename):
    web_dir = os.path.join(PROYECTO_DIR, "web")
    filepath = os.path.join(web_dir, filename)
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return send_from_directory(web_dir, filename)
    return "Not found", 404

@app.route('/css/<path:filename>')
def serve_css(filename):
    css_path = os.path.join(PROYECTO_DIR, "metodologia", "Bloque 01 - GESTIÓN DE PROYECTOS", "dashboard", "css", filename)
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/css; charset=utf-8'}
    return "Not found", 404

# Servir recursos estáticos (imágenes, videos, etc.)
@app.route('/recursos_graficos/<path:filename>')
def serve_recursos(filename):
    recursos_dir = os.path.join(PROYECTO_DIR, "recursos_graficos")
    filepath = os.path.join(recursos_dir, filename)
    if not os.path.exists(filepath):
        return "Not found", 404

    ext = os.path.splitext(filename)[1].lower()
    if ext == '.mp4':
        size = os.path.getsize(filepath)
        range_header = request.headers.get('Range')
        if range_header:
            match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else size - 1
                length = end - start + 1
                with open(filepath, 'rb') as f:
                    f.seek(start)
                    data = f.read(length)
                response = Response(data, 206, mimetype='video/mp4',
                    content_type='video/mp4',
                    direct_passthrough=True)
                response.headers.add('Content-Range', f'bytes {start}-{end}/{size}')
                response.headers.add('Accept-Ranges', 'bytes')
                response.headers.add('Content-Length', str(length))
                response.cache_control.max_age = 86400
                response.cache_control.public = True
                return response
        response = send_file(filepath, mimetype='video/mp4')
        response.headers.add('Accept-Ranges', 'bytes')
        response.cache_control.max_age = 86400
        response.cache_control.public = True
        return response

    response = send_from_directory(recursos_dir, filename)
    response.cache_control.max_age = 86400
    response.cache_control.public = True
    return response

@app.route('/backend/<path:filename>')
def serve_backend_static(filename):
    response = send_from_directory(BASE_DIR, filename)
    response.cache_control.max_age = 3600
    response.cache_control.public = True
    return response

@app.route('/algoritmo')
def serve_algoritmo():
    algo_path = os.path.join(PROYECTO_DIR, "web", "algoritmo_soma.html")
    if os.path.exists(algo_path):
        with open(algo_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Not found", 404

# ---- ALGORITMO SOMA (Progreso + Datos por proyecto) ----

@app.route('/api/algoritmo/progreso/<int:proyecto_id>', methods=['GET', 'PUT'])
def algoritmo_progreso(proyecto_id):
    try:
        conn = get_connection()
        if request.method == 'PUT':
            data = request.json
            seccion = data.get('seccion')
            paso = data.get('paso')
            estado = data.get('estado', 'PENDIENTE')
            ahora = datetime.datetime.now().isoformat()

            existing = fetchone(conn, """SELECT id FROM algoritmo_progreso
                WHERE proyecto_id=? AND seccion=? AND paso=?""",
                (proyecto_id, seccion, paso))
            if existing:
                execute(conn, """UPDATE algoritmo_progreso
                    SET estado=?, updated_at=? WHERE id=?""",
                    (estado, ahora, existing['id']))
            else:
                execute(conn, """INSERT INTO algoritmo_progreso
                    (proyecto_id, seccion, paso, estado, updated_at)
                    VALUES (?, ?, ?, ?, ?)""",
                    (proyecto_id, seccion, paso, estado, ahora))
            conn.commit()
            conn.close()
            return jsonify({"status": "success"}), 200

        rows = fetchall(conn, """SELECT seccion, paso, estado FROM algoritmo_progreso
            WHERE proyecto_id=? ORDER BY seccion, paso""", (proyecto_id,))
        conn.close()
        progreso = {}
        for r in rows:
            key = f"{r['seccion']}_{r['paso']}"
            progreso[key] = r['estado']
        return jsonify({"status": "success", "progreso": progreso}), 200
    except Exception as e:
        try: conn.close()
        except: pass
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/algoritmo/datos/<int:proyecto_id>', methods=['GET'])
def algoritmo_datos(proyecto_id):
    try:
        conn = get_connection()
        lead = fetchone(conn, """SELECT * FROM captura_web WHERE id=?""", (proyecto_id,))
        if not lead:
            conn.close()
            return jsonify({"status": "error", "message": "Proyecto no encontrado"}), 404

        espacios = fetchall(conn, """SELECT * FROM programa_arquitectonico
            WHERE lead_id=? ORDER BY tipo, id""", (proyecto_id,))
        cobros_data = fetchall(conn, """SELECT * FROM cobros
            WHERE proyecto_id=? ORDER BY id""", (proyecto_id,))

        conn.close()

        lead_dict = dictify(lead)
        if lead_dict and lead_dict.get('respuestas_json'):
            try:
                lead_dict['respuestas_json'] = json.loads(lead_dict['respuestas_json'])
            except: pass
        if lead_dict and lead_dict.get('analisis_procesado'):
            try:
                lead_dict['analisis_procesado'] = json.loads(lead_dict['analisis_procesado'])
            except: pass

        return jsonify({
            "status": "success",
            "lead": lead_dict,
            "programa": [dictify(e) for e in espacios],
            "cobros": [dictify(c) for c in cobros_data]
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/diagrama/proyectos', methods=['GET'])
def diagrama_proyectos():
    try:
        conn = get_connection()
        rows = fetchall(conn, """
            SELECT DISTINCT cw.id, cw.temp_id, cw.contacto, cw.fecha
            FROM captura_web cw
            INNER JOIN programa_arquitectonico pa ON pa.lead_id = cw.id
            ORDER BY cw.fecha DESC
        """)
        conn.close()
        proyectos = []
        for r in rows:
            proyectos.append({
                "id": r["id"],
                "nombre": r["temp_id"],
                "cliente": r["contacto"],
                "fecha": r["fecha"][:10] if r["fecha"] else ""
            })
        return jsonify(proyectos), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/diagrama/grafo/<int:lead_id>', methods=['GET'])
def diagrama_grafo(lead_id):
    try:
        zona_filtro = request.args.get('zona', type=int)
        conn = get_connection()

        if zona_filtro:
            espacios = fetchall(conn, """
                SELECT * FROM programa_arquitectonico
                WHERE lead_id = ? AND zona = ?
                ORDER BY id
            """, (lead_id, zona_filtro))
        else:
            espacios = fetchall(conn, """
                SELECT * FROM programa_arquitectonico
                WHERE lead_id = ?
                ORDER BY id
            """, (lead_id,))

        conn.close()

        if not espacios:
            return jsonify({"status": "empty", "nodes": [], "edges": []}), 200

        claves_validas = set()
        for e in espacios:
            if e["clave"]:
                claves_validas.add(e["clave"])

        areas = [e["area"] or 30 for e in espacios if e["clave"]]
        area_min = min(areas) if areas else 30
        area_max = max(areas) if areas else 30
        rango = max(area_max - area_min, 1)

        ZONA_COLOR_HEX = {
            1: "#4d7ae6", 2: "#e6cc33", 3: "#e64d4d",
            4: "#e68033", 5: "#9933cc"
        }

        nodes = []
        edges_set = set()
        id_map = {}

        for i, e in enumerate(espacios):
            if not e["clave"]:
                continue
            area_val = float(e["area"]) if e["area"] and e["area"] > 0 else 30
            proporcion = (area_val - area_min) / rango if rango > 0 else 0.5
            size = 20 + (proporcion * 40)
            zona = int(e["zona"]) if e["zona"] else 1
            color = ZONA_COLOR_HEX.get(zona, "#666666")

            label = f"{e['clave']}\n{e['espacio'] or '?'}"

            nodes.append({
                "id": e["clave"],
                "label": label,
                "size": size,
                "color": color,
                "zona": zona,
                "area": round(area_val, 1),
                "tipo": e["tipo"] or "",
                "espacio": e["espacio"] or ""
            })
            id_map[e["clave"]] = e

        for e in espacios:
            if not e["clave"] or not e["relacion_directa"]:
                continue
            try:
                relaciones = json.loads(e["relacion_directa"])
                for rel in relaciones:
                    if rel and rel != e["clave"] and rel in claves_validas:
                        edge_key = tuple(sorted([e["clave"], rel]))
                        if edge_key not in edges_set:
                            edges_set.add(edge_key)
            except:
                pass

        edges = [{"from": u, "to": v} for u, v in edges_set]

        return jsonify({"status": "success", "nodes": nodes, "edges": edges}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/fondo_democratizacion', methods=['GET'])
def fondo_democratizacion():
    try:
        conn = get_connection()
        rows = fetchall(conn, "SELECT m2, nivel_proyecto FROM captura_web WHERE nivel_proyecto IS NOT NULL")
        conn.close()
        total_fondo = 0
        for r in rows:
            m2 = r["m2"] or 0
            nivel = r["nivel_proyecto"]
            if nivel == "ejecutivo":
                total_fondo += m2 * 200
            elif nivel == "integral":
                total_fondo += m2 * 100
        return jsonify({"total_fondo": total_fondo}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/notificaciones/status', methods=['GET'])
def notificaciones_status():
    status = {
        "correo": {"configurado": False, "conectado": False},
        "whatsapp": {"configurado": False, "conectado": False}
    }
    if SENDGRID_API_KEY:
        status["correo"]["configurado"] = True
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            status["correo"]["conectado"] = True
        except Exception as e:
            status["correo"]["conectado"] = False
            status["correo"]["error"] = str(e)
    wa_host = os.environ.get("WA_SERVICE_HOST", "http://127.0.0.1:3001")
    try:
        req = urllib.request.Request(f"{wa_host}/status")
        resp = urllib.request.urlopen(req, timeout=3)
        if resp.status == 200:
            wa_status = json.loads(resp.read().decode())
            status["whatsapp"]["configurado"] = True
            status["whatsapp"]["conectado"] = wa_status.get("ready", False)
            status["whatsapp"]["error"] = wa_status.get("error")
    except Exception as e:
        status["whatsapp"]["error"] = str(e)
    return jsonify(status), 200

# ---- FONDOS (Provisiones mensuales para equipos/gastos futuros) ----

@app.route('/api/fondos', methods=['GET', 'POST'])
def fondos():
    try:
        conn = get_connection()
        if request.method == 'POST':
            data = request.json
            execute(conn, "INSERT INTO fondos (nombre, monto_mensual, balance_actual) VALUES (?, ?, ?)",
                    (data['nombre'], data.get('monto_mensual', 0), data.get('balance_actual', 0)))
            conn.commit()
            conn.close()
            return jsonify({"status": "success"}), 201
        rows = fetchall(conn, "SELECT * FROM fondos ORDER BY id")
        conn.close()
        return jsonify([dictify(r) for r in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fondos/<int:fondo_id>', methods=['DELETE'])
def eliminar_fondo(fondo_id):
    try:
        conn = get_connection()
        execute(conn, "DELETE FROM movimientos_fondo WHERE fondo_id = ?", (fondo_id,))
        execute(conn, "DELETE FROM fondos WHERE id = ?", (fondo_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fondos/<int:fondo_id>/apartar', methods=['POST'])
def apartar_fondo(fondo_id):
    try:
        conn = get_connection()
        data = request.json
        monto = data['monto']
        fecha = data.get('fecha', datetime.datetime.now().isoformat())
        execute(conn, "INSERT INTO movimientos_fondo (fondo_id, tipo, monto, fecha, concepto) VALUES (?, 'apartado', ?, ?, ?)",
                (fondo_id, monto, fecha, data.get('concepto', 'Aportación mensual')))
        execute(conn, "UPDATE fondos SET balance_actual = balance_actual + ? WHERE id = ?", (monto, fondo_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fondos/<int:fondo_id>/retirar', methods=['POST'])
def retirar_fondo(fondo_id):
    try:
        conn = get_connection()
        data = request.json
        monto = data['monto']
        fondo = fetchone(conn, "SELECT balance_actual FROM fondos WHERE id = ?", (fondo_id,))
        if not fondo:
            conn.close()
            return jsonify({"status": "error", "message": "Fondo no encontrado"}), 404
        if fondo['balance_actual'] < monto:
            conn.close()
            return jsonify({"status": "error", "message": "Saldo insuficiente"}), 400
        fecha = data.get('fecha', datetime.datetime.now().isoformat())
        execute(conn, "INSERT INTO movimientos_fondo (fondo_id, tipo, monto, fecha, concepto) VALUES (?, 'retiro', ?, ?, ?)",
                (fondo_id, monto, fecha, data.get('concepto', 'Retiro')))
        execute(conn, "UPDATE fondos SET balance_actual = balance_actual - ? WHERE id = ?", (monto, fondo_id))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fondos/<int:fondo_id>/movimientos', methods=['GET'])
def movimientos_fondo(fondo_id):
    try:
        conn = get_connection()
        rows = fetchall(conn, "SELECT * FROM movimientos_fondo WHERE fondo_id = ? ORDER BY fecha DESC, id DESC", (fondo_id,))
        conn.close()
        return jsonify([dictify(r) for r in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(port=port, debug=False, host='0.0.0.0', threaded=True)
