import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.patches import Circle
import json
import pickle
import os
import sys
import numpy as np

# ================== CONFIGURACIÓN VISUAL ==================
COLORS = {
    'bg': '#0a0a0a',
    'paper': '#f4f1ee',
    'accent': '#bc4b21',
    'card_bg': '#1a1a1a',
    'border': '#2a2a2a',
    'tree_bg': '#2a2a2a',
    'tree_fg': '#f4f1ee',
    'tree_selected': '#bc4b21'
}

ZONA_COLOR = {
    1: (0.3, 0.5, 0.9, 0.8),   # Social -> Azul
    2: (0.9, 0.8, 0.2, 0.8),   # Operativa -> Amarillo
    3: (0.9, 0.3, 0.3, 0.8),   # Descanso -> Rojo
    4: (0.9, 0.5, 0.2, 0.8),   # Soporte -> Naranja
    5: (0.6, 0.2, 0.6, 0.8)    # Transición -> Púrpura
}

DESCRIPCION_ZONA = {
    1: "Social",
    2: "Operativa",
    3: "Descanso",
    4: "Soporte",
    5: "Transición"
}

class SomaGraphViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("SOMA // Graph Viewer")
        self.root.geometry("1500x850")
        self.root.configure(bg=COLORS['bg'])
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

        # Configurar estilo para la tabla de proyectos
        self.setup_treeview_style()

        self.conn = sqlite3.connect('proyectos_arquitectonicos.db')
        self.proyecto_actual_id = None
        self.todos_los_espacios = []
        self.filtro_zona_actual = None
        self.G = None
        self.pos = None
        self.dragging = False
        self.current_node = None
        self.current_circle = None
        self.current_text = None
        self.pos_cache_file = "posiciones_cache.pkl"
        
        # Almacenar objetos gráficos
        self.node_circles = {}
        self.node_texts = {}
        self.edge_lines = []

        self.setup_ui()
        self.cargar_proyectos()
        self.cargar_posiciones_cache()

    def setup_treeview_style(self):
        """Configura el estilo oscuro para el Treeview"""
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background=COLORS['tree_bg'], 
                        foreground=COLORS['tree_fg'], 
                        fieldbackground=COLORS['tree_bg'],
                        bordercolor=COLORS['border'], 
                        borderwidth=0,
                        rowheight=25)
        style.configure("Treeview.Heading", 
                        background=COLORS['card_bg'], 
                        foreground=COLORS['accent'], 
                        font=("JetBrains Mono", 9, "bold"))
        style.map('Treeview', background=[('selected', COLORS['tree_selected'])])

    def cerrar_aplicacion(self):
        try:
            self.guardar_posiciones_cache()
            if self.conn:
                self.conn.close()
            plt.close('all')
            self.root.quit()
            self.root.destroy()
            sys.exit(0)
        except:
            sys.exit(0)

    def setup_ui(self):
        # Panel izquierdo
        panel_izq = tk.Frame(self.root, bg=COLORS['bg'], width=280)
        panel_izq.pack(side="left", fill="y", padx=10, pady=10)
        panel_izq.pack_propagate(False)

        tk.Label(panel_izq, text="SOMA", bg=COLORS['bg'],
                 font=("Unbounded", 18, "bold"), fg=COLORS['accent']).pack(pady=(20, 5))
        tk.Label(panel_izq, text="Graph Viewer", bg=COLORS['bg'],
                 font=("JetBrains Mono", 10), fg=COLORS['paper']).pack(pady=(0, 20))

        tk.Frame(panel_izq, height=2, bg=COLORS['border']).pack(fill="x", pady=10, padx=10)

        # Filtro por zona
        tk.Label(panel_izq, text="Filtrar por Zona", bg=COLORS['bg'],
                 font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(anchor="w", padx=10, pady=(0, 5))

        self.filtro_var = tk.StringVar(value="Todas")
        filtros = ["Todas"] + [f"{num} - {nombre}" for num, nombre in DESCRIPCION_ZONA.items()]
        combo_filtro = ttk.Combobox(panel_izq, textvariable=self.filtro_var, values=filtros,
                                    state="readonly", font=("JetBrains Mono", 9))
        combo_filtro.pack(fill="x", padx=10, pady=5)
        combo_filtro.bind("<<ComboboxSelected>>", self.aplicar_filtro)

        tk.Frame(panel_izq, height=10, bg=COLORS['bg']).pack()

        # Botón resetear posiciones
        tk.Button(panel_izq, text="Resetear Posiciones", command=self.resetear_posiciones,
                  bg=COLORS['card_bg'], fg=COLORS['paper'], font=("Unbounded", 9, "bold"),
                  relief="flat", padx=10, pady=6).pack(fill="x", pady=5, padx=10)

        # Botón guardar diagrama (PDF)
        tk.Button(panel_izq, text="📷 Guardar Diagrama", command=self.guardar_diagrama_pdf,
                  bg=COLORS['accent'], fg='white', font=("Unbounded", 9, "bold"),
                  relief="flat", padx=10, pady=6).pack(fill="x", pady=10, padx=10)

        tk.Frame(panel_izq, height=10, bg=COLORS['bg']).pack()

        # Instrucciones
        tk.Label(panel_izq, text="💡 Instrucciones:", bg=COLORS['bg'],
                 font=("Unbounded", 8, "bold"), fg=COLORS['accent']).pack(anchor="w", padx=10, pady=(15, 5))
        tk.Label(panel_izq, text="• Selecciona un proyecto\n  de la lista derecha\n• Elige filtro por zona\n• Arrastra nodos para\n  reubicarlos\n• Usa zoom/pan de la barra",
                 bg=COLORS['bg'], fg=COLORS['paper'], font=("JetBrains Mono", 8),
                 justify="left").pack(anchor="w", padx=10)

        # Panel derecho (lista de proyectos) - Fondo oscuro
        panel_der = tk.Frame(self.root, bg=COLORS['card_bg'], width=260)
        panel_der.pack(side="right", fill="y", padx=10, pady=10)
        panel_der.pack_propagate(False)

        tk.Label(panel_der, text="Proyectos", bg=COLORS['card_bg'],
                 font=("Unbounded", 9, "bold"), fg=COLORS['accent']).pack(pady=(10, 5))

        frame_lista = tk.Frame(panel_der, bg=COLORS['card_bg'])
        frame_lista.pack(fill="both", expand=True, padx=5, pady=5)

        # Treeview con estilo oscuro
        self.tree_proyectos = ttk.Treeview(frame_lista, columns=("Nombre", "Fecha"), show="headings", height=20)
        self.tree_proyectos.heading("Nombre", text="Nombre")
        self.tree_proyectos.heading("Fecha", text="Fecha")
        self.tree_proyectos.column("Nombre", width=150)
        self.tree_proyectos.column("Fecha", width=70)

        scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree_proyectos.yview)
        self.tree_proyectos.configure(yscrollcommand=scroll.set)
        
        self.tree_proyectos.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tree_proyectos.bind("<<TreeviewSelect>>", self.on_proyecto_seleccionado)

        # Panel central
        panel_central = tk.Frame(self.root, bg=COLORS['bg'])
        panel_central.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(9, 7), facecolor=COLORS['bg'])
        self.ax.set_facecolor(COLORS['bg'])
        self.canvas = FigureCanvasTkAgg(self.fig, master=panel_central)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Conectar eventos
        self.cid_press = self.canvas.mpl_connect('button_press_event', self.on_press)
        self.cid_release = self.canvas.mpl_connect('button_release_event', self.on_release)
        self.cid_motion = self.canvas.mpl_connect('motion_notify_event', self.on_motion)

        toolbar = NavigationToolbar2Tk(self.canvas, panel_central)
        toolbar.update()
        toolbar.pack(side="bottom", fill="x")

    def guardar_diagrama_pdf(self):
        """Guarda el diagrama actual como PDF sin preguntar"""
        if not self.G or len(self.G.nodes) == 0:
            messagebox.showwarning("Sin diagrama", "No hay ningún diagrama generado para guardar.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", 
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar diagrama como"
        )
        if filename:
            self.fig.savefig(filename, format='pdf', bbox_inches='tight', facecolor=COLORS['bg'])
            messagebox.showinfo("Exportar", f"Diagrama guardado en:\n{filename}")

    def cargar_posiciones_cache(self):
        if os.path.exists(self.pos_cache_file):
            try:
                with open(self.pos_cache_file, 'rb') as f:
                    self.pos_cache = pickle.load(f)
            except:
                self.pos_cache = {}
        else:
            self.pos_cache = {}

    def guardar_posiciones_cache(self):
        if self.pos is not None and self.proyecto_actual_id and self.filtro_zona_actual is not None:
            clave_cache = f"proyecto_{self.proyecto_actual_id}_filtro_{self.filtro_zona_actual}"
            pos_serializable = {node: (float(x), float(y)) for node, (x, y) in self.pos.items()}
            self.pos_cache[clave_cache] = pos_serializable
            with open(self.pos_cache_file, 'wb') as f:
                pickle.dump(self.pos_cache, f)

    def cargar_posiciones_guardadas(self):
        if self.proyecto_actual_id and self.G and self.filtro_zona_actual is not None:
            clave_cache = f"proyecto_{self.proyecto_actual_id}_filtro_{self.filtro_zona_actual}"
            if clave_cache in self.pos_cache:
                pos_guardadas = self.pos_cache[clave_cache]
                self.pos = {node: pos_guardadas[node] for node in pos_guardadas if node in self.G.nodes}
                return True
        return False

    def resetear_posiciones(self):
        if self.G and len(self.G.nodes) > 0:
            self.pos = nx.spring_layout(self.G, k=2.5, seed=42, iterations=60)
            self.guardar_posiciones_cache()
            self.dibujar_grafo_interactivo()
            messagebox.showinfo("Posiciones", "Posiciones restablecidas al layout automático")

    def on_press(self, event):
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return
        
        for node, circle in self.node_circles.items():
            dx = event.xdata - circle.center[0]
            dy = event.ydata - circle.center[1]
            dist = np.sqrt(dx*dx + dy*dy)
            if dist < circle.radius:
                self.dragging = True
                self.current_node = node
                self.current_circle = circle
                self.current_text = self.node_texts.get(node)
                break

    def on_motion(self, event):
        if self.dragging and self.current_node and event.inaxes == self.ax:
            if event.xdata is not None and event.ydata is not None:
                self.pos[self.current_node] = (event.xdata, event.ydata)
                
                if self.current_circle:
                    self.current_circle.center = (event.xdata, event.ydata)
                
                if self.current_text:
                    self.current_text.set_position((event.xdata, event.ydata))
                
                self.actualizar_edges_nodo(self.current_node)
                self.canvas.draw_idle()

    def actualizar_edges_nodo(self, nodo):
        for u, v, line in self.edge_lines:
            if u == nodo or v == nodo:
                x1, y1 = self.pos[u]
                x2, y2 = self.pos[v]
                line.set_data([x1, x2], [y1, y2])

    def on_release(self, event):
        if self.dragging:
            self.dragging = False
            self.guardar_posiciones_cache()
            self.current_node = None
            self.current_circle = None
            self.current_text = None

    def cargar_proyectos(self):
        for item in self.tree_proyectos.get_children():
            self.tree_proyectos.delete(item)
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nombre_proyecto, fecha_modificacion FROM proyectos ORDER BY fecha_modificacion DESC")
        for row in cursor.fetchall():
            fecha = row[2][:10] if row[2] else ""
            self.tree_proyectos.insert("", "end", iid=str(row[0]), values=(row[1], fecha))

    def on_proyecto_seleccionado(self, event):
        seleccion = self.tree_proyectos.selection()
        if seleccion:
            self.proyecto_actual_id = int(seleccion[0])
            self.cargar_espacios_proyecto()
            self.generar_diagrama()

    def cargar_espacios_proyecto(self):
        if not self.proyecto_actual_id:
            self.todos_los_espacios = []
            return
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT espacio, area, zona, clave, relacion_directa
            FROM espacios
            WHERE proyecto_id = ?
        ''', (self.proyecto_actual_id,))
        self.todos_los_espacios = cursor.fetchall()

    def aplicar_filtro(self, event=None):
        self.generar_diagrama()

    def generar_diagrama(self):
        if self.proyecto_actual_id is None:
            return

        if not self.todos_los_espacios:
            messagebox.showwarning("Proyecto Vacío", "Este proyecto no tiene espacios registrados.\nAgrega espacios en SOMA primero.")
            return

        filtro_texto = self.filtro_var.get()
        if filtro_texto == "Todas":
            self.filtro_zona_actual = None
        else:
            zona_num = int(filtro_texto.split(" - ")[0])
            self.filtro_zona_actual = zona_num

        if self.filtro_zona_actual is not None:
            espacios_filtrados = [e for e in self.todos_los_espacios if e[2] == self.filtro_zona_actual]
        else:
            espacios_filtrados = self.todos_los_espacios

        if not espacios_filtrados:
            messagebox.showinfo("Sin datos", f"No hay espacios en la zona {filtro_texto}.")
            return

        # Construir grafo
        self.G = nx.Graph()
        self.datos_nodos = {}
        nodos_filtrados = set()
        
        for espacio, area, zona, clave, relacion_json in espacios_filtrados:
            if not clave:
                continue
            nodos_filtrados.add(clave)

        # Calcular área máxima y mínima para escalar tamaños relativos
        areas = []
        for espacio, area, zona, clave, relacion_json in espacios_filtrados:
            if not clave:
                continue
            area_val = float(area) if area and area > 0 else 30
            areas.append(area_val)
        
        if areas:
            area_min = min(areas)
            area_max = max(areas)
        else:
            area_min = area_max = 30

        for espacio, area, zona, clave, relacion_json in espacios_filtrados:
            if not clave:
                continue
            nombre = espacio if espacio else "?"
            etiqueta = f"{clave}\n{nombre}"
            area_val = float(area) if area and area > 0 else 30
            
            # Escala proporcional reducida 20%
            if area_max > area_min:
                proporcion = (area_val - area_min) / (area_max - area_min)
                size_visual = 320 + (proporcion * 640)
            else:
                size_visual = 480
            
            zona_int = int(zona) if zona else 1
            color = ZONA_COLOR.get(zona_int, (0.5, 0.5, 0.5, 0.8))
            
            radius = (size_visual ** 0.5) / 28
            
            self.datos_nodos[clave] = {
                'size': size_visual, 
                'color': color, 
                'label': etiqueta,
                'radius': radius,
                'area': area_val
            }
            self.G.add_node(clave)

        for espacio, area, zona, clave, relacion_json in espacios_filtrados:
            if not clave or not relacion_json:
                continue
            try:
                relaciones = json.loads(relacion_json)
                for rel in relaciones:
                    if rel and rel != clave and rel in nodos_filtrados:
                        self.G.add_edge(clave, rel)
            except:
                pass

        # Generar layout automático si no hay posiciones guardadas
        if not self.cargar_posiciones_guardadas():
            if len(self.G.nodes) > 0:
                self.pos = nx.spring_layout(self.G, k=2.5, seed=42, iterations=60)
            else:
                self.pos = {}

        self.dibujar_grafo_interactivo()

    def dibujar_grafo_interactivo(self):
        """Dibuja el grafo con círculos reducidos un 20%"""
        self.ax.clear()
        self.node_circles = {}
        self.node_texts = {}
        self.edge_lines = []

        if len(self.G.nodes) == 0:
            self.ax.text(0.5, 0.5, "No hay relaciones para mostrar\ncon este filtro", 
                         transform=self.ax.transAxes, ha='center', va='center',
                         color=COLORS['paper'], fontsize=12, fontfamily='monospace')
            self.canvas.draw()
            return

        # Dibujar aristas
        for u, v in self.G.edges():
            if u in self.pos and v in self.pos:
                x1, y1 = self.pos[u]
                x2, y2 = self.pos[v]
                line, = self.ax.plot([x1, x2], [y1, y2], color=COLORS['paper'], 
                                     linewidth=1.5, alpha=0.5, solid_capstyle='round')
                self.edge_lines.append((u, v, line))

        # Dibujar nodos como círculos individuales
        for node in self.G.nodes():
            x, y = self.pos[node]
            radius = self.datos_nodos[node]['radius']
            color = self.datos_nodos[node]['color']
            
            circle = Circle((x, y), radius=radius, facecolor=color, 
                           edgecolor='white', linewidth=1.2, alpha=0.85, zorder=2)
            self.ax.add_patch(circle)
            self.node_circles[node] = circle
            
            text = self.ax.annotate(self.datos_nodos[node]['label'], xy=(x, y), 
                                   ha='center', va='center', fontsize=8,
                                   color=COLORS['paper'], fontfamily='monospace',
                                   fontweight='bold', zorder=3)
            self.node_texts[node] = text

        # Título
        titulo = f"SOMA Graph - Proyecto ID {self.proyecto_actual_id}"
        if self.filtro_zona_actual:
            titulo += f" | Zona: {self.filtro_zona_actual} - {DESCRIPCION_ZONA[self.filtro_zona_actual]}"
        else:
            titulo += " | Todas las zonas"
        self.ax.set_title(titulo, color=COLORS['accent'], fontsize=12, fontfamily='monospace', pad=15)
        
        # Ajustar límites con márgenes adecuados
        if len(self.pos) > 0:
            todas_x = [self.pos[n][0] for n in self.G.nodes()]
            todas_y = [self.pos[n][1] for n in self.G.nodes()]
            
            max_radius = max([self.datos_nodos[n]['radius'] for n in self.G.nodes()])
            
            x_min, x_max = min(todas_x), max(todas_x)
            y_min, y_max = min(todas_y), max(todas_y)
            
            margin = max_radius * 1.8
            
            x_range = x_max - x_min
            y_range = y_max - y_min
            
            if x_range < 0.8:
                x_min -= 0.5
                x_max += 0.5
            if y_range < 0.8:
                y_min -= 0.5
                y_max += 0.5
            
            self.ax.set_xlim(x_min - margin, x_max + margin)
            self.ax.set_ylim(y_min - margin, y_max + margin)
        
        self.ax.set_facecolor(COLORS['bg'])
        self.ax.axis('off')
        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = SomaGraphViewer(root)
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)