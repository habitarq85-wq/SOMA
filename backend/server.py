from flask import Flask, request, jsonify, send_from_directory, send_file, Response
from flask_cors import CORS
import datetime
import json
import os
import re
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db import get_connection, execute, fetchone, fetchall, get_lastrowid, dictify, json_loads

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'))

app = Flask(__name__)
CORS(app)

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

TWILIO_SID = os.environ.get("TWILIO_SID", "").strip()
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN", "").strip()
TWILIO_WHATSAPP = os.environ.get("TWILIO_WHATSAPP", "+14155238886")
NOTIFICACION_WHATSAPP = os.environ.get("NOTIFICACION_WHATSAPP", "").strip()

MINIMO_TALLER = 6500
RANGOS_OBRA = {
    250: {"min": 14000, "max": 16500},
    350: {"min": 18500, "max": 23000},
    850: {"min": 28000, "max": 40000}
}

os.makedirs(REPORTES_DIR, exist_ok=True)

def init_db():
    conn = get_connection()
    use_pg = bool(os.environ.get('DATABASE_URL', ''))
    tables = {
        'captura_web': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('temp_id', 'TEXT'), ('contacto', 'TEXT'), ('presupuesto', 'TEXT'),
            ('habitantes', 'TEXT'), ('respuestas_json', 'TEXT'), ('analisis_procesado', 'TEXT'),
            ('fecha', 'TEXT'), ('estado', 'TEXT'), ('m2', 'REAL'),
            ('honorarios_diseno', 'REAL'), ('inversion_obra_estimada', 'REAL'),
            ('nivel_proyecto', 'TEXT'), ("pipeline_estado", "TEXT DEFAULT 'lead'"),
        ],
        'cobros': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('concepto', 'TEXT'), ('monto', 'REAL'),
            ('fecha_vencimiento', 'TEXT'), ('fecha_pago', 'TEXT'),
            ("estado", "TEXT DEFAULT 'pendiente'"), ('metodo_pago', 'TEXT'), ('notas', 'TEXT'),
        ],
        'config_fiscal': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('rfc', 'TEXT'), ("regimen", "TEXT DEFAULT 'RESICO'"),
            ('pac_api_key', 'TEXT'), ('activo', 'INTEGER DEFAULT 1'),
        ],
        'programa_arquitectonico': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('lead_id', 'INTEGER'), ('tipo', 'TEXT'), ('espacio', 'TEXT'), ('area', 'REAL'),
            ('zona', 'INTEGER'), ('horario_inicio', 'TEXT'), ('horario_fin', 'TEXT'),
            ('mobiliario', 'TEXT'), ('acontecimientos', 'TEXT'), ('patrones_espaciales', 'TEXT'),
            ('usuarios', 'INTEGER'), ('clave', 'TEXT'), ('relacion_directa', 'TEXT'),
        ],
        'matriz_inversion': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('categoria', 'TEXT'), ('prioridad_gasto', 'INTEGER'),
            ('porcentaje_asignado', 'REAL'), ('monto_estimado', 'REAL'),
        ],
        'habitantes': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('nombre', 'TEXT'), ('edad', 'INTEGER'),
            ('genero', 'TEXT'), ('estatura_cm', 'REAL'), ('peso_kg', 'REAL'),
            ('hobbies', 'TEXT'), ('rol_poder', 'TEXT'), ('observaciones', 'TEXT'),
        ],
        'actividades': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('habitante_id', 'INTEGER'), ('hora', 'INTEGER'), ('actividad_principal', 'TEXT'),
            ('aislamiento_necesario', 'INTEGER'), ('iluminacion_deseada', 'TEXT'),
            ('espacio_sugerido', 'TEXT'),
        ],
        'ejes_diseno': [
            ('id', 'SERIAL PRIMARY KEY' if use_pg else 'INTEGER PRIMARY KEY AUTOINCREMENT'),
            ('proyecto_id', 'INTEGER'), ('eje', 'TEXT'), ('valor_polar', 'REAL'),
            ('justificacion', 'TEXT'),
        ],
    }
    for table_name, columns in tables.items():
        cols_sql = ", ".join(f"{name} {typ}" for name, typ in columns)
        execute(conn, f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_sql})")
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
            from_email="habitarq85@gmail.com",
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
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        mensaje = f"🔔 NUEVO LEAD SOMA\nID: {temp_id}\nCliente: {contacto}\nPaquete: {nivel_key.upper()}\nEscala: {m2:.0f} m²"
        client.messages.create(
            body=mensaje,
            from_=f"whatsapp:{TWILIO_WHATSAPP}",
            to=f"whatsapp:{NOTIFICACION_WHATSAPP}"
        )
        print("--- WHATSAPP ENVIADO ---")
        return True
    except Exception as e:
        print(f"--- ERROR WHATSAPP: {e} ---")
        return False

@app.route('/save_immersion', methods=['POST'])
def save_immersion():
    data = request.json
    respuestas = data.get('respuestas', {})
    contacto = data.get('contacto', 'Anónimo')
    cotizacion = data.get('cotizacion', {})
    fecha_hoy = datetime.datetime.now().strftime("%Y%m%d-%H%M")
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
                     (temp_id, contacto, m2, honorarios_diseno, inversion_obra_estimada, nivel_proyecto, respuestas_json, analisis_procesado, fecha)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (temp_id, contacto, m2, total_diseno, obra_min, nivel_key,
                   json.dumps(respuestas), reporte, datetime.datetime.now().isoformat()))
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
        lead = fetchone(conn, "SELECT id, contacto, m2, nivel_proyecto, honorarios_diseno FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return jsonify({"status": "error", "message": "Lead no encontrado"}), 404

        totales_rows = fetchall(conn, "SELECT tipo, SUM(area) as total FROM programa_arquitectonico WHERE lead_id=? GROUP BY tipo", (lead_id,))
        totales_por_tipo = {r["tipo"]: r["total"] for r in totales_rows}

        total_m2_row = fetchone(conn, "SELECT SUM(area) as total FROM programa_arquitectonico WHERE lead_id=?", (lead_id,))
        total_m2 = (total_m2_row["total"] or 0) if total_m2_row else 0
        conn.close()

        contacto = lead["contacto"]
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
        lead = fetchone(conn, "SELECT id, contacto, m2, nivel_proyecto, honorarios_diseno, temp_id FROM captura_web WHERE id=?", (lead_id,))
        if not lead:
            conn.close()
            return "Lead no encontrado", 404
        contacto = lead["contacto"]
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
<p><strong>Cliente:</strong> {contacto}</p>
<p><strong>ID:</strong> {temp_id or '---'} &nbsp;|&nbsp; <strong>Fecha:</strong> {fecha}</p>
<p><strong>Paquete:</strong> {nivel_key.upper()} &nbsp;|&nbsp; <strong>m² estimados (web):</strong> {m2_lead or 0}</p>
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

@app.route('/get_leads', methods=['GET'])
def get_leads():
    try:
        conn = get_connection()
        rows = fetchall(conn, "SELECT * FROM captura_web ORDER BY fecha DESC")
        conn.close()
        return jsonify([dictify(row) for row in rows]), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

PIPELINE_ESTADOS = ['lead', 'entrevistado', 'programado', 'cotizado', 'contratado', 'pagado']

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

@app.route('/cobros/<int:proyecto_id>', methods=['GET'])
def get_cobros(proyecto_id):
    try:
        conn = get_connection()
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

@app.route('/')
def serve_web():
    web_path = os.path.join(PROYECTO_DIR, "web", "Pagina Web 6.html")
    if os.path.exists(web_path):
        with open(web_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Pagina no encontrada", 404

@app.route('/dashboard')
def serve_dashboard():
    dashboard_path = os.path.join(PROYECTO_DIR, "metodologia", "Bloque 1 - Gestion del Entorno (ADM)", "dashboard", "Dashboard.html")
    if os.path.exists(dashboard_path):
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Dashboard no encontrado", 404

@app.route('/css/<path:filename>')
def serve_css(filename):
    css_path = os.path.join(PROYECTO_DIR, "metodologia", "Bloque 1 - Gestion del Entorno (ADM)", "dashboard", "css", filename)
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

# ---- DIAGRAMA SOMA (Herramienta de Diseño - Bloque 2) ----

@app.route('/diagrama')
def serve_diagrama():
    diagrama_path = os.path.join(PROYECTO_DIR, "metodologia", "Bloque 2 - Taller SOMA (OPERACION)", "02 Análisis", "DiagramaSoma.html")
    if os.path.exists(diagrama_path):
        with open(diagrama_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "DiagramaSoma no encontrado", 404

@app.route('/carta-presentacion')
def serve_carta_presentacion():
    carta_path = os.path.join(PROYECTO_DIR, "metodologia", "Bloque 1 - Gestion del Entorno (ADM)", "CARTA_PRESENTACION_SOMA.html")
    if os.path.exists(carta_path):
        with open(carta_path, 'r', encoding='utf-8') as f:
            return f.read(), 200, {'Content-Type': 'text/html; charset=utf-8'}
    return "Carta de presentación no encontrada", 404

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

@app.route('/save_lead_magnet', methods=['POST'])
def save_lead_magnet():
    data = request.json
    nombre = data.get('nombre', 'Anónimo')
    contacto = data.get('contacto', '')
    fuente = data.get('fuente', 'lead_magnet')
    fecha = datetime.datetime.now().isoformat()
    try:
        conn = get_connection()
        execute(conn, """INSERT INTO captura_web
                     (temp_id, contacto, m2, honorarios_diseno, nivel_proyecto, respuestas_json, analisis_procesado, fecha)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                  (f"LM-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}", f"{nombre} - {contacto}",
                   0, 0, 'lead_magnet', json.dumps({"fuente": fuente, "nombre": nombre}),
                   f"Lead magnet: {fuente}", fecha))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok"}), 200
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
    if TWILIO_SID and TWILIO_TOKEN:
        status["whatsapp"]["configurado"] = True
        try:
            client = Client(TWILIO_SID, TWILIO_TOKEN)
            client.api.accounts(TWILIO_SID).fetch()
            status["whatsapp"]["conectado"] = True
        except Exception:
            status["whatsapp"]["conectado"] = False
    return jsonify(status), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(port=port, debug=False, host='0.0.0.0')
