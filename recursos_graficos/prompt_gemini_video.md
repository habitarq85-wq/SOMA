# SOMA — Prompts por Escena para Video Filosófico

## Estilo General (aplica a todas las escenas)

### Referencias Visuales Principales

| Referencia | Elemento específico a tomar |
|---|---|
| **Ironman 2 / Avengers** (escenas de laboratorio de Tony Stark) | Gestos de manos que manipulan hologramas 3D: rotar, expandir, seccionar, pellizcar. Datos que fluyen alrededor de las manos como partículas. Iluminación del holograma reflejada en el rostro desde abajo. Wireframes volumétricos semitransparentes. |
| **Blade Runner 2049** | Iluminación general: neblina ligera, contraste dramático, luz rasante, sombras profundas pero con detalle. Atmósfera densa pero limpia. Tonos fríos con un solo acento de color cálido. |
| **Her (Spike Jonze)** | Paleta de colores: tonos terracota, naranjas quemados, blancos rotos, fondos oscuros no negros. Calidez emocional en la iluminación. Texturas suaves. |
| **Ex Machina** | Estética de interfaz: minimalista, limpia, líneas delgadas, datos flotantes sin ruido visual. La tecnología se siente avanzada pero no futurista — es creíble, cercana. |
| **Fotografía de Josef Schulz** | Texturas de concreto y materiales industriales: limpias, pulidas, sin imperfecciones dramáticas. La materialidad es protagonista silenciosa. |
| **Fotografía de Candida Höfer** | Composición de espacios arquitectónicos: simétrica, equilibrada, sin personas. La arquitectura se muestra sola, para ser contemplada. |

### Especificaciones de Cámara

- **Formato:** 16:9 horizontal, 24fps
- **Movimiento:** Flotante tipo steadicam, siempre en cámara lenta constante. Sin movimientos bruscos ni zoom digital. Desplazamientos laterales (truck) y orbitales suaves.
- **Profundidad de campo:** Muy poca en primeros planos (f/1.8 - f/2.8). Abierta (f/8 - f/11) en planos generales de arquitectura para mantener toda la escena nítida.
- **Planos:** Sostenidos (mínimo 2 segundos por plano). Sin cortes rápidos. Cada escena debe sentirse como una respiración.
- **Lente sugerido:** 35mm-50mm para escenas de arquitectura (perspectiva natural). 85mm-100mm para primeros planos de manos y detalles constructivos.

### Paleta de Color

- **Fondos:** #0a0a0a (negro profundo pero con textura, no plano)
- **Acento principal:** #bc4b21 (terracota) — presente en luces de interfaz, reflejos, tipografía
- **Concreto:** #8a8a8a a #c4c4c4 (grises pulidos, nunca fríos)
- **Madera:** #a67c52 a #d4a574 (cálida, miel, nunca caoba oscura)
- **Blancos:** #e8e0d8 (blanco roto, cálido, nunca blanco puro #ffffff)
- **Verde código:** #4a9e6b (verde pantalla, usado solo en escenas de código)
- **Iluminación:** Siempre cálida (temperatura color ~3500K-4500K). La luz terracota solo aparece como luz activa (hologramas, interfaces, reflejos).

### Iluminación

- **Clave principal:** Lateral o superior frontal, con textura (luz que entra por persianas, ventanas, o rendijas). Nunca luz cenital plana.
- **Luz de relleno:** Muy suave, 2 stops por debajo de la clave. Sombras con detalle, nunca negros aplastados.
- **Acento:** Luz terracota (#bc4b21) como contraluz o luz de borde en escenas de estudio. En escenas de interfaz, el holograma es la fuente de luz principal.
- **Práctica:** En escenas de taller/trayectoria, luz natural de ventana como fuente principal.

### Texturas y Materialidad

- **Concreto:** Pulido, liso, con porosidad mínima visible en primeros planos. Color gris neutro cálido.
- **Madera:** Veta visible, acabado mate o satinado, nunca brillante. Tonos miel.
- **Piedra:** Natural, textura suave al tacto visual, color gris-beige.
- **Acero:** Oscuro, satinado, sin reflejos especulares fuertes.
- **Textiles:** Lino, algodón crudo, lana — nunca sintéticos ni brillantes.

### Tipografía en Pantalla

- **Fuente:** Sans-serif delgada (estilo Helvetica Neue Light, Inter Light, o similar)
- **Color:** #bc4b21 (terracota)
- **Tamaño:** Moderado, legible en 16:9. Sin opacar la imagen.
- **Posición:** Variable según la escena (inferior izquierda, centrada, o integrada como HUD)
- **Animación:** Fundido suave de entrada y salida (0.3s fade in, 0.3s fade out). Sin desplazamientos ni efectos.
- **Estilo:** En escenas digitales (2, 3) los textos pueden parecer generados por la interfaz. En escenas físicas (1, 4, 5, 6) deben sentirse como parte del espacio.

### Transiciones Entre Escenas

Todas las transiciones deben ser morphs suaves o fundidos cruzados de 0.5-1 segundo. Sin cortes directos. La transición debe sentirse como un solo movimiento continuo de cámara a través de 7 espacios diferentes.

### Consistencia

- El mismo arquitecto protagonista en todas las escenas donde aparece (escenas 2, 3, 4)
- Consistencia de iluminación, paleta y texturas a lo largo de todo el video
- Sin narración ni voz en off
- Sin música — los textos en pantalla son el único elemento sonoro visual

---

## ESCENA 1 — ARQUITECTURA ACCESIBLE
*Duración: ~4 segundos*

### Concepto
La arquitectura de alta calidad no es cuestión de presupuesto. La creatividad y el mensaje trascienden los materiales costosos. Un espacio modesto puede tener la misma dignidad arquitectónica que uno de lujo.

### Prompt para Gemini

> Una sala pequeña con doble altura. Luz natural entra por un ventanal amplio. Los materiales son sencillos — concreto pulido en el piso, muros blancos, madera cálida en el techo. Una persona está sentada en un banco de madera junto a la ventana, leyendo. La luz crea patrones geométricos en el concreto. La cámara se desliza lateralmente muy lento. El espacio se transforma suavemente en otro similar — misma calidad de luz, mismos materiales, misma dignidad espacial — pero diferente escala. Fundido continuo entre espacios. Texturas de concreto y madera. Luz tamizada. Cámara lenta y contemplativa. Sin personas visibles después de la primera toma. Estilo cinematográfico oscuro, terracota tenue en los reflejos.

### Transición a Escena 2
El último espacio se disuelve en un estudio oscuro. Partículas de código flotan brevemente en la disolución.

---

## ESCENA 2 — INTERFAZ HOMBRE-MÁQUINA
*Duración: ~5 segundos*

### Concepto
El arquitecto no compite con la máquina: la domina. Sus manos son la interfaz. Los algoritmos responden a sus gestos. La tecnología es una extensión de su cuerpo.

### Prompt para Gemini

> Un arquitecto de pie en un estudio oscuro. Frente a él, flota un modelo arquitectónico 3D holográfico — una casa en wireframe terracota, semi-transparente, que gira lentamente. El arquitecto extiende las manos y con gestos naturales (como Tony Stark en Avengers) manipula el holograma: rota la maqueta con un giro de muñeca, la expande separando las manos, la secciona con un movimiento de pinza. Líneas de código, ecuaciones paramétricas y nodos de Grasshopper fluyen como datos alrededor de sus manos y antebrazos — partículas verdes y terracota que siguen el movimiento de sus dedos. La luz del holograma ilumina su rostro desde abajo. El fondo es oscuro, con reflejos sutiles de concreto y acero. Cámara orbita lentamente alrededor de la escena, a media altura. Sin texto. Estilo cinematográfico, iluminación tipo Blade Runner 2049.

### Transición a Escena 3
Primer plano de las manos del arquitecto. Los nodos de código se aceleran, se multiplican, se vuelven más densos.

---

## ESCENA 3 — AUTOMATIZACIÓN
*Duración: ~3 segundos*

### Concepto
El código construye solo. Muros, pisos, ventanas se generan automáticamente mientras el arquitecto observa. Lo protocolario se programa.

### Prompt para Gemini

> Vista cenital de dos manos abiertas flotando sobre una superficie oscura. Entre las manos, líneas de código verde y terracota fluyen verticalmente como cascada de datos. Debajo de las manos, un modelo arquitectónico se construye solo en tiempo real: los muros se extienden desde el suelo como si crecieran, los pisos se colocan como fichas de dominó, las ventanas se repiten en fachada con precisión milimétrica. El código y la construcción ocurren simultáneamente — cada línea de código genera un elemento constructivo. Las manos del arquitecto están quietas, solo observan. El proceso es rápido, hipnótico, preciso. Los dedos se mueven ligeramente, como dirigiendo una orquesta. Iluminación fría de pantalla. Sin texto. Estilo interactivo, programático, visualmente limpio.

### Transición a Escena 4
El código se desvanece. Las manos del arquitecto bajan lentamente. La escena se funde a un espacio iluminado por luz natural.

---

## ESCENA 4 — CREATIVIDAD LIBERADA
*Duración: ~4 segundos*

### Concepto
Cuando la tecnología hace lo técnico, el arquitecto vuelve a lo esencial: las manos en la materia, el boceto, la maqueta física, la decisión creativa.

### Prompt para Gemini

> El mismo arquitecto ahora está de pie frente a una mesa de madera maciza en un taller iluminado por luz natural de atardecer. Sobre la mesa hay una maqueta física de espuma y cartón — una casa en miniatura. El arquitecto sostiene una pieza pequeña, la observa desde distintos ángulos, la coloca con cuidado en la maqueta. Sus manos están manchadas de pegamento y lápiz. Detrás de él, al fondo desenfocado, se ve la computadora con el modelo 3D — pero ya no es el centro. En la pared hay bocetos a mano alzada, muestras de materiales, fotografías de obra. La luz natural cálida inunda el espacio. El arquitecto da un paso atrás, cruza los brazos, observa la maqueta con satisfacción. La tecnología hizo lo técnico; él hace lo creativo. Cámara lenta, plano sostenido. Sin texto.

### Transición a Escena 5
La maqueta física se transforma mediante morph en tres espacios arquitectónicos reales lado a lado.

---

## ESCENA 5 — TRES NIVELES, UNA CALIDAD
*Duración: ~3 segundos*

### Concepto
Esencial, Integral, Ejecutivo. Diferentes escalas, misma atención al detalle. El lujo no está en el tamaño sino en la intención del diseño.

### Prompt para Gemini

> Tríptico horizontal: tres espacios arquitectónicos lado a lado en el mismo cuadro, separados inicialmente por líneas delgadas de luz terracota. Izquierda: un espacio pequeño pero bien proporcionado — una sala con doble altura, concreto y madera, modesta pero digna. Centro: una casa familiar con patio interior, vegetación, más amplia, equilibrada. Derecha: una residencia amplia con jardín, generosa, con mobiliario de diseño. Los tres espacios comparten la misma luz cálida, los mismos materiales honestos (concreto, madera, piedra), la misma atención al detalle en las uniones y texturas. Las líneas divisorias se disuelven suavemente y los tres espacios convergen en uno solo. Cámara lenta, sin texto. Iluminación consistente. Materialidad que conecta las tres escalas.

### Transición a Escena 6
El espacio unificado se transforma en un solo detalle constructivo.

---

## ESCENA 6 — LO SUBLIME ACCESIBLE
*Duración: ~4 segundos*

### Concepto
Cada elemento existe por una razón. Nada es decorativo. La junta donde el concreto encuentra la madera: precisa, limpia, intencional. La calidad está en los detalles.

### Prompt para Gemini

> Primer plano extremo de un detalle constructivo. La junta donde una viga de madera cálida se encuentra con un muro de concreto pulido. La unión es perfecta — ni una separación, ni un error. La luz natural rasante recorre la superficie, revelando la textura del concreto y la veta de la madera. La cámara se mantiene en este detalle 2 segundos, sin movimiento. Luego se desplaza lentamente hacia arriba, revelando que este detalle pertenece a un espacio habitable — la misma sala de doble altura de la Escena 1, pero ahora la entendemos: cada elemento, cada junta, cada material está ahí por una razón. La cámara retrocede lentamente mientras la luz se vuelve más cálida. Fundido lento a negro. Sin texto. La imagen debe transmitir que la calidad no es decoración: es intención.

### Transición a Escena 7
Negro completo.

---

## ESCENA 7 — CIERRE
*Duración: ~3 segundos*

### Concepto
Identidad visual de SOMA.

### Prompt para Gemini

> Sobre fondo negro. Aparece lentamente el texto: "SOMA — Taller Virtual de Arquitectura". Tipografía limpia, sans-serif delgada, color terracota (#bc4b21). Abajo, más pequeño: "Lo protocolario se programa, lo creativo se libera". Sin animación, solo fundido de entrada. El texto se mantiene 2 segundos. Fundido lento a negro. Sin elementos adicionales. Sin música sugerida.

---

## Notas Técnicas Generales

- Cada escena debe funcionar como un clip individual de 3-5 segundos
- Las transiciones entre escenas pueden ser fundidos o morphs suaves
- La referencia Ironman/Avengers aplica especialmente a las Escenas 2 y 3: las manos como interfaz, gestos que controlan datos, hologramas que responden al movimiento
- Consistencia del protagonista (mismo arquitecto) en todas las escenas donde aparece
- Textos explicativos cortos aparecen y desaparecen en cada escena (ver prompts individuales)
- La iluminación general debe ser dramática pero natural, con el acento terracota como único color saturado
