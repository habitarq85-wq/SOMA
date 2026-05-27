# PROTOCOLO: REPRESENTACIÓN INTEGRAL (DOSSIER EDITORIAL)
## Bloque 2 — Taller SOMA (Operación) | Etapa 7 del Ciclo

### ¿Qué es la Representación Integral?

Es la compilación del proyecto en un dossier editorial de calidad revista, que unifica la memoria descriptiva, los renders, los planos y los conceptos de diseño en un solo documento presentable al cliente y al portafolio.

**Entrada:** Documento de Concepto + Modelo 3D + Renders (de Etapas 4, 5, 6).
**Salida:** Dossier editorial en HTML/PDF con identidad visual SOMA.

### Principio rector

El dossier no es un instructivo técnico — es la **historia del proyecto** contada con imágenes, textos cortos y diseño editorial. El cliente debe entender el proyecto sin necesidad de leer planos.

---

## 1. ESTRUCTURA DEL DOSSIER

### 1.1 Portada
(Fuente: editorial design principles — grid systems, typographic hierarchy)

- Render principal del proyecto (vista más impactante) a página completa
- Logotipo SOMA (esquina superior izquierda)
- Título del proyecto: "Proyecto Arquitectónico [Nombre del Cliente]"
- Subtítulo: tipo de paquete y fecha
- Frase del proyecto (Idea Matriz de la Conceptualización)
- Créditos: "SOMA Taller Virtual de Arquitectura · Juan José Piña May"

### 1.2 Ficha Técnica
- Nombre del proyecto
- Cliente
- Ubicación
- Tipo de proyecto
- Área de terreno
- Área construida
- Paquete contratado
- Fecha
- Número de proyecto interno (SOMA-XXXX)

### 1.3 Memoria Descriptiva (1 página)
(Fuente: PROTOCOLO_CONCEPTUALIZACION.md — Documento de Concepto)

En no más de 300 palabras:
- Idea Matriz del proyecto
- Mensaje arquitectónico (qué dice el proyecto)
- Partido arquitectónico (cómo se resolvió la implantación)
- Estrategias bioclimáticas principales
- Materialidad dominante

### 1.4 Planta de Conjunto (1 página)
- Planta de techos/implantación
- Escala gráfica + norte
- Nomenclatura de zonas SOMA (Social, Descanso, Operativa, Soporte, Transición)

### 1.5 Galería de Renders (3–6 páginas)
(Fuente: PROTOCOLO_VISUALIZACION.md — vistas obligatorias)

Cada render a página completa o doble página con:
- Leyenda corta del espacio (ej: "Sala-estar · La luz del poniente tamizada por la celosía")
- Material predominante del espacio
- Pie de foto con nombre de archivo

### 1.6 Planos Arquitectónicos (2–4 páginas)
- Plantas arquitectónicas (amuebladas)
- Cortes significativos (mínimo 2)
- Alzados principales
- Escalas: 1:100 o 1:75 (según tamaño del proyecto)

### 1.7 Moodboard de Acabados (1 página, solo Integral+)
- Muestras de materiales propuestos
- Nombre del material, proveedor, código de color
- Foto de referencia de cada material

### 1.8 Esquema de Pagos y Vigencia (1 página, misma info que cotización)
- Tabla 30/40/30
- Nota de vigencia de 30 días
- Aclaratoria: "Este documento cubre el diseño arquitectónico. La construcción está a cargo de un tercero."

### 1.9 Contraportada
- Render secundario o detalle
- Contacto: web, email, WhatsApp
- "SOMA Taller Virtual de Arquitectura"

---

## 2. PLANTILLA HTML (plantilla_dossier.html)
(Fuente: W3C Web Accessibility Initiative — w3.org/WAI/tutorials; Intersection Observer API — MDN Web Docs; CSS @media print — MDN Web Docs)

### 2.1 Tecnología
- HTML5 + CSS3 + JavaScript vanilla
- Sin frameworks (carga rápida, sin dependencias)
- Intersection Observer para efectos scroll-reveal
- `@media print` para exportación a PDF (Ctrl+P)

### 2.2 Identidad Visual (consistente con la web)
- Fondo: oscuro (#0A0A0A)
- Texto: claro (#E8E0D8)
- Acento: naranja SOMA (#bc4b21)
- Tipografía titular: Unbounded (Google Fonts)
- Tipografía de texto: JetBrains Mono (cuerpo) + Playfair Display (citas)
- Grid: sistema de 12 columnas para flexibilidad editorial

### 2.3 Efectos Interactivos
(Fuente: Intersection Observer API — developer.mozilla.org)

- Scroll-reveal: imágenes y textos aparecen al hacer scroll
- Transiciones suaves (opacity 0 → 1, translateY 20px → 0)
- Galería de renders: lightbox al hacer clic en imagen
- Navegación lateral con saltos a secciones

### 2.4 Exportación a PDF
(Fuente: CSS @media print — developer.mozilla.org)

- `@media print`: eliminar fondos oscuros (ahorrar tinta), convertir a blanco
- Ajustar saltos de página con `page-break-after`
- Ocultar elementos interactivos (botones, navegación)
- Configurar márgenes de impresión: 1.5 cm
- Resolución: 300 DPI para imágenes

### 2.5 Archivo de template
La plantilla base `plantilla_dossier.html` debe estar en:
```
metodologia/Bloque 2 - Taller SOMA (OPERACION)/03 Diseño/dossier/
```

Con la siguiente estructura:
```
dossier/
├── plantilla_dossier.html    ← Template parametrizable
├── css/
│   └── estilo_dossier.css    ← Estilos del dossier
├── js/
│   └── dossier.js            ← Scroll-reveal, lightbox, PDF
└── img/                      ← Carpeta para imágenes del proyecto
```

---

## 3. CÓMO USAR LA PLANTILLA

1. Copiar `plantilla_dossier.html` a `proyectos/SOMA-XXXX/dossier_editorial/`
2. Editar el bloque JSON al inicio del HTML con los datos del proyecto:

```javascript
const DATOS_PROYECTO = {
  titulo: "Casa [Cliente]",
  subtitulo: "SOMA [Paquete] · [Fecha]",
  idea_matriz: "Una caja de concreto que flota sobre el jardín.",
  cliente: "Nombre del Cliente",
  ubicacion: "Mérida, Yucatán",
  tipo: "Casa Habitación",
  area_terreno: 300,
  area_construida: 200,
  paquete: "Integral",
  numero_proyecto: "SOMA-20260526-0001",
  memoria: "Texto de la memoria descriptiva...",
  materialidad: "Concreto aparente, madera de tzalam, vidrio templado...",
  renders: [
    { archivo: "SOMA-LOPEZ-AEREA-01.png", leyenda: "Vista aérea del conjunto" },
    { archivo: "SOMA-LOPEZ-FACHADA-01.png", leyenda: "Fachada principal" }
  ],
  plantas: [
    { archivo: "planta_baja.png", escala: "1:100", titulo: "Planta Baja" }
  ],
  acabados: [
    { material: "Concreto aparente", proveedor: "CEMEX", color: "#B5B0A8", imagen: "concreto.jpg" }
  ]
};
```

3. Colocar las imágenes en `img/`
4. Abrir el HTML en el navegador → verificar visualización
5. Ctrl+P → Guardar como PDF

---

## 4. CHECKLIST DE CALIDAD EDITORIAL

- [ ] ¿La portada tiene el render más impactante?
- [ ] ¿La memoria descriptiva NO excede 300 palabras?
- [ ] ¿Todos los renders tienen leyenda explicativa?
- [ ] ¿Los planos incluyen escala gráfica y norte?
- [ ] ¿El moodboard (si aplica) tiene fotos de los materiales reales?
- [ ] ¿La ortografía y redacción están correctas?
- [ ] ¿El PDF se ve bien en pantalla y en impresión?
- [ ] ¿El nombre del archivo sigue la convención: `SOMA-Dossier-[Cliente].pdf`?
- [ ] ¿Se incluyó la nota de vigencia de 30 días?

---

## 5. SALIDA DE LA REPRESENTACIÓN INTEGRAL

1. **Dossier PDF** en `proyectos/SOMA-XXXX/dossier_editorial/SOMA-Dossier-[Cliente].pdf`
2. **Archivo HTML fuente** (para modificaciones futuras)
3. **Carpeta de imágenes** optimizadas usadas en el dossier

Este dossier es el entregable principal al cliente y la entrada al portafolio.

---

## FUENTES

- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — estructura narrativa visual del proyecto, jerarquía de información en láminas.
- **Francis D.K. Ching**, *Architectural Graphics* (6th ed., 2015) — composición de láminas, tipografía técnica, organización de planos en página.
- **C. M. Deasy**, *Design Places for People* (1974) — cómo el dossier debe contar la historia del espacio para el usuario, no solo del edificio.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — integración de la memoria descriptiva con la representación gráfica, claridad comunicativa.
- **W3C Web Accessibility Initiative** (w3.org/WAI/tutorials) — alt text para imágenes, contraste, accesibilidad del documento digital.
- **Intersection Observer API** — MDN Web Docs (developer.mozilla.org) — efectos scroll-reveal.
- **Rudolf Arnheim**, *Visual Thinking* (1969) — principios de percepción visual aplicados a la composición editorial y narrativa gráfica del dossier.
- **CSS @media print** — MDN Web Docs — exportación a PDF con estilos de impresión.

---

*"Un proyecto bien contado vale más que cien renders sueltos."*
