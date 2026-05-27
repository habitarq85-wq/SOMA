# PROTOCOLO: MODELADO SOMA
## Bloque 2 — Taller SOMA (Operación) | Etapa 5 del Ciclo

### ¿Qué es el Modelado?

Es la traducción del concepto arquitectónico a un modelo digital tridimensional
que sirve como herramienta de diseño, verificación y base para las etapas
siguientes (visualización, planos, evaluación).

**Entrada:** Documento de Concepto (de la Conceptualización).
**Salida:** Modelo 3D del proyecto verificado y listo para extraer vistas.

### Principio rector

El modelo es una herramienta de decisión, no un dibujo bonito.
Se modela para entender, verificar y comunicar, no para decorar.

---

## 1. DEL CONCEPTO AL VOLUMEN

### 1.1 Preparación

- [ ] Revisar el Documento de Concepto: Idea Matriz, diagrama de masas,
      zonificación SOMA, esquema de recorridos.
- [ ] Definir la **escala de trabajo**: 1:100 para modelo general,
      1:50 para zonas críticas.
- [ ] Elegir la **herramienta**: según el alcance del paquete contratado:
  - **SketchUp** — modelo conceptual rápido, ideal para Visualización
  - **Revit** — modelo BIM, obligatorio para Planos Técnicos (Ejecutivo)
  - **Blender** — alternativa open source, modelado + render
- [ ] Configurar el sistema de coordenadas: orientar el modelo al norte real
      (del análisis de sitio).

### 1.2 Construcción del Volumen Base

- [ ] Trazar el **polígono del predio** con dimensiones reales.
- [ ] Trazar el **bounding box legal** (COS, CUS, alturas máximas).
- [ ] Colocar la **vegetación existente a conservar** como referencia
      espacial (árboles, albarradas).
- [ ] Construir el **volumen base** de la opción seleccionada:
  - Macizo inicial que cumple el programa en planta.
  - Aplicar las operaciones formales definidas (sustracción/adiciones/
        fragmentación/plegados).
  - Verificar que el volumen respeta el bounding box.

### 1.3 Verificación Conceptual

- [ ] ¿El volumen refleja la Idea Matriz? (recorrer el modelo, sentir
      si comunica lo que debe).
- [ ] ¿La zonificación SOMA está correctamente ubicada en el modelo?
- [ ] ¿El recorrido principal funciona en 3D? (simular el recorrido
      a vista de peatón).
- [ ] ¿Las protecciones solares del análisis funcionan en el volumen?
      (sombras arrojadas sobre vanos).

---

## 2. ESTRATEGIA DE MODELADO

### 2.1 Niveles de Desarrollo (LOD)

| Paquete | LOD mínimo | Herramienta sugerida | Qué se modela |
|---------|-----------|---------------------|---------------|
| Esencial | LOD 200 | SketchUp / Blender | Masas, vanos, cubierta, topografía |
| Integral | LOD 300 | Revit / Blender | Muros, losas, estructuras, instalaciones esquemáticas |
| Ejecutivo | LOD 350+ | Revit | Todos los elementos constructivos, detalles |

- [ ] Definir el LOD objetivo según el paquete contratado.
- [ ] No modelar más de lo necesario para el LOD acordado (evitar
      tiempo perdido en detalles que no se entregarán).

### 2.2 Organización del Modelo

- [ ] **Capas / Categorías:** Separar por sistemas:
  - Estructura (cimentación, columnas, losas, vigas)
  - Arquitectura (muros, pisos, cubiertas, vanos, acabados)
  - Mobiliario (solo el necesario para verificar ergonomía)
  - Contexto (predio, vegetación, colindancias)
  - Instalaciones (solo diagramático en Integral+)
- [ ] **Nombres de elementos:** Convención consistente
      (ej: `MURO_EXTERIOR_PB_NORTE`, `LOSA_PB_COCINA`).
- [ ] **Grupos / Componentes:** Todo elemento repetible debe ser
      componente para facilitar cambios masivos.
- [ ] **Colores por zona SOMA** en vista de planta:

| Zona | Color sugerido |
|------|---------------|
| Social | Cálido (naranja/ocre) |
| Descanso | Frío (azul/verde) |
| Operativa | Neutro (gris) |
| Soporte | Oscuro (gris oscuro/marrón) |
| Transición | Claro (blanco/beige) |

### 2.3 Iteración y Verificación Continua

- [ ] Modelar por **ciclos cortos**: volumen → vanos → circulación →
      revisión → ajuste → siguiente ciclo.
- [ ] Cada ciclo verificar contra las **Intenciones de Diseño**
      (sección 3 del protocolo de Conceptualización).
- [ ] Cada ciclo verificar contra **constraints**:
  - Área construida ≤ CUS
  - Áreas por espacio ≥ dimensiones mínimas normativas
  - Alturas libres ≥ 2.60 m (2.40 m baños)
  - Circulaciones ≥ 0.90 m

---

## 3. MODELADO POR SISTEMAS

### 3.1 Sistema Estructural (Esquemático)

- [ ] Definir la **trama estructural** (ejes, claros, dirección de losas).
- [ ] **Cimentación:** Tipo según mecánica de suelos (zapata corrida,
      losa de cimentación, pilotes). En Yucatán: comúnmente losa
      de cimentación por roca calcárea a poca profundidad.
- [ ] **Columnas / Muros de carga:** Ubicación cada 4–6 m. Evitar
      columnas dentro de espacios que interrumpan el uso.
- [ ] **Losas:** Espesor según claro (losa maciza ~12–15 cm para claros
      de 4–5 m; losa reticular para claros mayores).
- [ ] **Cubierta:** Pendiente para drenaje (mín 2%). Tipo según
      estrategia bioclimática seleccionada (cool roof, techo ventilado,
      losa tradicional).

### 3.2 Sistema Arquitectónico

- [ ] **Muros exteriores:** Espesor y composición según estrategia
      bioclimática (doble hoja con aislamiento, block macizo + repellado).
- [ ] **Muros interiores:** Block partido o tablaroca (zona seca).
      En baños y cocina: block o tabique impermeable.
- [ ] **Vanos:** Dimensiones según el % de ventana/piso definido en
      el análisis de iluminación.
  - Posición: alinear dinteles a una altura constante (2.40 m
        recomendado) para orden visual en fachada.
  - Protección solar: aleros, celosías o volados según el análisis.
- [ ] **Cubierta:** Tipo (plana o inclinada), pendiente, material
      de acabado (impermeabilizante reflectante, teja, losa verde).

### 3.3 Circulaciones y Accesos

- [ ] Modelar el **recorrido principal** como un elemento continuo
      (una tira o volumen que atraviesa el proyecto).
- [ ] Verificar **alturas libres** en todo el recorrido.
- [ ] Verificar **anchuras** mínimas en puertas y pasillos.
- [ ] Marcar **umbrales**: cambios de nivel, cambio de material en piso,
      cambio de altura de techo.
- [ ] **Acceso principal:** Modelar el portal/entrada con énfasis
      (es la primera experiencia del usuario).

### 3.4 Instalaciones (Diagramático)

*Solo para Integral y Ejecutivo.*

- [ ] **Rutas de instalaciones:** Prever ductos verticales y horizontales
      (no modelar tuberías, solo shaft y espacios de instalaciones).
- [ ] **Baños:** Agrupar para compartir instalaciones (muros contiguos
      de baños).
- [ ] **Cocina:** Prever salida de campana, ducto de gas, punto de agua.
- [ ] **Cuarto de instalaciones:** Ubicación para calentador, cisterna,
      tinacos, aire acondicionado.

---

## 4. VERIFICACIÓN DEL MODELO

### 4.1 Checklist de Verificación

- [ ] **Programa:** ¿cada espacio del programa está modelado con su
      área correcta? Lista de espacios vs modelo.
- [ ] **Zonificación SOMA:** ¿cada espacio está en la zona correcta?
- [ ] **Circulaciones:** ¿el recorrido principal es fluido? ¿los anchos
      son correctos?
- [ ] **Orientación:** ¿el modelo está orientado al norte real?
      ¿las fachadas E/O tienen protección solar?
- [ ] **Accesibilidad:** ¿hay algún desnivel sin rampa? ¿puertas con
      ancho suficiente?
- [ ] **Estructura:** ¿las columnas no estorban en los espacios?
      ¿los claros son razonables?
- [ ] **Alturas:** ¿todas las alturas libres cumplen el mínimo?
- [ ] **Áreas:** ¿el área total construida no excede el CUS?

### 4.2 Pruebas Visuales Mínimas

- [ ] **Vista aérea:** ¿la forma se lee claramente desde arriba?
      (la vista más común en presentaciones).
- [ ] **Vista peatonal desde la calle:** ¿el proyecto se integra
      al contexto? (del análisis contextual).
- [ ] **Vista interior del espacio principal:** ¿la luz entra como
      se planeó? (del análisis de iluminación).
- [ ] **Corte por el espacio principal:** ¿la relación de alturas,
      vanos y volumetría funciona?
- [ ] **Recorrido animado (opcional):** Cámara que recorre el
      proyecto a velocidad peatonal.

### 4.3 Correcciones

- [ ] Documentar los problemas encontrados en la verificación.
- [ ] Priorizar: errores de programa > errores de circulación >
      errores de dimensiones > errores estéticos.
- [ ] Cada corrección debe responder: ¿sigue siendo fiel al
      concepto? (Idea Matriz). Si no, ajustar el modelo o
      re-evaluar el concepto.

---

## 5. SALIDA DEL MODELADO

Al completar esta etapa, se genera:

1. **Modelo 3D** en la herramienta seleccionada, organizado por capas
   y con la nomenclatura definida.
2. **Planos base del modelo:** Plantas, cortes y alzados extraídos
   del modelo (aunque sean esquemáticos).
3. **Checklist de verificación** marcado (completado/pendiente).
4. **Notas de diseño:** Decisiones tomadas durante el modelado que
   no estaban previstas en la conceptualización.
5. **Archivo de intercambio:** Exportación a formato compatible
   (.ifc para Revit, .fbx/.obj para Blender/SketchUp).

Este modelo es la entrada directa a:
- **Visualización** (Etapa 6) — para renders y presentaciones.
- **Representación Integral** (Etapa 7) — para el dossier editorial.
- **Evaluación** (Etapa 8) — para verificación de indicadores de habitabilidad.
- **Planos Técnicos** (Etapa 9) — si el paquete es Ejecutivo.

---

*El modelo no es el proyecto; es una representación del proyecto.
Lo importante no es cómo se ve el modelo, sino que las decisiones
de diseño sean correctas.*

---

## FUENTES

- **BIM Forum**, *Level of Development (LOD) Specification* (2023) — definición de LOD 200, 300, 350+ para elementos del modelo. (bimforum.org)
- **ISO 19650-1:2018** — Organization and digitization of information about buildings and civil engineering works, including building information modelling (BIM). (iso.org)
- **Francis D.K. Ching**, *Building Construction Illustrated* (6th ed., 2020) — composición de muros, losas, cubiertas, sistemas constructivos.
- **Francis D.K. Ching**, *Architectural Graphics* (6th ed., 2015) — capas, organización de planos, convenciones de dibujo.
- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — verificación espacial del modelo contra intenciones de diseño.
- **C. M. Deasy**, *Design Places for People* (1974) — modelado centrado en la experiencia del usuario, no solo en la geometria.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — coherencia entre el modelo 3D y la intencion funcional del proyecto.
- **Autodesk Revit Best Practices** — organización por worksets, naming conventions, familias parametrizadas. (autodesk.com)
- **D5 Render Official Documentation** — exportación de modelos desde Revit/Blender/SketchUp. (d5render.com/learn)
- **Reglamento de Construcción del Municipio de Mérida** — alturas libres mínimas (2.60m), anchos de circulación (0.90m), dimensiones mínimas de espacios.
- **NOM-008-SCFI** — Sistema General de Unidades de Medida.
- **Andrea Deplazes** (ed.), *Constructing Architecture: Materials, Processes, Structures* (3rd ed., 2005) — manual tectónico: modelado de materiales, uniones, encuentros constructivos.
- **Edward Allen**, *Fundamentals of Building Construction* (7th ed., 2019) — construcción en detalle, modelado de sistemas constructivos, composición de envolventes.
- **NOM-001-SEDE** — Instalaciones Eléctricas (distancias de seguridad en shafts).
