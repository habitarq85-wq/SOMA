# PROTOCOLO: REPRESENTACIÓN INTEGRAL — DOSSIER EDITORIAL
## Bloque 2 — Taller SOMA (Operación) | Sección 7 del PROCESO DE DISEÑO 2.0
## Referencia: Items 7.1 a 7.2

**Qué es:** Compilación del proyecto en un dossier editorial de calidad revista,
que unifica memoria descriptiva, renders, planos y conceptos de diseño.

**Entrada:** Documento de Concepto + Modelo 3D + Renders + Planos.

**Salida:** Dossier editorial en HTML/PDF con identidad visual SOMA.

**Principio rector:** El dossier es la **historia del proyecto** — el cliente debe
entender el proyecto sin necesidad de leer planos.

---

```
[HUMANO→AI] 7.1 Documento de Entrega HTML (P2.0 ref: 7.1)
─────────────────────────────────
INPUT:  6.1-6.2 Planos + 5.11 Renders + 4.1 Manifiesto + 4.2 Idea
OPERA:  Integrar entregables en documento HTML con identidad SOMA:
        portada, manifiesto, carrusel de planos, carrusel de
        perspectivas, animaciones web sutiles
OUTPUT: Documento HTML de entrega (autocontenido, imprimible a PDF)
PROC:   HUMANO→AI
```

```
[OUT] 7.2 Documento de Entrega PDF (P2.0 ref: 7.2)
─────────────────────────────────
INPUT:  7.1 HTML + 6.1-6.2 Planos + 5.11 Renders
OPERA:  Compilar plantas, alzados y perspectivas en PDF
OUTPUT: PDF de entrega (listo para imprimir/enviar)
PROC:   AI (generación de PDF)
```

---

## Estructura del Dossier

### Portada
- Render principal a página completa
- Logotipo SOMA (esquina superior izquierda)
- Título: "Proyecto Arquitectónico [Nombre]"
- Subtítulo: paquete y fecha
- Frase del proyecto (Idea Matriz)
- Créditos: "SOMA Taller Virtual de Arquitectura · Juan José Piña May"

### Ficha Técnica
- Nombre, cliente, ubicación, tipo
- Área de terreno y construida
- Paquete contratado, fecha, No. proyecto

### Memoria Descriptiva (1 página, ≤300 palabras)
- Idea Matriz del proyecto
- Mensaje arquitectónico
- Partido arquitectónico
- Estrategias bioclimáticas principales
- Materialidad dominante

### Planta de Conjunto (1 página)
- Escala 1:100 ó 1:75
- Implantación, cubiertas, áreas exteriores, vegetación
- Accesos, norte, escala gráfica

### Plantas Arquitectónicas (1 página cada una)
- Por nivel, escala 1:75
- Amuebladas, con nombres de espacios y áreas

### Cortes y Alzados (2 páginas)
- Corte longitudinal y transversal (1:75)
- Alzados principales (1:75)

### Renders y Perspectivas (2-4 páginas)
- Exterior general (página completa)
- Fachada principal
- Interior espacio principal
- Interior cocina/baño (Integral+)
- Zona exterior (Integral+)

### Estrategias Bioclimáticas (1 página)
- Diagrama de estrategias seleccionadas
- Triada recomendada para Mérida

### Criterio de Materiales y Acabados (1 página)
- Moodboard de materiales
- Tabla de acabados por espacio

---

## Especificaciones de Diseño Visual

| Elemento | Especificación |
|----------|---------------|
| Fondo | #0a0a0a (negro SOMA) |
| Acento | #d45e2c (naranja SOMA) |
| Fuente títulos | Unbounded, sans-serif |
| Fuente textos | JetBrains Mono, monospace |
| Grid | 12 columnas, gutter 20px |
| Animación | Intersection Observer (scroll-reveal) |

### @media print
- Fondo blanco para ahorrar tinta
- Tipografía serif para cuerpo de texto
- Imágenes en escala de grises (opcional)

---

## Salida de la Representación

1. `dossier_[proyecto].html` — documento interactivo
2. `dossier_[proyecto].pdf` — versión imprimible

---

## FUENTES

- Arnheim, R. (1969). *Visual Thinking.*
- Ching, F. (2015). *Architectural Graphics.*
