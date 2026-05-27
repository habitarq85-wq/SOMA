import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel, Entry, Button, Label, Frame, Listbox, Scrollbar, END, Canvas, LabelFrame
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime
import json
from tkinter import filedialog
import os
import re

# =========================== BASE DE DATOS ===========================
def inicializar_db():
    """Crea las tablas si no existen (NO borra datos existentes)"""
    conn = sqlite3.connect('proyectos_arquitectonicos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyectos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_proyecto TEXT UNIQUE,
            fecha_creacion TEXT,
            fecha_modificacion TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyecto_datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proyecto_id INTEGER,
            campo TEXT,
            valor TEXT,
            FOREIGN KEY(proyecto_id) REFERENCES proyectos(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS espacios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proyecto_id INTEGER,
            tipo_programa TEXT,
            espacio TEXT,
            area REAL,
            zona INTEGER,
            horario_inicio TEXT,
            horario_fin TEXT,
            mobiliario TEXT,
            acontecimientos TEXT,
            patrones_espaciales TEXT,
            usuarios INTEGER,
            clave TEXT,
            relacion_directa TEXT,
            FOREIGN KEY(proyecto_id) REFERENCES proyectos(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Inicializar BD (NO borrar datos existentes)
inicializar_db()
conn = sqlite3.connect('proyectos_arquitectonicos.db')
proyecto_actual_id = None

# Colores SOMA
COLORS = {
    'bg': '#0a0a0a',
    'paper': '#f4f1ee',
    'accent': '#bc4b21',
    'card_bg': '#1a1a1a',
    'border': '#2a2a2a',
    'deseado': '#bc4b21',
    'complementario': '#6b8f6b',
    'lujo': '#d4af37',
    'tree_bg': '#2a2a2a',
    'tree_fg': '#f4f1ee',
    'tree_selected': '#bc4b21'
}

# Diccionario de preguntas
preguntas = {
    "nombre_proyecto": "Cual es el nombre del proyecto",
    "cliente": "Cual es el nombre del cliente",
    "tipo_edificio": "Que tipo de edificio es",
    "objetivo": "Cual es el objetivo del proyecto",
    "presupuesto": "Cual es el presupuesto estimado (en MXN)",
    "superficie_terreno": "Cual es la superficie total del terreno (en m2)",
    "ubicacion_mundial": "Ubicacion mundial (pais)",
    "ubicacion_nacional": "Ubicacion nacional (estado)",
    "ubicacion_estatal": "Ubicacion estatal (municipio)",
    "ubicacion_local": "Ubicacion local (colonia)",
    "ubicacion_urbano": "Ubicacion urbano (calle)"
}

# Descripcion de zonas
descripcion_zona = {
    1: "Social",
    2: "Operativa",
    3: "Descanso",
    4: "Soporte",
    5: "Transicion"
}

# =========================== FUNCION DE HORARIO ===========================
def validar_horario(horario_str):
    pattern = r'^([0-1][0-9]|2[0-3]):([0-5][0-9])$'
    return re.match(pattern, horario_str) is not None

def entrada_horario_dual(parent, titulo):
    ventana = Toplevel(parent)
    ventana.title("Soma // Horario")
    ventana.geometry("400x300")
    ventana.configure(bg=COLORS['bg'])
    ventana.transient(parent)
    ventana.grab_set()
    
    frame = Frame(ventana, bg=COLORS['bg'], padx=25, pady=25)
    frame.pack(fill="both", expand=True)
    
    Label(frame, text="Ingrese el horario del espacio", bg=COLORS['bg'], 
          font=("JetBrains Mono", 10, "bold"), fg=COLORS['paper']).pack(pady=(0, 10))
    
    Label(frame, text="Formato: HH:MM", bg=COLORS['bg'], fg=COLORS['accent'], 
          font=("JetBrains Mono", 8)).pack(pady=(0, 10))
    
    # Horario INICIO
    Label(frame, text="Hora de INICIO", bg=COLORS['bg'], fg=COLORS['paper'], 
          font=("Unbounded", 8, "bold")).pack(pady=(5, 2))
    frame_inicio = Frame(frame, bg=COLORS['bg'])
    frame_inicio.pack(pady=2)
    hora_inicio_var = tk.StringVar(value="09")
    tk.Spinbox(frame_inicio, from_=0, to=23, width=3, format="%02.0f",
               textvariable=hora_inicio_var, bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", font=("JetBrains Mono", 10)).pack(side="left", padx=2)
    Label(frame_inicio, text=":", bg=COLORS['bg'], fg=COLORS['paper'], 
          font=("JetBrains Mono", 12, "bold")).pack(side="left")
    minuto_inicio_var = tk.StringVar(value="00")
    tk.Spinbox(frame_inicio, from_=0, to=59, width=3, format="%02.0f",
               textvariable=minuto_inicio_var, bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", font=("JetBrains Mono", 10)).pack(side="left", padx=2)
    
    # Horario FIN
    Label(frame, text="Hora de FIN", bg=COLORS['bg'], fg=COLORS['paper'], 
          font=("Unbounded", 8, "bold")).pack(pady=(8, 2))
    frame_fin = Frame(frame, bg=COLORS['bg'])
    frame_fin.pack(pady=2)
    hora_fin_var = tk.StringVar(value="18")
    tk.Spinbox(frame_fin, from_=0, to=23, width=3, format="%02.0f",
               textvariable=hora_fin_var, bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", font=("JetBrains Mono", 10)).pack(side="left", padx=2)
    Label(frame_fin, text=":", bg=COLORS['bg'], fg=COLORS['paper'], 
          font=("JetBrains Mono", 12, "bold")).pack(side="left")
    minuto_fin_var = tk.StringVar(value="00")
    tk.Spinbox(frame_fin, from_=0, to=59, width=3, format="%02.0f",
               textvariable=minuto_fin_var, bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", font=("JetBrains Mono", 10)).pack(side="left", padx=2)
    
    resultado = [None, None]
    def guardar():
        resultado[0] = f"{int(hora_inicio_var.get()):02d}:{int(minuto_inicio_var.get()):02d}"
        resultado[1] = f"{int(hora_fin_var.get()):02d}:{int(minuto_fin_var.get()):02d}"
        ventana.destroy()
    
    Button(frame, text="Guardar Horario", command=guardar,
           bg=COLORS['accent'], fg='white', font=("Unbounded", 8),
           relief="flat", pady=4).pack(pady=10)
    ventana.wait_window()
    return resultado[0], resultado[1]

# =========================== FUNCION DE CLAVE ===========================
def entrada_clave(parent, titulo):
    ventana = Toplevel(parent)
    ventana.title("Soma // Clave")
    ventana.geometry("350x180")
    ventana.configure(bg=COLORS['bg'])
    ventana.transient(parent)
    ventana.grab_set()
    
    frame = Frame(ventana, bg=COLORS['bg'], padx=25, pady=25)
    frame.pack(fill="both", expand=True)
    
    Label(frame, text="Ingrese la clave del espacio", bg=COLORS['bg'], 
          font=("JetBrains Mono", 10, "bold"), fg=COLORS['paper']).pack(pady=(0, 10))
    Label(frame, text="Solo el numero (ejemplo: 1, 2, 3)", bg=COLORS['bg'], 
          fg=COLORS['accent'], font=("JetBrains Mono", 8)).pack(pady=(0, 10))
    
    entrada = Entry(frame, font=("JetBrains Mono", 11), bg=COLORS['card_bg'], 
                    fg=COLORS['paper'], insertbackground=COLORS['paper'],
                    relief="flat", width=15, justify="center")
    entrada.pack(pady=5)
    
    resultado = [None]
    def guardar():
        valor = entrada.get().strip()
        if valor:
            try:
                num = int(valor)
                if num >= 1:
                    resultado[0] = f"E{num}"
                    ventana.destroy()
                else:
                    messagebox.showwarning("Error", "El numero debe ser 1 o mayor")
            except ValueError:
                messagebox.showwarning("Error", "Ingrese un numero valido")
        else:
            messagebox.showwarning("Error", "Ingrese un numero")
    
    Button(frame, text="Guardar Clave", command=guardar,
           bg=COLORS['accent'], fg='white', font=("Unbounded", 8),
           relief="flat", pady=4).pack(pady=8)
    entrada.bind('<Return>', lambda e: guardar())
    ventana.wait_window()
    return resultado[0]

# =========================== FUNCION DE RELACION ===========================
def entrada_relacion(parent, titulo, existentes=None):
    """Ventana para ingresar relacion directa (ACUMULA valores, no reemplaza)"""
    ventana = Toplevel(parent)
    ventana.title("Soma // Relacion directa")
    ventana.geometry("400x300")
    ventana.configure(bg=COLORS['bg'])
    ventana.transient(parent)
    ventana.grab_set()
    
    frame = Frame(ventana, bg=COLORS['bg'], padx=25, pady=20)
    frame.pack(fill="both", expand=True)
    
    Label(frame, text="Relaciones directas (AGREGAR)", bg=COLORS['bg'], 
          font=("JetBrains Mono", 10, "bold"), fg=COLORS['paper']).pack(pady=(0, 5))
    Label(frame, text="Ingrese numeros separados por coma (ej: 1, 3, 5)", 
          bg=COLORS['bg'], fg=COLORS['accent'], font=("JetBrains Mono", 7)).pack(pady=(0, 10))
    
    entrada = Entry(frame, font=("JetBrains Mono", 10), bg=COLORS['card_bg'], 
                    fg=COLORS['paper'], insertbackground=COLORS['paper'],
                    relief="flat", width=30)
    entrada.pack(pady=5)
    
    resultado = [None]
    def guardar():
        valor = entrada.get().strip()
        if valor:
            numeros = re.findall(r'\d+', valor)
            if numeros:
                nuevos = []
                for n in numeros:
                    num = int(n)
                    if num >= 1:
                        nuevos.append(f"E{num}")
                    else:
                        messagebox.showwarning("Error", f"Numero {n} no valido. Use 1 o mayor")
                        return
                resultado[0] = nuevos
                ventana.destroy()
            else:
                messagebox.showwarning("Error", "Ingrese al menos un numero")
        else:
            resultado[0] = []
            ventana.destroy()
    
    Button(frame, text="AGREGAR Relaciones", command=guardar,
           bg=COLORS['accent'], fg='white', font=("Unbounded", 8),
           relief="flat", pady=4).pack(pady=10)
    entrada.bind('<Return>', lambda e: guardar())
    ventana.wait_window()
    return resultado[0] if resultado[0] is not None else []

# =========================== FUNCIONES DE PREGUNTAS ===========================
def hacer_pregunta(campo, valor_actual=""):
    ventana = Toplevel(root)
    titulo = campo.replace('_', ' ').title()
    ventana.title(f"Soma // {titulo}")
    ventana.geometry("450x200")
    ventana.configure(bg=COLORS['bg'])
    ventana.transient(root)
    ventana.grab_set()
    
    frame = Frame(ventana, bg=COLORS['bg'], padx=25, pady=25)
    frame.pack(fill="both", expand=True)
    
    pregunta_texto = preguntas.get(campo, f"Ingrese {campo.replace('_', ' ')}")
    lbl_pregunta = Label(frame, text=pregunta_texto, bg=COLORS['bg'], 
                         font=("JetBrains Mono", 10, "bold"), fg=COLORS['paper'],
                         wraplength=380)
    lbl_pregunta.pack(pady=(0, 12))
    
    entrada = Entry(frame, font=("JetBrains Mono", 10), bg=COLORS['card_bg'], 
                    fg=COLORS['paper'], insertbackground=COLORS['paper'],
                    relief="flat", width=35)
    entrada.pack(pady=(0, 12))
    
    if valor_actual and valor_actual != "None" and valor_actual != "":
        entrada.insert(0, str(valor_actual))
    
    def guardar_respuesta(event=None):
        global proyecto_actual_id
        respuesta = entrada.get().strip()
        if respuesta:
            if campo == "nombre_proyecto":
                var_nombre.set(respuesta)
            elif campo == "cliente":
                var_cliente.set(respuesta)
            elif campo == "tipo_edificio":
                var_tipo.set(respuesta)
            elif campo == "objetivo":
                var_objetivo.set(respuesta)
            elif campo == "presupuesto":
                var_presupuesto.set(respuesta)
            elif campo == "superficie_terreno":
                var_superficie_terreno.set(respuesta)
            elif campo == "ubicacion_mundial":
                var_ubicacion_mundial.set(respuesta)
            elif campo == "ubicacion_nacional":
                var_ubicacion_nacional.set(respuesta)
            elif campo == "ubicacion_estatal":
                var_ubicacion_estatal.set(respuesta)
            elif campo == "ubicacion_local":
                var_ubicacion_local.set(respuesta)
            elif campo == "ubicacion_urbano":
                var_ubicacion_urbano.set(respuesta)
            
            guardar_proyecto()
            ventana.destroy()
        else:
            messagebox.showwarning("Campo vacio", "Escribe una respuesta")
    
    btn_guardar = Button(frame, text="Guardar", command=guardar_respuesta,
                         bg=COLORS['accent'], fg='white', font=("Unbounded", 8),
                         relief="flat", pady=4)
    btn_guardar.pack()
    entrada.bind('<Return>', guardar_respuesta)
    entrada.focus()

# =========================== FUNCIONES DE EDICION ===========================
def editar_espacio(espacio_id, tipo_programa):
    cursor = conn.cursor()
    cursor.execute("SELECT espacio, area, zona, horario_inicio, horario_fin, mobiliario, acontecimientos, patrones_espaciales, usuarios, clave, relacion_directa FROM espacios WHERE id=? AND proyecto_id=?", 
                   (espacio_id, proyecto_actual_id))
    datos = cursor.fetchone()
    
    if not datos:
        messagebox.showerror("Error", "No se encontró el espacio")
        return
    
    ventana = Toplevel(root)
    ventana.title(f"Soma // Editar Espacio - {datos[0]}")
    ventana.geometry("715x770")  # Aumentado 10% (650x700 -> 715x770)
    ventana.configure(bg=COLORS['bg'])
    
    canvas = Canvas(ventana, bg=COLORS['bg'], highlightthickness=0)
    scrollbar = Scrollbar(ventana, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=COLORS['bg'])
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    frame = Frame(scrollable_frame, bg=COLORS['bg'], padx=15, pady=15)
    frame.pack(fill="both", expand=True)
    
    frame_titulo = Frame(frame, bg=COLORS['bg'])
    frame_titulo.pack(fill="x", pady=(0, 10))
    Label(frame_titulo, text=f"EDITANDO: {datos[0]}", bg=COLORS['bg'], 
          font=("Unbounded", 10, "bold"), fg=COLORS['accent']).pack(side="left")
    btn_guardar = Button(frame_titulo, text="💾 Guardar", bg=COLORS['accent'], 
                         fg='white', font=("Unbounded", 8, "bold"),
                         relief="flat", padx=10, pady=3, cursor="hand2")
    btn_guardar.pack(side="right")
    
    entradas = {}
    
    # Campos basicos
    campos = [
        ("Espacio", datos[0]),
        ("Area (m2)", datos[1]),
        ("Zona (1-5)", datos[2]),
        ("Numero de usuarios", datos[8])
    ]
    for label, valor in campos:
        f = Frame(frame, bg=COLORS['bg'])
        f.pack(fill="x", pady=3)
        Label(f, text=label, bg=COLORS['bg'], font=("JetBrains Mono", 8), 
              fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
        entry = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], 
                      fg=COLORS['paper'], relief="flat", width=25)
        entry.insert(0, str(valor))
        entry.pack(side="left", padx=5)
        entradas[label] = entry
    
    # Info zona
    fz = Frame(frame, bg=COLORS['bg'])
    fz.pack(fill="x", pady=2)
    Label(fz, text="1:Social | 2:Operativa | 3:Descanso | 4:Soporte | 5:Transicion", 
          bg=COLORS['bg'], fg=COLORS['accent'], font=("JetBrains Mono", 6)).pack(anchor="w")
    
    # Horario
    f = Frame(frame, bg=COLORS['bg'])
    f.pack(fill="x", pady=5)
    Label(f, text="Horario", bg=COLORS['bg'], font=("JetBrains Mono", 8), 
          fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
    horario_inicio = tk.StringVar(value=datos[3] if datos[3] else "")
    horario_fin = tk.StringVar(value=datos[4] if datos[4] else "")
    e1 = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", width=8, textvariable=horario_inicio, state="readonly")
    e1.pack(side="left", padx=2)
    Label(f, text="-", bg=COLORS['bg'], fg=COLORS['paper'], font=("JetBrains Mono", 9)).pack(side="left", padx=2)
    e2 = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", width=8, textvariable=horario_fin, state="readonly")
    e2.pack(side="left", padx=2)
    def sel_horario():
        ini, fin = entrada_horario_dual(ventana, "Horario")
        if ini and fin:
            horario_inicio.set(ini)
            horario_fin.set(fin)
    Button(f, text="⌚", command=sel_horario, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 8), width=2, relief="flat").pack(side="left", padx=2)
    
    # Clave
    f = Frame(frame, bg=COLORS['bg'])
    f.pack(fill="x", pady=5)
    Label(f, text="Clave (E1,E2...)", bg=COLORS['bg'], font=("JetBrains Mono", 8), 
          fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
    clave_var = tk.StringVar(value=datos[9] if datos[9] else "")
    e_clave = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
                    relief="flat", width=15, textvariable=clave_var, state="readonly")
    e_clave.pack(side="left", padx=2)
    def sel_clave():
        cl = entrada_clave(ventana, "Clave")
        if cl:
            clave_var.set(cl)
    Button(f, text="🔑", command=sel_clave, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 8), width=2, relief="flat").pack(side="left", padx=2)
    
    # Listas
    try:
        mob_items = json.loads(datos[5]) if datos[5] else []
        acon_items = json.loads(datos[6]) if datos[6] else []
        pat_items = json.loads(datos[7]) if datos[7] else []
        rel_items = json.loads(datos[10]) if datos[10] else []
    except:
        mob_items, acon_items, pat_items, rel_items = [], [], [], []
    
    def crear_lista(titulo, items, frame_padre):
        f = LabelFrame(frame_padre, text=titulo, bg=COLORS['bg'], fg=COLORS['accent'],
                       font=("JetBrains Mono", 7, "bold"), bd=1, relief="solid")
        f.pack(fill="x", pady=5)
        lbox = Listbox(f, font=("JetBrains Mono", 7), height=3, bg=COLORS['card_bg'], 
                       fg=COLORS['paper'], selectbackground=COLORS['accent'])
        lbox.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        def actualizar():
            lbox.delete(0, END)
            for item in items:
                lbox.insert(END, f"• {item}")
        actualizar()
        fe = Frame(f, bg=COLORS['bg'])
        fe.pack(side="right", padx=2)
        entry = Entry(fe, font=("JetBrains Mono", 7), width=12, bg=COLORS['card_bg'], 
                      fg=COLORS['paper'], relief="flat")
        entry.pack(pady=2)
        def agregar():
            val = entry.get().strip()
            if val:
                items.append(val)
                actualizar()
                entry.delete(0, END)
        Button(fe, text="+", command=agregar, bg=COLORS['accent'], fg='white',
               font=("Unbounded", 7), width=2, relief="flat").pack()
        return items, lbox
    
    mob_items, _ = crear_lista("Mobiliario", mob_items, frame)
    acon_items, _ = crear_lista("Acontecimientos", acon_items, frame)
    pat_items, _ = crear_lista("Patrones espaciales", pat_items, frame)
    
    # Relacion directa - CON ACUMULACION
    fr = LabelFrame(frame, text="Relacion directa (AGREGAR)", bg=COLORS['bg'], fg=COLORS['accent'],
                    font=("JetBrains Mono", 7, "bold"), bd=1, relief="solid")
    fr.pack(fill="x", pady=5)
    lbox_rel = Listbox(fr, font=("JetBrains Mono", 7), height=3, bg=COLORS['card_bg'], 
                       fg=COLORS['paper'], selectbackground=COLORS['accent'])
    lbox_rel.pack(side="left", fill="x", expand=True, padx=2, pady=2)
    def actualizar_rel():
        lbox_rel.delete(0, END)
        for item in rel_items:
            lbox_rel.insert(END, f"• {item}")
    actualizar_rel()
    fe_rel = Frame(fr, bg=COLORS['bg'])
    fe_rel.pack(side="right", padx=2)
    def sel_rel():
        nuevas = entrada_relacion(ventana, "Relacion directa")
        if nuevas:
            for item in nuevas:
                if item not in rel_items:  # Evitar duplicados
                    rel_items.append(item)
            actualizar_rel()
    Button(fe_rel, text="+", command=sel_rel, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 7), width=2, relief="flat").pack(pady=2)
    
    def guardar_cambios():
        try:
            nombre = entradas["Espacio"].get().strip()
            if not nombre:
                messagebox.showwarning("Error", "Nombre obligatorio")
                return
            area = float(entradas["Area (m2)"].get()) if entradas["Area (m2)"].get() else 0
            zona = int(entradas["Zona (1-5)"].get()) if entradas["Zona (1-5)"].get() else 1
            usuarios = int(entradas["Numero de usuarios"].get()) if entradas["Numero de usuarios"].get() else 0
            if zona < 1 or zona > 5:
                messagebox.showwarning("Error", "Zona entre 1 y 5")
                return
            
            clave = clave_var.get().strip()
            if not clave:
                messagebox.showwarning("Error", "Clave obligatoria")
                return
            
            cursor = conn.cursor()
            cursor.execute('''UPDATE espacios SET espacio=?, area=?, zona=?, horario_inicio=?, horario_fin=?,
                              mobiliario=?, acontecimientos=?, patrones_espaciales=?, usuarios=?, clave=?, relacion_directa=?
                              WHERE id=? AND proyecto_id=?''',
                           (nombre, area, zona, horario_inicio.get(), horario_fin.get(),
                            json.dumps(mob_items), json.dumps(acon_items), json.dumps(pat_items),
                            usuarios, clave, json.dumps(rel_items), espacio_id, proyecto_actual_id))
            conn.commit()
            actualizar_todas_tablas()
            ventana.destroy()
            messagebox.showinfo("Exito", "Espacio actualizado")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    btn_guardar.config(command=guardar_cambios)

# =========================== NUEVO PROYECTO ===========================
def nuevo_proyecto_action():
    global proyecto_actual_id
    proyecto_actual_id = None
    var_nombre.set("")
    var_cliente.set("")
    var_tipo.set("")
    var_objetivo.set("")
    var_presupuesto.set("")
    var_superficie_terreno.set("")
    var_ubicacion_mundial.set("")
    var_ubicacion_nacional.set("")
    var_ubicacion_estatal.set("")
    var_ubicacion_local.set("")
    var_ubicacion_urbano.set("")
    
    actualizar_vista_proyecto()
    actualizar_todas_tablas()
    hacer_pregunta("nombre_proyecto", "")

# =========================== FUNCIONES DE ESPACIOS ===========================
def nuevo_espacio(tipo_programa):
    global proyecto_actual_id
    if not proyecto_actual_id:
        messagebox.showwarning("Sin proyecto", "Primero crea un proyecto con Nuevo Proyecto")
        return
    
    ventana = Toplevel(root)
    ventana.title(f"Soma // Nuevo Espacio - {tipo_programa}")
    ventana.geometry("715x770")  # Aumentado 10% (650x700 -> 715x770)
    ventana.configure(bg=COLORS['bg'])
    
    canvas = Canvas(ventana, bg=COLORS['bg'], highlightthickness=0)
    scrollbar = Scrollbar(ventana, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg=COLORS['bg'])
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    frame = Frame(scrollable_frame, bg=COLORS['bg'], padx=15, pady=15)
    frame.pack(fill="both", expand=True)
    
    frame_titulo = Frame(frame, bg=COLORS['bg'])
    frame_titulo.pack(fill="x", pady=(0, 10))
    Label(frame_titulo, text=f"Agregar Espacio a {tipo_programa}", bg=COLORS['bg'], 
          font=("Unbounded", 10, "bold"), fg=COLORS['accent']).pack(side="left")
    btn_guardar = Button(frame_titulo, text="💾 Guardar", bg=COLORS['accent'], 
                         fg='white', font=("Unbounded", 8, "bold"),
                         relief="flat", padx=10, pady=3, cursor="hand2")
    btn_guardar.pack(side="right")
    
    entradas = {}
    
    # Campos basicos
    campos = [
        ("Espacio", "espacio"),
        ("Area (m2)", "area"),
        ("Zona (1-5)", "zona"),
        ("Numero de usuarios", "usuarios")
    ]
    for label, key in campos:
        f = Frame(frame, bg=COLORS['bg'])
        f.pack(fill="x", pady=3)
        Label(f, text=label, bg=COLORS['bg'], font=("JetBrains Mono", 8), 
              fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
        entry = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], 
                      fg=COLORS['paper'], relief="flat", width=25)
        entry.pack(side="left", padx=5)
        entradas[key] = entry
    
    # Info zona
    fz = Frame(frame, bg=COLORS['bg'])
    fz.pack(fill="x", pady=2)
    Label(fz, text="1:Social | 2:Operativa | 3:Descanso | 4:Soporte | 5:Transicion", 
          bg=COLORS['bg'], fg=COLORS['accent'], font=("JetBrains Mono", 6)).pack(anchor="w")
    
    # Horario
    f = Frame(frame, bg=COLORS['bg'])
    f.pack(fill="x", pady=5)
    Label(f, text="Horario", bg=COLORS['bg'], font=("JetBrains Mono", 8), 
          fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
    horario_inicio = tk.StringVar()
    horario_fin = tk.StringVar()
    e1 = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", width=8, textvariable=horario_inicio, state="readonly")
    e1.pack(side="left", padx=2)
    Label(f, text="-", bg=COLORS['bg'], fg=COLORS['paper'], font=("JetBrains Mono", 9)).pack(side="left", padx=2)
    e2 = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
               relief="flat", width=8, textvariable=horario_fin, state="readonly")
    e2.pack(side="left", padx=2)
    def sel_horario():
        ini, fin = entrada_horario_dual(ventana, "Horario")
        if ini and fin:
            horario_inicio.set(ini)
            horario_fin.set(fin)
    Button(f, text="⌚", command=sel_horario, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 8), width=2, relief="flat").pack(side="left", padx=2)
    
    # Clave
    f = Frame(frame, bg=COLORS['bg'])
    f.pack(fill="x", pady=5)
    Label(f, text="Clave (E1,E2...)", bg=COLORS['bg'], font=("JetBrains Mono", 8), 
          fg=COLORS['paper'], width=14, anchor="w").pack(side="left")
    clave_var = tk.StringVar()
    e_clave = Entry(f, font=("JetBrains Mono", 9), bg=COLORS['card_bg'], fg=COLORS['paper'],
                    relief="flat", width=15, textvariable=clave_var, state="readonly")
    e_clave.pack(side="left", padx=2)
    def sel_clave():
        cl = entrada_clave(ventana, "Clave")
        if cl:
            clave_var.set(cl)
    Button(f, text="🔑", command=sel_clave, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 8), width=2, relief="flat").pack(side="left", padx=2)
    
    # Listas
    mob_items, acon_items, pat_items, rel_items = [], [], [], []
    
    def crear_lista(titulo, items, frame_padre):
        f = LabelFrame(frame_padre, text=titulo, bg=COLORS['bg'], fg=COLORS['accent'],
                       font=("JetBrains Mono", 7, "bold"), bd=1, relief="solid")
        f.pack(fill="x", pady=5)
        lbox = Listbox(f, font=("JetBrains Mono", 7), height=3, bg=COLORS['card_bg'], 
                       fg=COLORS['paper'], selectbackground=COLORS['accent'])
        lbox.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        def actualizar():
            lbox.delete(0, END)
            for item in items:
                lbox.insert(END, f"• {item}")
        actualizar()
        fe = Frame(f, bg=COLORS['bg'])
        fe.pack(side="right", padx=2)
        entry = Entry(fe, font=("JetBrains Mono", 7), width=12, bg=COLORS['card_bg'], 
                      fg=COLORS['paper'], relief="flat")
        entry.pack(pady=2)
        def agregar():
            val = entry.get().strip()
            if val:
                items.append(val)
                actualizar()
                entry.delete(0, END)
        Button(fe, text="+", command=agregar, bg=COLORS['accent'], fg='white',
               font=("Unbounded", 7), width=2, relief="flat").pack()
        return items, lbox
    
    mob_items, _ = crear_lista("Mobiliario", mob_items, frame)
    acon_items, _ = crear_lista("Acontecimientos", acon_items, frame)
    pat_items, _ = crear_lista("Patrones espaciales", pat_items, frame)
    
    # Relacion directa - CON ACUMULACION
    fr = LabelFrame(frame, text="Relacion directa (AGREGAR)", bg=COLORS['bg'], fg=COLORS['accent'],
                    font=("JetBrains Mono", 7, "bold"), bd=1, relief="solid")
    fr.pack(fill="x", pady=5)
    lbox_rel = Listbox(fr, font=("JetBrains Mono", 7), height=3, bg=COLORS['card_bg'], 
                       fg=COLORS['paper'], selectbackground=COLORS['accent'])
    lbox_rel.pack(side="left", fill="x", expand=True, padx=2, pady=2)
    def actualizar_rel():
        lbox_rel.delete(0, END)
        for item in rel_items:
            lbox_rel.insert(END, f"• {item}")
    actualizar_rel()
    fe_rel = Frame(fr, bg=COLORS['bg'])
    fe_rel.pack(side="right", padx=2)
    def sel_rel():
        nuevas = entrada_relacion(ventana, "Relacion directa")
        if nuevas:
            for item in nuevas:
                if item not in rel_items:  # Evitar duplicados
                    rel_items.append(item)
            actualizar_rel()
    Button(fe_rel, text="+", command=sel_rel, bg=COLORS['accent'], fg='white',
           font=("Unbounded", 7), width=2, relief="flat").pack(pady=2)
    
    def guardar_espacio_final():
        try:
            nombre = entradas["espacio"].get().strip()
            if not nombre:
                messagebox.showwarning("Error", "Nombre del espacio obligatorio")
                return
            
            area = float(entradas["area"].get()) if entradas["area"].get() else 0
            zona = int(entradas["zona"].get()) if entradas["zona"].get() else 1
            usuarios = int(entradas["usuarios"].get()) if entradas["usuarios"].get() else 0
            
            if zona < 1 or zona > 5:
                messagebox.showwarning("Error", "La zona debe ser entre 1 y 5")
                return
            
            clave = clave_var.get().strip()
            if not clave:
                messagebox.showwarning("Error", "La clave es obligatoria")
                return
            
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO espacios (proyecto_id, tipo_programa, espacio, area, zona, 
                              horario_inicio, horario_fin, mobiliario, acontecimientos, patrones_espaciales, 
                              usuarios, clave, relacion_directa)
                              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                           (proyecto_actual_id, tipo_programa, nombre, area, zona,
                            horario_inicio.get(), horario_fin.get(),
                            json.dumps(mob_items), json.dumps(acon_items), json.dumps(pat_items),
                            usuarios, clave, json.dumps(rel_items)))
            conn.commit()
            actualizar_todas_tablas()
            ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    btn_guardar.config(command=guardar_espacio_final)

# =========================== FUNCIONES DE BASE DE DATOS ===========================
def guardar_proyecto():
    global proyecto_actual_id
    nombre = var_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Error", "Debes crear un proyecto con Nuevo Proyecto")
        return
    
    cursor = conn.cursor()
    ahora = datetime.now().isoformat()
    
    if proyecto_actual_id:
        cursor.execute("UPDATE proyectos SET nombre_proyecto=?, fecha_modificacion=? WHERE id=?", 
                      (nombre, ahora, proyecto_actual_id))
    else:
        cursor.execute("INSERT INTO proyectos (nombre_proyecto, fecha_creacion, fecha_modificacion) VALUES (?,?,?)",
                      (nombre, ahora, ahora))
        proyecto_actual_id = cursor.lastrowid
    
    datos_a_guardar = {
        "cliente": var_cliente.get(),
        "tipo_edificio": var_tipo.get(),
        "objetivo": var_objetivo.get(),
        "presupuesto": var_presupuesto.get(),
        "superficie_terreno": var_superficie_terreno.get(),
        "ubicacion": {
            "mundial": var_ubicacion_mundial.get(),
            "nacional": var_ubicacion_nacional.get(),
            "estatal": var_ubicacion_estatal.get(),
            "local": var_ubicacion_local.get(),
            "urbano": var_ubicacion_urbano.get()
        }
    }
    
    for campo, valor in datos_a_guardar.items():
        cursor.execute("DELETE FROM proyecto_datos WHERE proyecto_id=? AND campo=?", (proyecto_actual_id, campo))
        if valor:
            cursor.execute("INSERT INTO proyecto_datos (proyecto_id, campo, valor) VALUES (?,?,?)",
                          (proyecto_actual_id, campo, json.dumps(valor, ensure_ascii=False)))
    
    conn.commit()
    actualizar_vista_proyecto()
    actualizar_lista_proyectos()
    actualizar_todas_tablas()

def cargar_proyecto(proyecto_id):
    global proyecto_actual_id
    proyecto_actual_id = proyecto_id
    
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_proyecto FROM proyectos WHERE id=?", (proyecto_id,))
    resultado = cursor.fetchone()
    if resultado:
        var_nombre.set(resultado[0])
    
    cursor.execute("SELECT campo, valor FROM proyecto_datos WHERE proyecto_id=?", (proyecto_id,))
    for campo, valor_json in cursor.fetchall():
        valor = json.loads(valor_json)
        if campo == "ubicacion":
            var_ubicacion_mundial.set(valor.get("mundial", ""))
            var_ubicacion_nacional.set(valor.get("nacional", ""))
            var_ubicacion_estatal.set(valor.get("estatal", ""))
            var_ubicacion_local.set(valor.get("local", ""))
            var_ubicacion_urbano.set(valor.get("urbano", ""))
        elif campo == "cliente":
            var_cliente.set(valor)
        elif campo == "tipo_edificio":
            var_tipo.set(valor)
        elif campo == "objetivo":
            var_objetivo.set(valor)
        elif campo == "presupuesto":
            var_presupuesto.set(valor)
        elif campo == "superficie_terreno":
            var_superficie_terreno.set(valor)
    
    actualizar_vista_proyecto()
    actualizar_todas_tablas()
    actualizar_lista_proyectos()
    messagebox.showinfo("Exito", f"Proyecto '{resultado[0]}' cargado")

def actualizar_lista_proyectos():
    for item in lista_proyectos.get_children():
        lista_proyectos.delete(item)
    
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_proyecto, fecha_modificacion FROM proyectos ORDER BY fecha_modificacion DESC")
    for proyecto in cursor.fetchall():
        fecha = proyecto[2][:10] if proyecto[2] else ""
        lista_proyectos.insert("", END, values=(proyecto[1], fecha), iid=str(proyecto[0]))

def eliminar_proyecto():
    global proyecto_actual_id
    seleccion = lista_proyectos.selection()
    if seleccion:
        if messagebox.askyesno("Confirmar", "Eliminar este proyecto?"):
            proyecto_id = int(seleccion[0])
            cursor = conn.cursor()
            cursor.execute("DELETE FROM proyectos WHERE id=?", (proyecto_id,))
            cursor.execute("DELETE FROM proyecto_datos WHERE proyecto_id=?", (proyecto_id,))
            cursor.execute("DELETE FROM espacios WHERE proyecto_id=?", (proyecto_id,))
            conn.commit()
            actualizar_lista_proyectos()
            if proyecto_actual_id == proyecto_id:
                proyecto_actual_id = None
                var_nombre.set("")
                var_cliente.set("")
                var_tipo.set("")
                var_objetivo.set("")
                var_presupuesto.set("")
                var_superficie_terreno.set("")
                var_ubicacion_mundial.set("")
                var_ubicacion_nacional.set("")
                var_ubicacion_estatal.set("")
                var_ubicacion_local.set("")
                var_ubicacion_urbano.set("")
                actualizar_vista_proyecto()
                actualizar_todas_tablas()

def abrir_proyecto_seleccionado(event):
    seleccion = lista_proyectos.selection()
    if seleccion:
        cargar_proyecto(int(seleccion[0]))

def actualizar_tabla(tabla, tipo_programa):
    for row in tabla.get_children():
        tabla.delete(row)
    if proyecto_actual_id:
        cursor = conn.cursor()
        cursor.execute("SELECT id, espacio, area, horario_inicio, horario_fin, zona, mobiliario, acontecimientos, patrones_espaciales, usuarios, clave, relacion_directa FROM espacios WHERE proyecto_id=? AND tipo_programa=?", 
                       (proyecto_actual_id, tipo_programa))
        for row in cursor.fetchall():
            try:
                # Horario en formato vertical (arriba inicio, abajo fin) sin "a"
                if row[3] and row[4]:
                    horario_text = f"{row[3]}\n{row[4]}"
                else:
                    horario_text = "-"
                zona_text = f"{row[5]} ({descripcion_zona.get(row[5], '')})"
                mob = json.loads(row[6]) if row[6] else []
                acon = json.loads(row[7]) if row[7] else []
                pat = json.loads(row[8]) if row[8] else []
                rel = json.loads(row[11]) if row[11] else []
                mob_str = "\n".join(mob) if mob else "-"
                acon_str = "\n".join(acon) if acon else "-"
                pat_str = "\n".join(pat) if pat else "-"
                rel_str = "\n".join(rel) if rel else "-"
            except:
                mob_str = "-"
                acon_str = "-"
                pat_str = "-"
                rel_str = "-"
                horario_text = "-"
                zona_text = "-"
            tabla.insert("", END, values=(row[1], row[2], horario_text, zona_text, mob_str, acon_str, pat_str, row[9], row[10] if row[10] else "-", rel_str), tags=(row[0],))

def actualizar_todas_tablas():
    actualizar_tabla(tree_deseado, "Programa Deseado")
    actualizar_tabla(tree_complementario, "Programa Complementario")
    actualizar_tabla(tree_lujo, "Programa de Lujo")

def actualizar_vista_proyecto():
    nombre = var_nombre.get() if var_nombre.get() else "Sin Proyecto"
    texto_nombre.config(text=f"Soma // {nombre}")
    
    ubicacion_partes = []
    if var_ubicacion_mundial.get(): ubicacion_partes.append(var_ubicacion_mundial.get())
    if var_ubicacion_nacional.get(): ubicacion_partes.append(var_ubicacion_nacional.get())
    if var_ubicacion_estatal.get(): ubicacion_partes.append(var_ubicacion_estatal.get())
    if var_ubicacion_local.get(): ubicacion_partes.append(var_ubicacion_local.get())
    if var_ubicacion_urbano.get(): ubicacion_partes.append(var_ubicacion_urbano.get())
    
    texto_info.config(text=f"Cliente: {var_cliente.get() if var_cliente.get() else '--'} | Tipo: {var_tipo.get() if var_tipo.get() else '--'} | Objetivo: {var_objetivo.get() if var_objetivo.get() else '--'} | Presupuesto: ${var_presupuesto.get() if var_presupuesto.get() else '--'} | Terreno: {var_superficie_terreno.get() if var_superficie_terreno.get() else '--'}m2 | Ubicacion: {' / '.join(ubicacion_partes) if ubicacion_partes else '--'}")

def exportar_pdf():
    if not proyecto_actual_id:
        messagebox.showwarning("Sin datos", "No hay proyecto cargado")
        return
    
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not filename:
        return
    
    try:
        doc = SimpleDocTemplate(filename, pagesize=landscape(A4))
        story = []
        styles = getSampleStyleSheet()
        
        color_accent = colors.HexColor('#bc4b21')
        color_gris = colors.HexColor('#E8E0D3')
        color_borde = colors.HexColor('#CCCCCC')
        color_fondo_tabla = colors.HexColor('#FAFAFA')
        
        titulo_style = ParagraphStyle('Titulo', parent=styles['Heading1'], fontSize=16, textColor=color_accent, spaceAfter=20)
        subtitulo_style = ParagraphStyle('Subtitulo', parent=styles['Heading2'], fontSize=12, textColor=colors.black, spaceAfter=10)
        
        story.append(Paragraph(f"{var_nombre.get()}", titulo_style))
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Datos del Proyecto", subtitulo_style))
        
        datos_proyecto = [
            ["Cliente:", var_cliente.get() if var_cliente.get() else "-"],
            ["Tipo de Edificio:", var_tipo.get() if var_tipo.get() else "-"],
            ["Objetivo:", var_objetivo.get() if var_objetivo.get() else "-"],
            ["Presupuesto:", f"${var_presupuesto.get()}" if var_presupuesto.get() else "-"],
            ["Terreno:", f"{var_superficie_terreno.get()} m2" if var_superficie_terreno.get() else "-"]
        ]
        tabla_datos = Table(datos_proyecto, colWidths=[2*inch, 4*inch])
        tabla_datos.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), 'Helvetica'), ('FONTSIZE', (0,0), (-1,-1), 9), ('BACKGROUND', (0,0), (0,-1), color_gris), ('GRID', (0,0), (-1,-1), 0.5, color_borde)]))
        story.append(tabla_datos)
        story.append(Spacer(1, 0.3*inch))
        
        for tipo in ["Programa Deseado", "Programa Complementario", "Programa de Lujo"]:
            cursor = conn.cursor()
            cursor.execute("SELECT espacio, area, horario_inicio, horario_fin, zona, mobiliario, acontecimientos, patrones_espaciales, usuarios, clave, relacion_directa FROM espacios WHERE proyecto_id=? AND tipo_programa=?", (proyecto_actual_id, tipo))
            espacios = cursor.fetchall()
            if espacios:
                story.append(Paragraph(tipo.upper(), subtitulo_style))
                tabla_espacios = [["Espacio", "Area", "Horario", "Zona", "Mobiliario", "Acontecimientos", "Patrones", "Usuarios", "Clave", "Relacion"]]
                for esp in espacios:
                    try:
                        if esp[2] and esp[3]:
                            horario = f"{esp[2]}\n{esp[3]}"
                        else:
                            horario = "-"
                        mob = "\n".join(json.loads(esp[5])) if esp[5] else "-"
                        acon = "\n".join(json.loads(esp[6])) if esp[6] else "-"
                        pat = "\n".join(json.loads(esp[7])) if esp[7] else "-"
                        rel = "\n".join(json.loads(esp[10])) if esp[10] else "-"
                    except:
                        mob = acon = pat = rel = "-"
                        horario = "-"
                    tabla_espacios.append([esp[0] or "-", f"{esp[1]} m2", horario, f"{esp[4]} ({descripcion_zona.get(esp[4], '')})", mob, acon, pat, str(esp[8]), esp[9] or "-", rel])
                col_widths = [0.9*inch, 0.5*inch, 0.6*inch, 0.8*inch, 1.0*inch, 1.0*inch, 1.0*inch, 0.5*inch, 0.6*inch, 0.9*inch]
                tabla = Table(tabla_espacios, colWidths=col_widths, repeatRows=1)
                tabla.setStyle(TableStyle([('FONTNAME', (0,0), (-1,-1), 'Helvetica'), ('FONTSIZE', (0,0), (-1,-1), 6), ('BACKGROUND', (0,0), (-1,0), color_accent), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('BACKGROUND', (0,1), (-1,-1), color_fondo_tabla), ('GRID', (0,0), (-1,-1), 0.3, color_borde), ('VALIGN', (0,0), (-1,-1), 'TOP')]))
                story.append(tabla)
                story.append(Spacer(1, 0.15*inch))
        
        doc.build(story)
        messagebox.showinfo("Exito", f"PDF guardado en:\n{filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar PDF:\n{str(e)}")

# =========================== INTERFAZ PRINCIPAL ===========================
root = tk.Tk()
root.title("Soma // Architectural Praxis System")
root.geometry("1700x900")
root.configure(bg=COLORS['bg'])

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background=COLORS['tree_bg'], foreground=COLORS['tree_fg'], 
                fieldbackground=COLORS['tree_bg'], bordercolor=COLORS['border'], borderwidth=0, rowheight=70)
style.configure("Treeview.Heading", background=COLORS['bg'], foreground=COLORS['accent'], 
                font=("JetBrains Mono", 8, "bold"))
style.map('Treeview', background=[('selected', COLORS['tree_selected'])])

var_nombre = tk.StringVar()
var_ubicacion_mundial = tk.StringVar()
var_ubicacion_nacional = tk.StringVar()
var_ubicacion_estatal = tk.StringVar()
var_ubicacion_local = tk.StringVar()
var_ubicacion_urbano = tk.StringVar()
var_cliente = tk.StringVar()
var_tipo = tk.StringVar()
var_objetivo = tk.StringVar()
var_presupuesto = tk.StringVar()
var_superficie_terreno = tk.StringVar()

# Panel Superior
panel_superior = Frame(root, bg=COLORS['card_bg'], height=80)
panel_superior.pack(fill="x", padx=10, pady=10)
panel_superior.pack_propagate(False)
Label(panel_superior, text="SOMA", bg=COLORS['card_bg'], font=("Unbounded", 18, "bold"), fg=COLORS['accent']).pack(side="left", padx=20, pady=15)
texto_nombre = Label(panel_superior, text="Soma // Sin Proyecto", bg=COLORS['card_bg'], font=("Unbounded", 11, "bold"), fg=COLORS['paper'])
texto_nombre.pack(side="left", padx=20, pady=15)
texto_info = Label(panel_superior, text="", bg=COLORS['card_bg'], font=("JetBrains Mono", 8), fg=COLORS['paper'])
texto_info.pack(side="left", padx=20, pady=15)

# Panel Izquierdo
panel_izquierdo = Frame(root, bg=COLORS['bg'], width=300)
panel_izquierdo.pack(side="left", fill="y", padx=10, pady=5)
panel_izquierdo.pack_propagate(False)

canvas_izq = Canvas(panel_izquierdo, bg=COLORS['bg'], highlightthickness=0)
scroll_izq = Scrollbar(panel_izquierdo, orient="vertical", command=canvas_izq.yview)
frame_botones = Frame(canvas_izq, bg=COLORS['bg'])
frame_botones.bind("<Configure>", lambda e: canvas_izq.configure(scrollregion=canvas_izq.bbox("all")))
canvas_izq.create_window((0, 0), window=frame_botones, anchor="nw")
canvas_izq.configure(yscrollcommand=scroll_izq.set)
canvas_izq.pack(side="left", fill="both", expand=True)
scroll_izq.pack(side="right", fill="y")

Label(frame_botones, text="DATOS DEL PROYECTO", bg=COLORS['bg'], font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(anchor="w", pady=(5, 5), padx=10)
Button(frame_botones, text="Nuevo Proyecto", command=nuevo_proyecto_action, bg=COLORS['accent'], fg='white', font=("Unbounded", 9, "bold"), relief="flat", padx=10, pady=5).pack(fill="x", pady=2, padx=10)
btn_cliente = Button(frame_botones, text="Cliente", command=lambda: hacer_pregunta("cliente", var_cliente.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8), relief="flat", padx=10, pady=5); btn_cliente.pack(fill="x", pady=2, padx=10)
btn_tipo = Button(frame_botones, text="Tipo", command=lambda: hacer_pregunta("tipo_edificio", var_tipo.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8), relief="flat", padx=10, pady=5); btn_tipo.pack(fill="x", pady=2, padx=10)
btn_objetivo = Button(frame_botones, text="Objetivo", command=lambda: hacer_pregunta("objetivo", var_objetivo.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8), relief="flat", padx=10, pady=5); btn_objetivo.pack(fill="x", pady=2, padx=10)
btn_presupuesto = Button(frame_botones, text="Presupuesto", command=lambda: hacer_pregunta("presupuesto", var_presupuesto.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8), relief="flat", padx=10, pady=5); btn_presupuesto.pack(fill="x", pady=2, padx=10)
btn_terreno = Button(frame_botones, text="Superficie Terreno", command=lambda: hacer_pregunta("superficie_terreno", var_superficie_terreno.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8), relief="flat", padx=10, pady=5); btn_terreno.pack(fill="x", pady=2, padx=10)

Label(frame_botones, text="UBICACION", bg=COLORS['bg'], font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(anchor="w", pady=(10, 5), padx=10)
f_ubi = Frame(frame_botones, bg=COLORS['bg']); f_ubi.pack(fill="x", padx=10, pady=2)
Button(f_ubi, text="Mundial", command=lambda: hacer_pregunta("ubicacion_mundial", var_ubicacion_mundial.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=4).pack(side="left", padx=2, expand=True, fill="x")
Button(f_ubi, text="Nacional", command=lambda: hacer_pregunta("ubicacion_nacional", var_ubicacion_nacional.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=4).pack(side="left", padx=2, expand=True, fill="x")
f_ubi2 = Frame(frame_botones, bg=COLORS['bg']); f_ubi2.pack(fill="x", padx=10, pady=2)
Button(f_ubi2, text="Estatal", command=lambda: hacer_pregunta("ubicacion_estatal", var_ubicacion_estatal.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=4).pack(side="left", padx=2, expand=True, fill="x")
Button(f_ubi2, text="Local", command=lambda: hacer_pregunta("ubicacion_local", var_ubicacion_local.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=4).pack(side="left", padx=2, expand=True, fill="x")
Button(f_ubi2, text="Urbano", command=lambda: hacer_pregunta("ubicacion_urbano", var_ubicacion_urbano.get()), bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=4).pack(side="left", padx=2, expand=True, fill="x")

Label(frame_botones, text="PROGRAMAS", bg=COLORS['bg'], font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(anchor="w", pady=(10, 5), padx=10)
Button(frame_botones, text="Deseado", command=lambda: nuevo_espacio("Programa Deseado"), bg=COLORS['deseado'], fg='white', font=("Unbounded", 9, "bold"), relief="flat", padx=10, pady=5).pack(fill="x", pady=2, padx=10)
Button(frame_botones, text="Complementario", command=lambda: nuevo_espacio("Programa Complementario"), bg=COLORS['complementario'], fg='white', font=("Unbounded", 9, "bold"), relief="flat", padx=10, pady=5).pack(fill="x", pady=2, padx=10)
Button(frame_botones, text="Lujo", command=lambda: nuevo_espacio("Programa de Lujo"), bg=COLORS['lujo'], fg='#2a2a2a', font=("Unbounded", 9, "bold"), relief="flat", padx=10, pady=5).pack(fill="x", pady=2, padx=10)

Label(frame_botones, text="ACCIONES", bg=COLORS['bg'], font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(anchor="w", pady=(10, 5), padx=10)
f_acc = Frame(frame_botones, bg=COLORS['bg']); f_acc.pack(fill="x", padx=10, pady=2)
Button(f_acc, text="Guardar", command=guardar_proyecto, bg=COLORS['accent'], fg='white', font=("Unbounded", 8, "bold"), relief="flat", padx=5, pady=5).pack(side="left", padx=2, expand=True, fill="x")
Button(f_acc, text="Exportar PDF", command=exportar_pdf, bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=5).pack(side="left", padx=2, expand=True, fill="x")
Button(f_acc, text="Eliminar", command=eliminar_proyecto, bg=COLORS['card_bg'], fg=COLORS['paper'], font=("JetBrains Mono", 7), relief="flat", padx=5, pady=5).pack(side="left", padx=2, expand=True, fill="x")

# Panel Central
panel_central = Frame(root, bg=COLORS['bg'])
panel_central.pack(side="left", fill="both", expand=True, padx=10, pady=5)

canvas_central = Canvas(panel_central, bg=COLORS['bg'], highlightthickness=0)
scroll_central = Scrollbar(panel_central, orient="vertical", command=canvas_central.yview)
frame_tablas = Frame(canvas_central, bg=COLORS['bg'])
frame_tablas.bind("<Configure>", lambda e: canvas_central.configure(scrollregion=canvas_central.bbox("all")))
canvas_central.create_window((0, 0), window=frame_tablas, anchor="nw")
canvas_central.configure(yscrollcommand=scroll_central.set)
canvas_central.pack(side="left", fill="both", expand=True)
scroll_central.pack(side="right", fill="y")

def crear_tabla(parent, titulo, color):
    frame = LabelFrame(parent, text=titulo, bg=COLORS['bg'], fg=color, font=("Unbounded", 9, "bold"), bd=1, relief="solid")
    frame.pack(fill="both", expand=True, pady=5)
    
    frame_tabla = Frame(frame, bg=COLORS['bg'])
    frame_tabla.pack(fill="both", expand=True)
    
    columns = ("Espacio", "Area", "Horario", "Zona", "Mobiliario", "Acontecimientos", "Patrones", "Usuarios", "Clave", "Relacion")
    tree = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=4)
    anchos = [90, 45, 70, 85, 100, 100, 100, 45, 55, 90]
    for col, ancho in zip(columns, anchos):
        tree.heading(col, text=col)
        tree.column(col, width=ancho, minwidth=ancho)
    
    scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll_y.set)
    scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scroll_x.set)
    
    tree.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")
    
    def on_double_click(event):
        seleccion = tree.selection()
        if seleccion:
            espacio_id = tree.item(seleccion[0], "tags")[0]
            editar_espacio(espacio_id, titulo.replace("★ ", "").replace("◇ ", "").replace("◆ ", ""))
    tree.bind("<Double-1>", on_double_click)
    return tree

tree_deseado = crear_tabla(frame_tablas, "★ Programa Deseado", COLORS['deseado'])
tree_complementario = crear_tabla(frame_tablas, "◇ Programa Complementario", COLORS['complementario'])
tree_lujo = crear_tabla(frame_tablas, "◆ Programa de Lujo", COLORS['lujo'])

# Panel Derecho
panel_derecho = Frame(root, bg=COLORS['card_bg'], width=240)
panel_derecho.pack(side="left", fill="y", padx=10, pady=5)
panel_derecho.pack_propagate(False)

Label(panel_derecho, text="PROYECTOS", bg=COLORS['card_bg'], font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(pady=(8, 5))

frame_lista = Frame(panel_derecho, bg=COLORS['card_bg'])
frame_lista.pack(fill="both", expand=True, padx=5, pady=5)

lista_proyectos = ttk.Treeview(frame_lista, columns=("Nombre", "Fecha"), show="headings", height=20)
lista_proyectos.heading("Nombre", text="Nombre")
lista_proyectos.heading("Fecha", text="Fecha")
lista_proyectos.column("Nombre", width=140)
lista_proyectos.column("Fecha", width=65)

scroll_lista = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_proyectos.yview)
lista_proyectos.configure(yscrollcommand=scroll_lista.set)
lista_proyectos.pack(side="left", fill="both", expand=True)
scroll_lista.pack(side="right", fill="y")

lista_proyectos.bind("<Double-1>", abrir_proyecto_seleccionado)

actualizar_todas_tablas()
actualizar_lista_proyectos()

root.mainloop()