# REFLEXIONES ESTRATÉGICAS - JUAN (SOMA)

## [2026-05-12] - Estrategia de Precios y Democratización
"Quiero volver al precio por m2. El objetivo es ser agresivo con los precios para democratizar la arquitectura, permitiendo que proyectos de lujo compensen lo que los proyectos accesibles necesitan."

"Si bien hay mucho valor invertido en el desarrollo del emprendimiento y el desgaste del equipo, estoy utilizando muchas herramientas open source (incluso D5 en versión gratuita con bloques de Warehouse) para reducir costos operativos. El lujo está en los materiales y en el detalle, pero lo sublime está en la creatividad y el mensaje. No necesitamos lujos para que la arquitectura de alta calidad exista y llegue a todos."

### Definición de Precios de Ancla (SOMA v2):
- **SOMA Esencial:** $200 / m² (Democratización real, proceso automatizado).
- **SOMA Integral:** $550 / m² (Motor financiero, equilibrio diseño/técnica).
- **SOMA Ejecutivo:** $1,100 / m² (Lujo competitivo, subsidio cruzado).

### [2026-05-13] - Ajuste de Escala Competitiva (SOMA v2.1)
"He decidido ajustar los precios para competir frontalmente con despachos que ofrecen ejecutivos a $550/m². Me preocupa que el nivel integral de la competencia sea mucho más bajo que el nuestro, por lo que rediseñamos la oferta."

"El objetivo sigue siendo la democratización, pero asegurando que el salto entre niveles sea lógico para el cliente y rentable para el sistema SOMA. El nivel Ejecutivo a $1,000 sigue siendo nuestro motor de subsidio cruzado para los niveles base."

**Nueva Escala Oficial:**
- **SOMA Esencial:** $250 / m² (Subimos para dar confianza, pero seguimos bajo la competencia).
- **SOMA Integral:** $400 / m² (Bajamos para ser competitivos frente a los $357 del mercado, justificando el valor con nuestra tecnología).
- **SOMA Ejecutivo:** $1,000 / m² (Número redondo psicológico, incluye coordinación técnica integral).

### Entregables por Paquete

#### ANTEPROYECTO BÁSICO
Diseño arquitectónico completo que incluye plantas, alzados, análisis de sitio y normativa, así como una perspectiva general del proyecto.

#### ANTEPROYECTO INTEGRAL
Todo lo del nivel básico más moodboard de acabados, criterios de ingenierías, planos para permiso de construcción y perspectivas adicionales del proyecto.

#### EJECUTIVO
Todo lo del nivel integral más planos técnicos ejecutivos, detalles constructivos específicos y coordinación integral de ingenierías.


### [2026-05-14] - Consolidación del Taller y Zonificación Maestra
"En SOMA lo técnico se programa y lo creativo se libera. No somos un producto de fábrica, somos un Taller de Diseño que usa la tecnología como exoesqueleto. En pragmatismo el proceso puede parecer un producto, pero el resultado es una pieza de autor única."

"He decidido ajustar el cargo mínimo operativo del taller a $8,000 MXN. Las personas no necesitan saber que ese es nuestro mínimo; el sistema debe aplicarlo de forma silenciosa para proteger la viabilidad de proyectos pequeños sin espantar al cliente con explicaciones técnicas."

"La zonificación oficial de SOMA se divide en: Social, Descanso, Operativa, Soporte y Transición. Estos son los parámetros que el sistema debe usar para procesar el habitar, aunque en el cotizador usemos términos comunes para no confundir a la gente."

"Sobre los riesgos de utilidad en proyectos pequeños: aquí aplico el querer democratizar la arquitectura. El lujo (proyectos de gran escala y niveles ejecutivos) paga la inclusividad. El impacto social de resolver bien un espacio pequeño con alta calidad de diseño es fundamental para la tesis de SOMA."

"En el cotizador, el precio no tiene relación con la calidad. Desde el nivel básico se entregan planos arquitectónicos formales, cortes y perspectivas fotorealistas de propuesta. La calidad es innegociable y constante; lo que varía es la profundidad de la información técnica y el alcance de los entregables."

### [2026-05-15] - Instrucciones sobre la Página Web 5

"En los entregables del cotizador no deben aparecer los precios de los paquetes, solo el nombre: SOMA ESENCIAL, SOMA INTEGRAL, SOMA EJECUTIVO. El precio lo ve el sistema internamente."

"En el paso de contacto, la leyenda debe decir: Ingresa tu correo o número de WhatsApp para contactarnos. El botón solo debe decir Enviar. La leyenda de privacidad debe decir: Tus datos están protegidos. Solo los usaremos para enviarte información."

"En el cotizador, el primer apartado debe ser Por Programa (Espacios)."

"En el paso de éxito después del contacto debe decir: ¿Quieres saber cuánto costaría tu diseño y cuánto podrías invertir en obra? Con una nota abajo: Te damos un estimado paramétrico por m². Nosotros diseñamos, un constructor externo ejecuta."

"El análisis de las respuestas de inmersión no es para el cliente, es para el área de diseño arquitectónico."

"Cuando el cliente ponga su contacto debe validarse que sea un correo o número de teléfono real, no cualquier texto."

"El WhatsApp de notificación debe llegarme a mí cuando el cliente registre su contacto, no debe abrírsele al cliente al final del cotizador. El botón del paso final solo debe decir Finalizar."

"Los reportes de inmersión se guardan en backend/reportes/ mientras configuramos el envío de correos."

"El botón de Enviar no debe abrir WhatsApp para el cliente. Solo debe enviar los datos al servidor. La notificación me llega por el servidor y el reporte se guarda en backend/reportes/. Cuando configure el correo, se enviará automáticamente a habitarq85@gmail.com."

### [2026-05-18] - Instrucciones sobre Notificaciones (SMTP + WhatsApp)

"yo necesito que el cliente cuando me ponga su wasap en las preguntas de inmersión, este me mande el wasap a mi numero para hacer el contact, twilio es para eso."

"lo tendré que pagar después?"

"ya me inicie sesión, vamos a usarlo para pruebas en modo gratis y despues lo cambiamos al telegram. eso apuntalo en algun lado para tenerlo asentado."

**Decisión:** Twilio se usará mientras dure el crédito gratuito (~$15 USD). Cuando se termine, migrar a Telegram (gratis 100%).

### [2026-05-18] - Instrucciones sobre el Dashboard

"ponle nombres comunes en español"

"por ejemplo, no se que hace referencia pipeline."

**Corrección:** Traducir todo el Dashboard a español: Pipeline → Clientes, Leads → Clientes, ONLINE → ACTIVO, OFFLINE → INACTIVO, etc.

### [2026-05-18] - Instrucciones sobre la Matriz de 24 Horas

"que es esa matriz de 24 horas, no recuerdo haberlo pedido"

**Explicación:** Tabla que registra qué hace cada habitante hora por hora para determinar necesidades de aislamiento, iluminación y zonificación.

### [2026-05-18] - Instrucciones sobre la App de Entrevista

"Ok, ya voy recordando, la idea es generar una aplicación de entrevista interactiva con el cliente. /home/juan/Documentos/PROYECTO SOMA/aplicaciones_python/app_inmersion/ Aqui se avanzó esta aplicación y dentro de la carpeta web en el archivo Entrevista_Guion esta el guión. analizame los pasos a seguir."

"si, esta bien la estructura solo que el guión se diseño para hacer la entrevista en tono natural poco rigida. La idea de la aplicación es esta:
1. Llego con el cliente con la entrevista previamente estudiada en cuanto a tópicos.
2. abro en mi celular la web con la aplicación de la entrevista.
3. La aplicación se activa cuando yo le aprieto el boton de iniciar, en ese momento empieza a grabar la conversación y comienza con una introducción y el primer tópico que creo no aparece adecuadamente en el guión (hableme de la razón para estar aquí, es decir expliqueme lo que quiere, donde el cliente va a describir que construcción quiere hacer, que espacios necesita y como los necesita).
4. Posteriormente yo intervengo con el segundo tópico que es quienes van a habitar ese edificio (cantidad de usuarios, tipos de usuarios, capacidad de usuarios (accesibilidad).
5. El siguiente tópico sería las características del programa que me están pidiendo para saber como complementarlo o ampliarlo si es necesario.
6. Posteriormente vendrían las dinámicas de los espacios, es decir usos y costumbres, rutinas.
7. El siguiente tópico se refiere a la cantidad que pueden invertir en el proyecto, para saber si es por etapas, que acabados usar.
8. y el cierre es la explicación de nuestros procesos, anticipos, cobros."

"En el tópico 3, no es que yo complemente el programa en ese momento, sino que hago preguntas para analizar después acerca de que espacios complementarios necesitaría."

"Mejor, recuerda que la entrevista es una herramienta para recolectar información para su posterior tratamiento y análisis (bloque2), se trata de recolectar información y brindar información de nuestro trabajo como diseñadores."

### [2026-05-18] - Instrucciones sobre el Procesamiento con IA

"1. El flujo es correcto, solo ten en cuenta los alcances del emprendimiento, en algún lugar ya establecí lo que hacemos y lo que no, es decir, no construimos, no gestionamos, diseñamos, tenemos coadyuvantes. En el cierre además de explicar como trabajamos, también explicamos ligeramente nuestra filosofía, en este caso es automatizar lo técnico y liberar el diseño."

"2. Que tan factible es meter el deepseek flash en la aplicación para que procese las respuestas de la entrevista en el activity matrix y además guía de diseño, similar a lo que se hizo en el apartado de inmersión de la pagina web, es decir relacionar las respuestas del cliente con factores de habitabilidad obtenidos de la psicología ambiental, proxémica, environmental behavior, space sintax, patrones espaciales (alexander), trabajos de post ocupación POE."

### [2026-05-18] - Instrucciones sobre Organización de la Información

"Es importante establecer donde y como se va a poner la información. El análisis de la entrevista debe ser bastante completo, es para los diseñadores y es complemento de la inmersión web, es decir deben ir juntos. No quiero que se sobre satura el Dashboard, es decir ahí van los tópicos y en documento aparte va la información. Tampoco olvidar que cada proyecto va a tener su propia guía."

### [2026-05-18] - Instrucciones sobre Costos de IA

"por el momento no vamos a hacer pruebas que tengan costo hasta el final. Antes quiero profundizar en las preguntas de la herramienta auxiliar."

### [2026-05-18] - Instrucciones sobre las Preguntas de Entrevista

"Si me gusta. utiliza el lenguaje mas natural posible pensando en una conversación entre dos humanos."

### [2026-05-18] - Activity Matrix en Dashboard

"Visualizar la Activity Matrix en el Dashboard: leer de tabla actividades y mostrar grid interactivo con tooltips por hora y habitante."

Se implementó: endpoint `GET /activity_matrix/<temp_id>` en server.py, botón "MATRIZ" en cada lead card, grid de 24h con tooltips y leyenda de zonas SOMA. Los proyectos de la app_inmersion que no están en captura_web se fusionan automáticamente.

### [2026-05-18] - Imágenes de Inmersión

"Buscar imágenes libres de derecho donde se represente lo que queremos decir en las preguntas. Dos ejemplos por cada opción. Pueden ser de arquitectura latinoamericana, inspiradas en patrones espaciales de Christopher Alexander."

Se descargaron 40 imágenes de Unsplash (2 por opción) a `recursos_graficos/Inmersion/`. Se vinculó la variante `_1` en la web. Juan prefiere generar sus propias imágenes y reemplazarlas después.

### [2026-05-19] — Instrucciones sobre Kanban Pipeline
"El kanban está bien, pero no tiene scroll horizontal y se ve oculto a la izquierda."

**Corrección:** Se agregó `overflow-x:auto` al bloque section y al contenedor kanban.

### [2026-05-19] — Instrucciones sobre Programa Arquitectónico (Clave y Relaciones)
"En el generador de programa falta una anotación que explique cuál es la zona 1 al 5."

"Las relaciones solo las puedo poner cuando la lista de espacios esté terminada. En el programa original teníamos acotados esos elementos — la clave se ponía como E{número} (solo el número) y las relaciones se ponían después."

**Implementación:**
- Zona: se agregó leyenda "1=Social · 2=Operativa · 3=Descanso · 4=Soporte · 5=Transición"
- Clave: se cambió a input numérico, se guarda como E{número}
- Relaciones: se movieron a botón 🔗 en cada fila, con mini-modal flotante que solo acepta números separados por coma (ej: 1,3,5)
- El mini-modal es movible (drag) para no tapar la tabla

### [2026-05-19] — Instrucciones sobre Cotización PDF
"No debemos mostrar el precio de los paquetes en la cotización, ni la anotación que 8000 es lo mínimo. El precio por metro cuadrado es un dato interno al igual que el mínimo de precio. Tampoco hay que mencionar la cotización de obra, nosotros no hacemos obra y ese dato ya se lo dimos en el cotizador."

**Implementación:** El PDF de cotización solo muestra:
- Membrete SOMA, datos del cliente, fecha
- Tabla del programa arquitectónico con espacios y m2
- Total de honorarios de diseño
- **NO muestra**: precio por m2, cargo mínimo $8,000, ni estimación de obra

### [2026-05-19] — Activity Matrix (Fallback SQLite)
"no he podido probar la matriz"

**Problema:** El endpoint solo leía de `datos_estructurados.json` (app entrevista). Los leads web no tenían matriz.

**Solución:** Fallback a SQLite. El endpoint ahora consulta `actividades` + `habitantes` cuando no encuentra el JSON. Además se agregó scroll automático a la sección al presionar MATRIZ.

### [2026-05-19] — Cotización PDF: Esquema de Pagos + Vigencia
"consideras que en la cotización deba ir alguna anotación para determinar el tiempo de validez"

**Decisión:** Agregar tabla de esquema 30/40/30 en la cotización PDF + nota de vigencia de 30 días + aclaratoria de que cubre solo diseño, no obra.

### [2026-05-19] — Carta de Presentación SOMA
"Para finalizar con el modelo empresarial me gustaría hacer un documento como especie de carta de presentación, donde aparezca el nombre de la empresa SOMA Taller Virtual de Arquitectura y se redacte los objetivos, misión, visión y valores."

**Decisión:** Crear carta de presentación en MD + HTML editorial con identidad visual de la web (fondo oscuro, Unbounded, acento #bc4b21). Servida desde Flask en `/carta-presentacion`. Firma: Maestro en Arquitectura Juan José Piña May.

### [2026-05-19] - Estrategia de Pagos Agresiva (30/40/30)
"Quiero manejar una estrategia agresiva para ganar la confianza ahora que apenas nos vamos a dar a conocer: anticipo de 30%, primer pago de 40% con entrega de anteproyecto, tercer pago de 30% con entrega final."

**Decisión:** Cambiar de 50/50 a 30/40/30 para reducir la barrera de entrada (30% vs 50%) y alinear pagos con hitos de valor visibles (anteproyecto).

**Implementación:**
- Contrato actualizado con tabla 30/40/30
- Dashboard: botón "Generar 30/40/30" que crea los 3 cobros automáticamente
- Backend: endpoint `POST /cobros/generar_esquema/<id>`
- Forma manual de cobros sigue disponible (colapsada por defecto)

### [2026-05-19] — Imágenes del Carrusel Vertical
"renombre los nombres de las imagenes del carrusel vertial, además veo simbolos extraños en los nombres que les pusiste."

**Problema:** `fileNameFromPath()` usaba `path.split('/').pop()` sin `decodeURIComponent`. El `img.src` devuelve URL codificada (ej. `Cocina%20C.png`), mostrando `%20` en el título.

**Solución:** `decodeURIComponent()` + `.trim()` en `fileNameFromPath`. Además se actualizaron todos los `projectAssets` para coincidir exactamente con los nombres reales en disco (Casa Alina sin sufijos C/L, Casa-Taller Roma con Lateral en vez de Fachada 2, Casona Cristi con Salón/Tragaluz, Hotel Telchac con Andador/Lateral).

### [2026-05-19] — Videos de Fondo No Rotaban
"abri la web6 y no estan pasando todos los videos"

**Problema:** El `<video>` tenía atributo `loop`. Cuando un video terminaba, se repetía infinitamente en vez de disparar `onended`, por lo que la playlist nunca avanzaba.

**Solución:** Eliminar `loop` del HTML + agregar `onloadeddata` para llamar `play()` solo cuando el video está listo. Ahora rotan los 4 correctamente.

### [2026-05-19] — Frases del Hero + Pagina Web 6
"haz una frase mas referente al uso de la IA y centra las frases al eje horizontal de la pagina"

**Implementación:** 
- 4 frases rotativas con fade (Carta de Presentación + IA): "Lo protocolario se programa, lo creativo se libera." / "La arquitectura de alta calidad no debería ser un privilegio." / "El lujo está en los materiales, lo sublime en la creatividad." / "La IA no debe reemplazar el oficio, sino liberar al diseñador para crear."
- Centradas al eje horizontal con flexbox `align-items: center`.
- Se creó `web/Pagina Web 6.html` con todos los arreglos.

### [2026-05-21] — Instrucciones sobre Organización de Procesos (Flujo Correcto)

"después de la recepción y entrevista va el programa sin investigación, después la cotización y después la investigación propiamente dicha."

**Decisión:** El orden correcto del flujo SOMA es:
1. Lead → 2. Entrevista → 3. Programa Arquitectónico → 4. Cotización → 5. Contrato → 6. Investigación (sitio, normativa) → 7. Diseño → 8. Cierre

La investigación de sitio y normativa NO va antes de la cotización; se ejecuta después del contrato, cuando ya hay pago de por medio.

### [2026-05-21] — Instrucciones sobre Diagrama Espacial

"Según yo el diagrama espacial ya lo hicimos, no en el dashboard porque eso es parte del bloque 2 de diseño."

**Decisión:** El Diagrama Espacial SOMA (`DiagramaSoma.html` con vis-network) está completado como herramienta del Bloque 2 (Taller). No debe integrarse al Dashboard — pertenece al proceso de diseño, no a la gestión administrativa.

### [2026-05-21] — Instrucciones sobre la Sección Trayectoria

"Buscaba algo más creativo que hacer un CV listado."

**Decisión:** La trayectoria debe contarse como una progresión de aprendizaje, no como un currículum. Se eligió formato **línea de tiempo vertical** donde cada etapa tiene:
- Años
- Título del rol/institución
- Frase conceptual del aprendizaje (en cursiva)

"enfoque en el aprendizaje relacionando la licenciatura en arquitectura con 'Introducción a la arquitectura y descubrimiento de la forma-espacio-orden', la maestría con 'Desarrollo filosófico y tecnológico' y la carrera profesional con 'Aprendizaje profundo y real con especial énfasis en Duarte Aznar porque allí me dediqué realmente a proyectos'."

### [2026-05-21] — Corrección de Fechas en Trayectoria

- Maestría en Arquitectura UNAM: **2014–2015** (no 2014–2016)
- Proyectista CDMX: **2016–2017** (no solo 2017)

"trabajé 1 año en CDMX, 8 meses en NODO y el resto en Soluciones Señaléticas."

### [2026-05-21] — Instrucciones sobre Email de Contacto

"quita el email nada más."

"En la sección contacto pon el correo de Habitarq85@gmail.com."

**Decisión:** Eliminar `taller@virtual.lab` (placeholder). El email oficial de contacto es `habitarq85@gmail.com`.

### [2026-05-21] — Instrucciones sobre el Layout de Trayectoria

"la línea del tiempo y el título se salen de la pantalla, reduce la línea del tiempo y coloca el título como en las otras secciones."

**Decisión:** 
- Timeline más compacta (30px entre nodos, textos más pequeños)
- Título fuera del contenedor angosto (a ancho completo como las demás secciones)
- Espacio de foto recuperado como columna lateral

### [2026-05-22] - Organización de Bloques: Cada Bloque con sus Herramientas

"Lo que estoy buscando es que cada bloque tenga sus herramientas, lo que tengo duda es de la inforamción compartida por los bloques, donde ubicarla."

"Por ejemplo el dasboard creo que debe estar en la carpeta del bloque 1 y creo que esta bien que la base de datos este en el bloque 3. analiza antes."

**Decisión:**
- Dashboard movido de `dashboard/` (raíz) a `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/`
- Base de datos se queda en `backend/` (Bloque 3)
- Cada bloque autocontenido con sus herramientas. Los bloques solo hablan con el backend (API Flask), no entre sí directamente.
- Patrón validado: B2 ya tiene `DiagramaSoma.html` al lado de sus protocolos; ahora B1 tiene su Dashboard.

### [2026-05-22] — Buyer Persona y Estrategia MKT
"El cliente ideal sería el dueño de casa que construye por primera vez. También me gustaría tener en cuenta a algún cliente de otra parte de Latinoamérica que quiera un proyecto de esos que buscan soluciones por internet y por economía contactan con freelancer de otro país."

**Perfil del Buyer 1:** 30-45 años, profesionista estable, Mérida, primera casa, presupuesto por validar.

**Perfil del Buyer 2:** LATAM remoto, valora proceso y metodología primero, después precio.

**Priorización:** Buyer 1 (local) meses 0-12, Buyer 2 (remoto) prueba mes 6+, Buyer 3 (arquitecto coadyuvante) mes 12+.

**Canales:** Instagram + Google + Recomendación combinados.

### [2026-05-22] — Filosofía vs realidad de accesibilidad
"La idea es arrancar con los clientes posibles y conforme se vaya consolidando empezamos a aplicar los mecanismos de subsidio de tal manera que podamos ofrecer servicios a costo directo para personas que no tengan acceso."

**Decisión:** La democratización no es el punto de partida, es el destino. Fase 1 (0-6 meses): construir estructura. Fase 2 (6-12): probar mecanismo de subsidio. Fase 3 (12-18): primer proyecto subsidiado. Fase 4 (18+): subsidio automático.

### [2026-05-22] — Análisis de precios COTAPAREDES
"Su precio por m2 de diseño es de 400 pesos en 2019 donde si hacemos una comparación con sus paquetes él cobra 50% para su paquete básico, 65% su paquete integral y 100% su paquete ejecutivo."

**Conclusión:** Con inflación 2019-2026 (~45%), los precios equivalentes serían: básico $290/m², integral $377/m², ejecutivo $580/m². SOMA está a $250/$400/$1,000. El Esencial está bien para arrancar — no bajarlo. El salto a Ejecutivo necesita justificarse bien.

### [2026-05-22] — Convenio de anticipo y pagos
"Debemos preparar un contrato para el anticipo y los pagos, para irlos firmando con el cliente."

**Decisión:** Se creó CONVENIO_ANTICIPO_PAGOS.md (versión práctica de 1 hoja) + RECIBO_PAGO_PARCIAL.md para pagos 2 y 3. El contrato completo ya existía.

### [2026-05-22] — Valor legal de los contratos
"¿Qué vinculación real tienen estos contratos por si el cliente firma que va a pagar la liquidación de los trabajos y no lo hace?"

**Decisión:** El contrato es simbólico para montos de diseño residencial. Demandar no es rentable. La protección real es: (1) cobrar antes de entregar (30/40/30), (2) no soltar archivos editables hasta el último pago, (3) elegir clientes confiables. El pagaré formal no se implementa aún, queda pendiente.

### [2026-05-22] — Corrección de interpretación de Filosofía
"El lujo está en los materiales y el detalle, lo sublime está en la creatividad y el mensaje significa que la arquitectura puede tener materiales de lujo con detalles muy finos pero también puede tener materiales sencillos y rústicos, lo que las hace arquitectura es que comunican un mensaje sublime con creatividad de manera clara, estética y honesta."

**Corrección:** No es "el lujo está en los materiales, lo sublime en la creatividad" como dos opciones separadas. Es: los materiales (lujosos o sencillos) son el vehículo, lo sublime es el mensaje que comunican. Ambos coexisten. No se trata de elegir entre lujo y sencillez — se trata de que cualquier material, bien usado, puede transmitir un mensaje sublime.

- [ ] **RECORDATORIO:** Cuando la web esté publicada, recordar a Juan que active Google My Business (guía en Bloque 4/GOOGLE_MY_BUSINESS.md) y agregue el sitio web al perfil.

### [2026-05-25] — Ajustes y Correcciones en Página Web

"cambiar la foto de trayectoria, aqui esta la imagen /home/juan/Documentos/PROYECTO SOMA/recursos_graficos/Foto trayectoria/"

**Decisión:** Usar `retrato final.png` (1264x2048) en lugar del placeholder. Recortar 20% superior con `object-fit: cover` + `object-position: 50% 100%`.

"vamos a eliminar por el momento el video filosófico y vamos a pasar el carrusel de conceptos al centro y un poco mas grande."

**Decisión:** Video placeholder eliminado. Carrusel agrandado (400px slides) y centrado con padding lateral. Velocidad reducida.

"el boton de finalizar en la inmersión a veces no funciona, podrías revisarlo"

**Decisión:** Agregar AbortController con timeout de 3s al fetch para evitar que se trabe si el servidor no responde. Protección contra doble clic.

"en la portada quiero modificar la frase 'la arquitectura de alta calidad no debería ser un privilegio' dame opciones menos agresivas"

**Decisión:** Nueva frase: "Que la buena arquitectura no sea la excepción, sino el punto de partida."

"en el apartado filosofía la parte de la frase: No necesitamos lujos para que la arquitectura de alta calidad exista y llegue a todos. quiero reformular esa parte por otra opción menos agresiva"

**Decisión:** Nueva frase: "La calidad en la arquitectura no está en el costo, sino en la claridad del mensaje."

"se repite mucho la palabra mensaje, en la frase anterior, deja los sublime esta en la creatividad."

**Decisión:** La frase completa: "El lujo está en los materiales y en el detalle, pero lo sublime está en la creatividad. La calidad en la arquitectura no está en el costo, sino en la claridad del mensaje."

### Próxima Sesión
- Automatización de Impuestos: Cálculo ISR/IVA, CFDI, reportes fiscales (requiere RFC).
- Probar la app de entrevista en celular real (grabación de audio).
- Instalar faster-whisper para transcripción local (cuando haya mejor conexión).
- Configurar DEEPSEEK_API_KEY para activar el análisis automático (sin costo hasta agotar crédito gratuito).
- Registro RFC de Juan en RESICO para emitir CFDI.
- Implementar PROTOCOLO_VISUALIZACION.md, plantilla_dossier.html, PROTOCOLO_EVALUACION.md.

---

## [2026-05-28] — Sesión: Landscape responsive + SMTP Railway

"DEBE SER LA DOBLE VERIFICACIÓN, BORRE UNA POR ERROR, AHORA LO CHECO Y TE AVISO."

"VEO UN PROBLEMA EN LA PAGINA, EN CELULAR VERTICAL SE VE BIEN, EN MONITOR DE LAPTOP SE VE BIEN, PERO EN CELULAR HORIZONTAL SE CORTAN LAS IMAGENES, COMO PODEMOS SOLUCIONARLO"

**Decisión:** Nueva media query `max-height: 520px` para landscape. Hero mantiene 100vh, demás secciones auto-height.

"La portada se reduco a la mitad y aparece el letrero de proyectos, ya no hay recortes pero los titulos de las imagenes del carrusel quedan muy encimadas a la imagen. Conviene hacer la actualización en la pagina web 6 antes de actualizarlo en github para no estar recargando a cada rato? o es indiferente."

**Decisión:** Sí, editar local y probar antes de push. Se corrigió selector a `section + section` para no afectar el hero. Slide titles más pequeños en mobile.

"Sigue la portada con los videos recortada como si fuera una banda superior."

**Bug:** El selector `section { min-height: auto; height: auto; }` colapsaba la altura del hero, el video se veía como una banda. **Fix:** `section + section` aplica solo a secciones después de la primera.

"correcto, ya quedo pasalo al github y rainway"

"Pusiste al dia el snapshot y el soma_core_index y pusiste mis instrucciones literales en SOLOJUAN."

### [2026-05-28] — Sesión: Cotizador (single POST) + Responsive landscape/portrait + Imágenes comprimidas

"el cotizador manda la info dos veces, una en el paso 12 y otra en el 15, debe ser solo al final."

**Decisión:** Se eliminó el fetch de `registerContact()` (paso 12). Ambos pasos (12 y 15) llaman a `finishImmersion(this)` como único punto de guardado. El POST a `/save_immersion` ocurre una sola vez.

"en celular vertical, el título del hero se ve en medio, debería estar en el tercio superior. también el overlay está muy claro."

**Decisión:**
- Hero `padding-top: 15vh` para subir el título al tercio superior
- Overlay más oscuro: `rgba(10,10,10,0.7) → rgba(10,10,10,0.95)`
- Proyectos centrados verticalmente con `justify-content: center`
- Títulos del carrusel en mobile: `bottom: 8px`, landscape: `bottom: 0` con padding mínimo

"en celular horizontal las imágenes del portafolio se ven recortadas y el carrusel de filosofía no desliza horizontal."

**Decisión:**
- Modal portafolio en landscape: `display: flex; flex-direction: column`
- `view-center { flex: 1 }` para que la imagen ocupe el espacio disponible
- `view-side { height: 70px }` miniaturas más pequeñas
- Carrusel filosofía forzado horizontal con `!important`: `flex-direction: row; flex-wrap: nowrap; overflow-x: auto`

"en servicios, la imagen se ve separada de la lista, deberían ir juntas."

**Decisión:** HTML reestructurado: `.services-row` envuelve `<ul>` + `.services-visual`. El contacto queda debajo del row. Desktop `grid-template-columns: 1fr 260px`, mobile `1fr auto`, landscape `1fr auto`. Altura base del visual: 220px.

"en trayectoria, en portrait se ve muy plana la foto, necesita un efecto de viñeta."

**Decisión:** `::after` en portrait con `box-shadow: inset 0 0 30px 15px rgba(10,10,10,0.7)`. Texto "M. en Arq." en una sola línea en timeline y bajo la foto.

"quita la diapositiva de 'CALIDAD SIN JERARQUÍAS' del carrusel de filosofía, y agrega una flecha que indique que se puede deslizar en celular."

**Decisión:** Slide 7 eliminado del carrusel. Agregada flecha `→` con animación pulse en mobile, con máscara gradient fade al final del carrusel.

"agrega el WhatsApp en la sección de contacto."

**Decisión:** "WhatsApp: 999 531 4093" agregado en la sección Contacto.

"comprime las imágenes para que pesen menos."

**Decisión:** 110 imágenes comprimidas con Pillow (quality 80 JPG, 70 WebP). 49 MB → 44 MB. Videos no comprimidos (ffmpeg no instalado). Commit `0531ffe` subido a GitHub.

### Próxima Sesión
- **Bug 1:** En celular horizontal no se ve el botón cotizador (revisar z-index, overflow, posición del modal).
- **Bug 2:** La página se traba en "Enviar" — el fetch a `/save_immersion` cuelga sin respuesta; falta timeout/catch en el cliente.

---

## [2026-05-29] — Sesión: Video crossfade, SendGrid, Landscape compact, Immersion images

### Video
"más obscuro todavía" (x4 — progresión 0.4 → 0.5 → 0.45 → 0.40)

### Cotizador Email
"no se pudo conectar con el servidor. tus datos se perderán"

**Decisión:** Timeout cliente 5s → 20s. SMTP seguía fallando en Railway.

"error 101 network is unreachable"

**Decisión:** Railway bloquea todos los puertos SMTP (465, 587, 25). Migrar a SendGrid (API HTTP, puerto 443).

"sigue dando error. lo que hice fue cambiar el port 465 por 587 y modificar el ssl a false"

"es de twilio?" (sobre SendGrid)

"me pide domain" (al configurar SendGrid)

**Decisión:** Usar Single Sender Verification (no Domain). Verificar `habitarq85@gmail.com`.

"que pongo en sender verification"
"digo en sender autentication" (sic)

**Campos:** From Email `habitarq85@gmail.com`, From Name `SOMA Arquitectura`, Reply To `habitarq85@gmail.com`, Address dirección física, City Mérida, State Yucatán, Country Mexico.

"ok que mas"

**API Key creada:** `SG.<redactado>`

*(Nota: la API key real solo está en .env local y Railway env vars. No pushear a GitHub.)*

"OK, VOY A PROBAR"

"DICE INMERSIÓN REGISTRADA TE CONTACTAREMOS PRONTO, PERO NO LLEGÓ EL CORREO"

"SI SE FUE A SPAM, COMO EVIAR QUE SE VAYA AHI"

**Decisión:** Marcar como "No es spam" por ahora. Para arreglarlo de raíz: autenticar un dominio en SendGrid (Settings → Sender Authentication → Domain Authentication).

"Parece que ya quedo !!!!"

"actualiza la bitacora y todos los documentos del proyecto, entiendo que la pagina web6 local tambien esta actualizada."

### Landscape Mobile (Contacto invisible)
"en celular horizontal no se ve el contacto" (reporte de sesión anterior)

**Decisión:** Compactación máxima para que quepa sin scroll:
- Imagen servicios 120px → 90px
- Fuentes reducidas a 0.45rem
- Grid gaps a 4px
- Timeline compacto
- Removido `display: inline !important` del h2

### Immersion Images
"las imagenes aparecen cortadas, no respetan su proporción, podrías resolverlo"

**Decisión:** En 480px → `object-fit: contain; height: auto; max-height: 200px`. En 768px → `max-height: 180px`. Imágenes completas sin recorte.

### Desktop Section Contacto
"la imagen de la pagina ya quedó, ponlo como ito del proyecto"

**Decisión:** `section:last-of-type` centrada como las demás. Título Contacto hereda h2 global. Textos alineados con servicios via `padding-left: 25px`.

"Actualizaste SOLOJUAN CON MIS INSTRUCCIONES LITERALES DE LA SESIÓN?"

### Próxima Sesión
- **[MEDIA] Autenticar dominio** en SendGrid para que correos no caigan en spam.
- **[MEDIA] Confirmar landscape mobile** en vivo.
- **[ALTA] RFC en RESICO** — sin factura no hay cobro formal.
- **[ALTA] Primer cliente real** — validar el ciclo completo.
- **[ALTA] Dominio propio** — `soma.onrender.com` no inspira confianza.
- **[MEDIA] Migrar a PostgreSQL** — SQLite se pierde al reiniciar Railway.

---

## [2026-06-02] — Sesión: Precios v3.0, UX cotizador, scroll reveal, fixes

### Nueva Escala de Precios Oficial (SOMA v3.0)
- **SOMA Esencial:** $250/m² (se mantiene)
- **SOMA Integral:** $350/m² (bajó de $400)
- **SOMA Ejecutivo:** $850/m² (bajó de $1,000)
- **Cargo mínimo operativo:** $6,500 (bajó de $8,000)

"El mínimo del taller va a ser 6,500. El precio integral va a ser 350 por metro cuadrado. El paquete ejecutivo va a ser 850 por metro cuadrado."

### Programa arquitectónico — Espacios mínimos
"Aquí están los espacios con dimensiones mínimas funcionales + factor 1.35 ya aplicado [...] El de la cochera utiliza el de 2 autos, los demás si modifícalos."

**Decisión:** Los valores de programa se cambiaron a mínimos funcionales con 1.35 integrado. Cochera 30m² (2 autos). Se eliminó `* 1.35` del JS para no duplicar.

### Quote-type tabs
"En el cotizador, en el apartado cotizador parámetros, necesito que estén visibles los tres tipos que pueden ser marcado con negritas el que está activo, ejemplo esta activo por programa, en transparentes los que no están activos."

**Decisión:** `<select>` reemplazado por 3 botones tipo tab. Activo: acento + negrita + fondo tenue. Inactivos: gris translúcido.

### Botón volver unificado
"haz el botón volver de las preguntas similar al botón volver del cotizador parámetros escala e inversión, es decir su flecha y tamaño de letra."

**Decisión:** Todos los `.btn-back` ahora estilo `transparent + border #333 + font-family JetBrains Mono` con texto `← volver` y centrados abajo.

### Scroll reveal filosofía + bidireccional
"haz que se encienda uno y se apague el otro así cuando subes y bajes lo ves animado igual en el apartado proyectos."

**Decisión:** `classList.toggle('revealed', entry.isIntersecting)` en vez de solo `add()`. Filosofía con `opacity: 0.5; transform: translateX(-15px)` → revelado.

---

## [2026-06-02] - Hacia el Algoritmo SOMA y Organización de Proyectos

### Sobre la documentación del proceso
"y es que realmente apenas estoy asentando mis procesos en /04 Proyectos/Proyecto 1/ para que luego busquemos los patrones y alcancemos el algoritmo"

**Decisión:** Flujo inductivo. Documentar primero el proceso real empírico (`CONTENIDO-DISEÑO` de 17 pasos), para luego decantar y refinar la teoría, en lugar de forzar la teoría sobre la práctica. Se generó `FUSION_CONCEPTUALIZACION.md`.

### Sobre el concepto de "Algoritmo de Diseño"
"Y mas que un check list es un algoritmo soma de diseño, es decir que podamos identificar las variables, y con recursos de programación y por cada etapa hasta que siguiendo el algoritmo tengas un entregable."
"esacto, esa es la idea de la automatización soma, una guía logica, la creatividad esta adentro, es un nodo."
"que creo tiene que ser visual porque es para el diseñador, que sepa que pasos debe seguir y ya con que estilo o mensaje sea propio."

**Decisión:** Evolucionar de "Rutas" a "Algoritmo". SOMA no te dice *qué* diseñar (creatividad = nodo), sino *cómo procesar* la información (variables de entrada → pasos lógicos → entregable). Deberá ser un mapa visual nodal para el diseñador.

### Sobre la organización de carpetas
"Como es mejor para organizar carpetas... opción 1 analisis de sitio - proyecto alina, proyecto telchac, opción 2 - proyecto alina - analisis de sitio, analisis de usuario, etc."
"En análisis tengo varios materiales, ejemplo relaciones espaciales, analisis del usuario, analisis del sitio, etc. como me conviene ordenarlo si es de diferentes tipos de material."

**Decisión:**
1. Estructura por Proyecto (Opción 2), no por especialidad. Favorece el contexto y poder comprimir/enviar un proyecto autónomo.
2. Un solo documento para investigación en crudo (`expediente_sitio.md`), pero un documento de síntesis directiva (`guia_diseno.md`).
3. Agrupar todo el análisis en una sola carpeta usando prefijos numéricos (`01_analisis_usuario.md`, `01_usuario_matrix.png`, etc.) sin separar por formato de archivo, para contar la historia secuencialmente.

---

### Próxima Sesión
- Dashboard apunta a `localhost:8080` — reconectar cuando se migre a Render (pendiente).
- Trazar las variables globales del Algoritmo SOMA y su mapa visual basado en la fusión lograda hoy.

---

## [2026-06-08] — PROCESO DE DISEÑO 2.0 + Biblioteca SOMA

### Expansión del PROCESO DE DISEÑO
"El PROCESO DE DISEÑO original (143 líneas) debe expandirse a especificación completa con INPUT/OPERA/OUTPUT/PROC para cada item."

**Decisión:** Se creó `PROCESO DE DISEÑO 2.0` (~1614 líneas) con:
- Cada item clasificado por naturaleza: `[REF]` (buscar/referenciar), `[OUT]` (generar), `[DEC]` (decisión humana), `[ACC]` (acción técnica), `[EVA]` (evaluar), `[GUI]` (consultar/guía)
- Cada item asignado a procesador: `AI`, `HUMANO`, `AI→HUMANO`, `HUMANO→AI`
- Citas inline con referencias al final
- Cross-references a protocolos existentes

**Regla confirmada:** Sección 2 (Investigación) outputea solo raw files. Sección 3 (Análisis) los procesa. No mezclar.

"5.10 debe ser AI→HUMANO (el humano decide). 2.2.3 debe ser AI (automatizable: búsqueda de normativa de fraccionamiento). Los items de Sección 2 que requieren decisión humana deben ser HUMANO o AI→HUMANO, no AI."

### Biblioteca SOMA
"La biblioteca es el repositorio central de fuentes. El primer proyecto descarga, los siguientes copian de la biblioteca. No duplicar esfuerzo."

**Decisión:** Biblioteca creada en `/biblioteca/` con 6 carpetas:
- `normativas/` — PDFs descargados (Reglamento, NTC, NOMs, planes)
- `clima/` — cartas solares y rosa de vientos generadas por script + índice
- `diseno/` — solo referencias (Neufert, Panero, Ching — copyright, no descargar)
- `arquetipos/` — índice de recursos open-access (AI busca, humano decide)
- `repertorio/` — proyectos de referencia filtrados (AI compila, humano cura)
- `patrones/` — catálogo SOMA de 42 patrones + 34 Alexander mapeados (AI→HUMANO)

**Copyright:** "Neufert, Ching, Panero, Alexander no se descargan. Solo referenciar con ISBN y lugar de consulta."

**CONAGUA:** "El sitio SMN bloquea descargas automáticas. Usar link directo + tabla resumen en su lugar."

### Flujo de trabajo AI→HUMANO
"Para el catálogo de patrones: AI hace el borrador inicial (42 patrones), humano cura y ajusta por proyecto. Es documento vivo."

"Para arquetipos: AI busca recursos académicos open-access. humano decide cuáles usar."

"Para repertorio: AI compila proyectos candidatos filtrados por clima/tipo. humano selecciona."

**Próxima sesión:** Revisar protocolos contra 2.0, mapear items a codebase, integrar biblioteca en template de proyecto.

---

## [2026-06-09] — Migración a Render + PostgreSQL + Dominio

**Decisión:** Migrar de Railway a Render por el PostgreSQL gratis y 750h/mes. Dominio `soma-arquitectura.com` registrado en Cloudflare. Email profesional via Cloudflare Email Routing → Gmail. SendGrid autenticado con dominio propio.

"La web ya está en producción con dominio propio. Ahora toca conseguir clientes."

### Nuevos Pendientes Priorizados
1. **Cerrar 1 cliente real** — probar el ciclo completo
2. **RFC en RESICO** — sin factura no hay cobro formal
3. **Dashboard con login** — proteger `/dashboard` con contraseña
4. **faster-whisper + DeepSeek** — automatizar análisis
5. **Tiempos de entrega** — definir tabla en TIEMPOS_ENTREGA_BASE.md

