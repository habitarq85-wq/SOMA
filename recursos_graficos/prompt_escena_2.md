# ESCENA 2 — INTERFAZ HOMBRE-MÁQUINA
*Duración: ~5 segundos*

## Concepto
El arquitecto no usa la máquina: la extiende. Sus manos son el mouse, el teclado, la interfaz. Los algoritmos responden a sus gestos como extensión natural del cuerpo.

## Textos en pantalla (aparecen y desaparecen)

| # | Texto | Timing | Posición | Animación |
|---|-------|--------|----------|-----------|
| 1 | `"LA MANO COMO INTERFAZ"` | t=0.0s aparece, t=2.0s se desvanece | Inferior izquierda (x=5%, y=80%) | Fundido 0.3s in, 0.4s out. Estilo HUD: aparece como si un sistema lo etiquetara |
| 2 | `"EL GESTO COMO COMANDO"` | t=2.0s aparece, t=4.0s se desvanece | Esquina inferior derecha (x=60%, y=80%) | Fundido 0.3s in, 0.4s out. Aparece sincronizado con el gesto de rotación |
| 3 | `"HOMBRE + MÁQUINA"` | t=4.0s aparece, se mantiene hasta transición | Centrado (x=50%, y=75%) | Fundido 0.4s in. Se mantiene hasta que la escena se desvanece |

**Tipografía:** Sans-serif delgada, color #bc4b21, con un 20% de transparencia (que parezca发光 de interfaz). Sin sombra. Sin borde. Los textos deben sentirse generados por el propio sistema holográfico — como etiquetas de datos en una interfaz de Ironman.

## Especificaciones de cámara

- **Tipo:** Orbita lenta alrededor del arquitecto (180° en 5 segundos)
- **Velocidad:** Muy lenta — el arquitecto completa un arco de 180° mientras la cámara se mueve de su frente izquierdo a su frente derecho
- **Lente:** 50mm (retrato comprimido, aísla al sujeto del fondo)
- **Profundidad de campo:** f/2.0 — fondo oscuro desenfocado, el arquitecto y el holograma nítidos
- **Altura:** A la altura del pecho del arquitecto (~1.40m del suelo)
- **Movimiento:** Orbital suave, como una grúa robótica. Sin vibración. El centro de la órbita es el holograma flotante.

## Iluminación

- **Fuente principal:** El propio holograma arquitectónico. Luz terracota (#bc4b21) emitida desde el modelo 3D flotante
- **Calidad:** Luz dura con caída rápida — ilumina el rostro del arquitecto desde abajo (luz de monitor)
- **Relleno:** Muy mínimo — reflejo ambiente de las superficies del estudio (1/4 de la principal)
- **Acento:** Luz de borde fría (#4a6b8a) muy sutil desde atrás para separar al arquitecto del fondo oscuro
- **Contraste:** Alto — 6 stops entre el holograma (punto más brillante) y el fondo (negro con textura)

## Paleta de colores para esta escena

- **Fondo estudio:** #0a0a0a (negro texturizado, no plano)
- **Piel arquitecto:** Iluminada por terracota — tonos cálidos naturales con reflejo #bc4b21
- **Holograma:** #bc4b21 (wireframe) con toques #d47a41 (acentos más brillantes)
- **Datos flotantes:** #4a9e6b (verde código) y #bc4b21 (terracota)
- **Luz de borde:** #4a6b8a (azul acero muy sutil)

## Composición

**Plano medio:** El arquitecto está ligeramente descentrado (tercio izquierdo). El holograma ocupa el centro del encuadre. Las manos del arquitecto entran desde la izquierda. Detrás, el fondo es negro con reflejos de concreto y acero apenas perceptibles. La composición evoca la escena del laboratorio de Tony Stark en Avengers: el sujeto a un lado, el holograma al centro, las manos como interfaz.

## Elementos visuales clave

- Modelo arquitectónico 3D en wireframe terracota (una casa) flotando y rotando lentamente
- Manos del arquitecto haciendo gestos precisos: rotar (giro de muñeca), expandir (separar manos), seccionar (pinza de dedos)
- Partículas de datos (nodos de Grasshopper, líneas de código, ecuaciones paramétricas) fluyendo alrededor de las manos y antebrazos
- Cada gesto debe generar una respuesta visual inmediata en el holograma

## Secuencia de gestos

| Tiempo | Gesto | Efecto en holograma |
|--------|-------|---------------------|
| t=0s a 1.5s | Manos quietas, observa | El modelo gira lentamente solo |
| t=1.5s a 2.5s | Giro de muñeca derecha | El modelo rota 90° |
| t=2.5s a 3.5s | Separa ambas manos | El modelo se expande (zoom in virtual) |
| t=3.5s a 4.5s | Pinza con índice y pulgar | El modelo se secciona, mostrando corte longitudinal |
| t=4.5s a 5.0s | Manos bajan lentamente | El modelo vuelve a su estado original |

## Transición a Escena 3
Primer plano de las manos del arquitecto. Los datos se aceleran, se multiplican, se vuelven más densos. Los textos se desvanecen convertidos en partículas de código. La luz cambia de terracota cálida a verde frío de pantalla. Fundido de 0.5s donde las manos y el código son el elemento de continuidad.
