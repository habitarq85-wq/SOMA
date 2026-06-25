# PROTOCOLO: GUÍA DE VISITA — ENTREVISTA + LEVANTAMIENTO EN CAMPO
## Bloque 2 — Taller SOMA (Operación)
## Referencia: PROCESO DE DISEÑO 2.0 — Items 2.2.1.2, 2.2.2, 2.2.4, 3.10

**Propósito:** Única visita presencial al sitio con el cliente para extraer
datos cualitativos de la entrevista + levantar datos del sitio y ambientales,
evitando una segunda visita.

**Relación con el 2.0:**
- **2.2.1.2 (Investigación)** — entrevista presencial con grabación y notas
- **2.2.2 (Datos del Sitio)** — levantamiento físico, elementos interiores y exteriores
- **2.2.4 (Datos Ambientales)** — fuentes de ruido y olores
- **3.10.1–5 (Análisis)** — transcripción, perfiles, matrices, necesidades

**Herramienta:** Guía de Visita (guia_visita.html) + App de Entrevista
(`aplicaciones_python/app_inmersion/`, puerto 5050) que graba la conversación
y estructura los datos.

**Dinámica:** Llegar al sitio, primero recorrer el terreno y entorno para
levantar datos (2.2.2, 2.2.4), luego sentarse a conversar los 6 tópicos.
El arquitecto lleva el hilo; la app registra audio continuo, tiempo por tópico
y formulario post-entrevista.

---

## Visita en Campo

```
[ACC] Visita en Campo (P2.0 ref: 1.2, 2.2.1.2)
─────────────────────────────────
INPUT:  Cita agendada + Guía de Visita (checklist sitio + ambientales +
        6 tópicos) + respuestas de Inmersión Web (10 ejes)
OPERA:  1. Recorrer el terreno y entorno — levantar datos del sitio (2.2.2)
           y ambientales (2.2.4) — fotos, croquis, notas
        2. Sentarse con el cliente — conversar los 6 tópicos con
           grabación de audio continuo
           El arquitecto toma notas de observaciones no verbales
OUTPUT: • `entrevista.wav` o `.webm` (audio en bruto)
        • `notas_campo_entrevista.txt` (observaciones)
        • `croquis_levantamiento.pdf` / `fotos_terreno/` (datos sitio)
        • `mapa_fuentes_ruido.pdf` / `mapa_fuentes_olores.pdf` (ambientales)
PROC:   HUMANO
```

---

## Checklist de Datos del Sitio (2.2.2)

### 2.2.2.1 Levantamiento Físico del Terreno
- [ ] Dimensiones y forma del terreno — medir poligonal, verificar escrituras
- [ ] Niveles y pendientes
- [ ] Tipo de suelo (observación superficial)
- [ ] Vegetación existente — ubicación, especie, diámetro aprox.
- [ ] Construcciones existentes
- [ ] Fotografiar desde múltiples ángulos
- [ ] Anotar medidas de escrituras / plano catastral

### 2.2.2.2 Elementos Interiores del Predio
- [ ] Árboles — especie, ubicación, diámetro de tronco
- [ ] Pozos, cenotes, cuerpos de agua
- [ ] Construcciones existentes — muros, pisos, losas, vanos, estado, materiales
- [ ] Acometidas: agua, drenaje, electricidad, gas

### 2.2.2.3 Elementos Exteriores (Entorno)
- [ ] Recorrer el entorno inmediato a pie
- [ ] Colindancias — alturas, materiales, usos, estado
- [ ] Vialidades — ancho, tipo, flujo, velocidad
- [ ] Banquetas — ancho, estado, materiales
- [ ] Postes — luz, teléfono, CCTV
- [ ] Alcantarillas y drenaje pluvial
- [ ] Árboles públicos

---

## Checklist de Datos Ambientales (2.2.4)

### 2.2.4.1 Fuentes de Ruido
- [ ] Vialidades cercanas — flujo, tipo vehículos, horarios críticos
- [ ] Industrias, talleres, escuelas, comercios con música
- [ ] Aires acondicionados o maquinaria en colindancias
- [ ] Registrar ubicación en croquis
- [ ] Clasificar ruido: bajo / medio / alto
- [ ] Anotar horarios críticos

### 2.2.4.2 Fuentes de Olores
- [ ] Basureros, granjas, industrias, pozos sépticos
- [ ] Quemas o fogatas
- [ ] Registrar dirección del viento
- [ ] Anotar horarios y estacionalidad
- [ ] Preguntar a vecinos (opcional)

---

## Entrevista — 6 Tópicos

### Tópico 1: La razón de estar aquí
*Objetivo: Entender el encargo, el sitio y las reglas del juego.*

- [ ] Describa el proyecto: qué quiere construir, dónde, para qué
- [ ] Terreno: dimensiones, ubicación, si ya es propietario
- [ ] Reglas: manual de construcción del fraccionamiento, restricciones conocidas
- [ ] Tomador de decisiones: quién tiene la última palabra (estético y económico)
- [ ] Presupuesto: ¿incluye terreno? ¿o solo construcción + honorarios?

### Tópico 2: Los habitantes
*Objetivo: Construir la UserEntity de cada habitante.*

- [ ] Quiénes van a habitar el edificio (cantidad, edades, salud/movilidad)
- [ ] Tipos de usuarios: residentes fijos, visitas frecuentes, servicio
- [ ] Capacidades: accesibilidad, necesidades especiales
- [ ] Quién pasa más tiempo en casa, quién trabaja desde casa
- [ ] Mascotas (tipo, cantidad, tamaño)

### Tópico 3: El programa arquitectónico
*Objetivo: Registrar los espacios solicitados. NO complementar en el momento.*

- [ ] Recámaras: cantidad, todas con baño y closet, ¿una en PB?
- [ ] Baños: baño de visitas, medios baños
- [ ] Zonas de trabajo/hobby: oficina, estudio, taller, gimnasio, cava, cuarto TV
- [ ] Servicios: cuarto de servicio, lavado, bodega, cochera (autos)
- [ ] Extras: alberca, terraza, jardín, roof garden
- [ ] Colecciones o equipamiento especial que requiera espacio dedicado

### Tópico 4: Dinámicas y rutinas
*Objetivo: Poblar la Activity Matrix de 24 slots por habitante.*

- [ ] Día entre semana: despertar, comidas, trabajo, llegada a casa, dormir
- [ ] Fines de semana: ¿diferente?
- [ ] Quién cocina, ¿comen juntos o separados?
- [ ] Visitas: frecuencia, fiestas, familia que se queda a dormir
- [ ] Clima: ¿ventilación natural o A/C? ¿qué tanto uso de aire esperan?
- [ ] Materiales: ¿buscan materiales "eternos" o aprecian pátina? ¿madera/piedra?
- [ ] Orden: espacios fáciles de limpiar vs "desorden creativo"

### Tópico 5: Inversión
*Objetivo: Validar viabilidad económica y definir prioridades.*

- [ ] Presupuesto realista para el proyecto completo
- [ ] ¿Construcción única o por etapas?
- [ ] Prioridad: más m² con acabados sencillos vs menos m² con acabados de lujo
- [ ] ¿Honorarios de diseño incluidos?
- [ ] Rango de obra esperado: $14k–$16.5k (Esencial), $18.5k–$23k (Integral), $28k–$40k (Ejecutivo)

### Tópico 6: La cereza del pastel (Poética)
*Objetivo: Extraer el CreativeCore y el Mensaje Creativo.*

- [ ] Si al entrar a tu casa pudieras sentir un solo adjetivo, ¿cuál sería?
- [ ] ¿Cuál es tu recuerdo más feliz relacionado con un espacio?
- [ ] ¿Hay algún objeto que deba dictar el diseño de un espacio?
- [ ] ¿Qué es lo que NO quieres que pase en este proceso?
- [ ] ¿Cómo te imaginas viviendo aquí en 10 años?
- [ ] Cierre: filosofía SOMA (automatizamos lo técnico, liberamos el diseño)

---

## Post-Entrevista

```
[ACC] Formulario Post-Entrevista
─────────────────────────────────
INPUT:  6 tópicos conversados + notas del arquitecto
OPERA:  Inmediatamente después de la entrevista, el arquitecto llena
        el formulario en la App de Entrevista: cliente, habitantes,
        programa, rutinas, inversión, notas adicionales
OUTPUT: `info.json` — metadatos estructurados del proyecto
PROC:   HUMANO
```

---

## Procesamiento con IA

```
[ACC] Análisis Automático (P2.0 ref: 3.10)
─────────────────────────────────
INPUT:  `entrevista.wav` + `info.json`
OPERA:  1) Transcripción con faster-whisper (local)
        2) Análisis con DeepSeek Flash API:
           - Extraer Activity Matrix por habitante
           - Identificar CreativeCore
           - Generar guía de diseño
        Sin API configurada → genera guía stub
OUTPUT: • `transcripcion.txt`
        • `guia_de_diseno.md` — documento para diseñadores
        • `datos_estructurados.json` — matriz, ejes, CreativeCore
PROC:   AI
```

---

## Estructura de proyecto generada

```
backend/proyectos/SOMA-YYYYMMDD-XXXX/
├── info.json                 ← metadatos (estado, cliente, fechas)
├── entrevista.webm           ← grabación de audio
├── transcripcion.txt         ← salida de Whisper
├── guia_de_diseno.md         ← documento para diseñadores
└── datos_estructurados.json  ← Activity Matrix, ejes, CreativeCore
```

### Complementariedad Web + Entrevista

| Fuente | Captura | Uso |
|--------|---------|-----|
| Inmersión Web (10 ejes) | Preferencias visuales A/B | Parámetros de fachada, planta, materialidad |
| Entrevista (6 tópicos) | Contexto profundo | Guía de diseño unificada |

Ambas fuentes se fusionan en la `guia_de_diseno.md` de cada proyecto.

---

## FUENTES

- Hall, E. T. (1966). *The Hidden Dimension.* Doubleday.
- Alexander, C. et al. (1977). *A Pattern Language.* Oxford University Press.
- Zeisel, J. (2006). *Inquiry by Design.* Norton.
- Deasy, C. M. & Lasswell, T. E. (1990). *Designing Places for People.*
- Holahan, C. J. (1982). *Environmental Psychology.* Random House.
- Sommer, R. (1969). *Personal Space: The Behavioral Basis of Design.*
