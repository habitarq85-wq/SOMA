# PROTOCOLO DE ANÁLISIS
## Bloque 2 — Taller SOMA (Operación)

### Diferencia entre Investigación y Análisis

| Fase | Qué se hace | Pregunta que responde | Producto |
|------|------------|----------------------|----------|
| **Investigación** | Se recolectan datos brutos del sitio, usuario, clima y contexto | ¿Qué hay? | Checklist de datos, registro fotográfico, planimetría raw |
| **Análisis** | Se procesan esos datos para extraer patrones, conflictos y oportunidades de diseño | ¿Qué significa? ¿Qué hacer con eso? | Estrategias de diseño, diagramas, matrices, constraints |

**Regla:** No se puede analizar lo que no se investigó. Todo análisis parte de un dato
recolectado en la fase de investigación.

---

## 1. ANÁLISIS DE SITIO

*Entrada: Datos del PROTOCOLO_INVESTIGACION_PREVIA.md (topografía, dimensiones,
vegetación, infraestructura).*

### 1.1 Volumetría Regulatoria (Bounding Box)

- [ ] A partir de COS: calcular el área máxima de desplante (ej: 600 m² × 0.40 = 240 m²).
- [ ] A partir de CUS: calcular el área máxima construible total.
- [ ] A partir de restricciones: trazar la envolvente máxima edificable en planta.
- [ ] A partir de altura máxima: definir cuántos niveles caben.
- [ ] Trazar el **polígono de construcción permitido** en un plano del predio.
- [ ] Identificar zonas "muertas" donde no se puede construir pero se puede
      aprovechar (jardines, patios, estacionamiento).

*Salida: Plano de Bounding Box con el volumen máximo legal.*

### 1.2 Mapa de Conflictos Sitio-Diseño

- [ ] Cruce de topografía + COS: ¿la pendiente afecta el desplante?
- [ ] Cruce de vegetación + Bounding Box: ¿hay árboles a conservar dentro del
      polígono construible?
- [ ] Cruce de infraestructura + diseño: ¿la acometida eléctrica/agua está donde
      la necesito? ¿hay que reubicar el acceso de servicio?
- [ ] Cruce de acústica + zonificación: ¿las fuentes de ruido afectan la ubicación
      de recámaras?
- [ ] Cruce de visuales + orientación: ¿la mejor vista coincide con la peor
      orientación solar? ¿qué gana: la vista o el confort?

*Salida: Matriz de conflictos con prioridad (rojo = resolver en diseño,
amarillo = monitorear, verde = sin conflicto).*

### 1.3 Diagrama de Aprovechamiento del Predio

- [ ] Dibujar el soleamiento por hora sobre el polígono construible.
- [ ] Dibujar las franjas de viento dominante.
- [ ] Identificar el **área premium**: zona con mejor combinación de orientación N,
      viento NE, buena vista y acceso.
- [ ] Identificar el **área de servicio**: zonas calientes (E/O), ruidosas, sin vista.
- [ ] Proponer una primera macro-zonificación del predio (construcción, jardín,
      acceso, servicio).

*Salida: Diagrama de macrolocalización de usos en el predio.*

---

## 2. ANÁLISIS DEL USUARIO

*Entrada: Datos de entrevista (PROTOCOLO_02_ENTREVISTA + App puerto 5050)
e inmersión web (10 ejes visuales).*

### 2.1 Perfil de UserEntity

Para cada habitante registrado:

| Dato de investigación | Análisis |
|----------------------|----------|
| Edad y salud | Necesidades de accesibilidad, alturas de muebles, riesgo de caídas |
| Ocupación | Espacios requeridos (oficina, taller, recepción de visitas) |
| Hobbies | Mobiliario especial, almacenamiento, área dedicada |
| Horarios en casa | Actividad Matrix, conflictos de uso simultáneo |
| Rol de poder | Quién decide estética vs función, prioridades de diseño |

- [ ] **Mapa de convivencia:** ¿quién coincide con quién en cada hora? Identificar
      momentos de alta demanda simultánea (baños mañana, cocina mediodía).
- [ ] **Perfil de privacidad:** ¿cada habitante necesita aislamiento o integración?
      Cruzar con la ActivityMatrix.
- [ ] **Perfil sensorial:** ¿prefieren luz natural o tenue? ¿sonido de la calle o
      silencio absoluto? ¿texturas frías o cálidas?

*Salida: Fichas de UserEntity por habitante + tabla de conflictos de convivencia.*

### 2.2 Perfil de Diseño (10 Ejes de Inmersión)

Los 10 ejes A/B de la web se procesan así:

- [ ] **Polaridad dominante:** ¿el proyecto tiende más a A o a B? Promedio general.
- [ ] **Ejes definitorios:** ¿cuáles ejes tuvieron respuesta más extrema (0–2 o 8–10)?
      Esos son los que dictan el carácter del proyecto.
- [ ] **Ejes neutros:** ¿cuáles quedaron en 4–6? Se pueden resolver por contexto
      o por decisión del diseñador.
- [ ] **Coherencia interna:** ¿hay ejes contradictorios? (ej: fachada muy abierta
      pero perfil social muy privado → conflicto que debe resolverse en diseño).
- [ ] **Traducción a partido arquitectónico:**
  | Eje | Si va a A | Si va a B |
  |-----|-----------|-----------|
  | Fachada | Fachada abierta, vanos generosos | Fachada maciza, vanos controlados |
  | Privacidad | Recibidor visual, gradación | Transparencia total desde entrada |
  | Planta | Planta libre, límites virtuales | Espacios definidos por muros |
  | Iluminación | Ventanas amplias, luz directa | Luz tamizada, tragaluces |
  | Tacto | Acabados texturizados (piedra, madera) | Superficies lisas (concreto pulido) |
  | Niveles | Un piso + losa | Dos o más niveles |
  | Paisaje | Jardín, vegetación, agua | Patio duro, piedra, grava |
  | Escala | Espacios íntimos, escala humana | Espacios amplios, doble altura |
  | Perfil Social | Zonas sociales integradas | Recámaras aisladas, circulación separada |
  | Color | Acentos de color en muros o mobiliario | Neutros (blanco, gris, beige) |

*Salida: Perfil de diseño del proyecto con 3–4 ejes definitorios.*

### 2.3 CreativeCore (5 Ejes de Tensión)

Procesar las respuestas del Tópico 6 de la entrevista:

- [ ] **Tensión/Calma:** ¿el proyecto busca ser un refugio de calma o un espacio
      de energía y dinamismo?
- [ ] **Brutalismo/Refinamiento:** ¿materiales expuestos y crudos o acabados
      cuidados y sofisticados?
- [ ] **Privacidad/Transparencia:** ¿la relación con el exterior es de apertura
      o de protección?
- [ ] **Ortogonalidad/Organicismo:** ¿geometría clara y ordenada o formas libres
      y curvas?
- [ ] **Permanencia/Efimeridad:** ¿materiales que envejecen con dignidad o
      livianos y cambiables?

- [ ] **Mensaje poético:** Redactar una frase que capture la intención del proyecto
      (ej: "Una casa que abraza el jardín como extensión de la sala").
- [ ] **Adjetivo rector:** Una sola palabra que defina la experiencia espacial
      (paz, poder, orden, libertad, refugio, encuentro).

*Salida: CreativeCore del proyecto (5 posiciones + mensaje poético + adjetivo rector).*

---

## 3. ANÁLISIS BIOCLIMÁTICO

*Entrada: Datos climáticos de investigación (temperatura, humedad, vientos,
asoleamiento).*

**Diferencia clave:** La investigación registra "el sol sale por el E y se pone
por el O, la temperatura media es 26°C". El análisis responde "qué hago con eso".

### 3.1 Carta Solar y Estrategia de Orientación

- [ ] **Gráfica de trayectoria solar:** Dibujar el recorrido del sol sobre el
      polígono construible en solsticio de verano e invierno.
- [ ] **Horas de sol directo por fachada:** Calcular cuántas horas recibe sol
      directo cada orientación en verano.
- [ ] **Asignación de usos por orientación:**
  - **Norte:** Recámaras, estudio, sala (máximo confort, mínima ganancia).
  - **Sur:** Aleros profundos. Comedor, circulaciones (sol alto controlable).
  - **Este:** Baños, cocina, desayunador (sol matutino, se calientan temprano
        pero se enfrían en la tarde).
  - **Oeste:** Servicio, bodega, muros ciegos o con protección pesada
        (el sol de la tarde es el más agresivo).
- [ ] **Estrategia de protecciones:**
  - Profundidad de alero necesario en cada fachada según la latitud (20.97°N).
  - Selección de tipo: volado fijo, brise-soleil horizontal/vertical,
        celosía, vegetación, pérgola.
  - Decidir si la protección es fija (alero) o móvil (persiana, louver
        operable) según uso del espacio.

*Salida: Diagrama de orientación con asignación de usos y tipo de protección
por fachada.*

### 3.2 Estrategia de Ventilación

- [ ] **Rosa de vientos del sitio:** Procesar datos de dirección y velocidad
      de viento dominante.
- [ ] **Zonas de presión (+)** y **succión (-):** Identificar qué fachadas están
      a barlovento (+) y sotavento (-) según viento dominante.
- [ ] **Trazado de ejes de ventilación cruzada:** Dibujar flechas que atraviesen
      los espacios propuestos, conectando fachada de alta presión con fachada
      de baja presión.
- [ ] **Relación de área de entrada/salida:** La salida debe ser igual o mayor
      que la entrada para que el flujo sea eficiente. Si la entrada es 2 m²,
      la salida debe ser ≥2 m².
- [ ] **Decisión de vanos por fachada:**
  - Barlovento (NE): ventanas mayores, louvers fijos.
  - Sotavento (SO): ventanas menores o iguales, operable.
  - E y O: ventanas pequeñas con protección pesada o inexistentes.
- [ ] **Estrategia de ventilación nocturna:** ¿se pueden abrir todas las ventanas
      de forma segura por la noche? ¿Cómo se evitan mosquitos? (mallas
      mosquito en todas las ventanas operables).

*Salida: Diagrama de ventilación con flechas de flujo, tamaño de vanos por
fachada y ubicación de louvers/mallas.*

### 3.3 Selección de Estrategias Pasivas

- [ ] De la tabla de estrategias bioclimáticas (Investigación 4.9), seleccionar
      las que aplican según el análisis de orientación y ventilación.
- [ ] **Cubierta:** ¿cool roof, techo ventilado, doble altura, techo verde?
      Decisión basada en presupuesto y tipo de losa.
- [ ] **Muros:** ¿masa térmica (concreto), doble hoja con aislamiento, o
      bajareque/madera regional?
- [ ] **Patio:** ¿patio interior como pulmón térmico? ¿abierto al N o al S?
- [ ] **Vegetación:** ¿árboles caducifolios al E/O? ¿trepadoras en pérgolas?
- [ ] **Chimenea solar:** Conducto vertical pintado de negro al sol. Acelera el tiro
      por convección, succiona el aire caliente. ¿Vale la pena según el presupuesto?
- [ ] **Pozo canadiense (geotermia somera):** Tubo enterrado a ~2 m que templa el
      aire antes de entrar (reduce 4–6°C). Inversión mayor, efectivo pero costoso.

#### Tabla de Estrategias Bioclimáticas

| Estrategia | Beneficio estimado | Costo relativo | Cuándo aplica |
|------------|-------------------|----------------|---------------|
| Cool roof (techo reflectante) | -3.14°C interior [UADY, 2020] | Bajo | Techos con exposición solar directa |
| Techo ventilado (doble cámara) | -2°C adicional [UADY, 2020] | Medio | Losas de concreto, cubiertas inclinadas |
| Doble altura en espacios clave | -1.22°C [UADY, 2022] | Medio | Salas, comedores, circulaciones |
| Aleros profundos (>1.00 m) | Reduce ganancia solar directa | Bajo | Fachada S y E |
| Ventilación cruzada NE-SO | Enfriamiento pasivo continuo | Bajo | Toda vivienda en Mérida |
| Celosías / brise-soleil | Bloquea sol, permite viento | Medio | Fachadas E y O |
| Patio interior como pulmón | Ventila + organiza la casa | Medio | Predios grandes o medianos |
| Vegetación regional en E-O | Microclima, sombra, frescura | Bajo | Espacio exterior disponible |
| Muros doble hoja con aislamiento | Aísla térmica y acústicamente | Alto | Muros E, O y ruidosos |
| Pozo canadiense (geotermia) | Templa aire 4–6°C | Alto | Presupuesto elevado |
| Chimenea solar | Extrae aire caliente por cubierta | Bajo | Techos inclinados o losas |

**Recomendación general:** Combinar mínimo 3-4 estrategias de bajo costo antes
de recurrir a A/C. La triada óptima para Mérida: cool roof + ventilación cruzada
+ aleros profundos.

*Salida: Ficha de estrategias pasivas seleccionadas con justificación de cada
decisión.*

### 3.4 Zonificación Térmica del Proyecto

- [ ] Dividir la planta en zonas según necesidad de enfriamiento:
  - **Zona A (confort natural):** Recámaras N, sala N, circulación.
        Sin A/C, solo ventilación natural.
  - **Zona B (confort híbrido):** Comedor, cocina, estudio.
        Ventilación natural + respaldo de A/C (minisplit).
  - **Zona C (confort asistido):** Baños, lavado, servicio.
        Ventilación mecánica básica (extractor).
- [ ] Separar las zonas A de las C con circulaciones o espacios de transición
      para evitar pérdida de confort.

*Salida: Plano de zonificación térmica con colores por tipo de confort.*

### 3.5 Ciclo Diario de Aperturas (Operación Pasiva)

*Cómo usar la arquitectura según la hora del día. Esto se entrega al cliente como
parte del manual de uso de la vivienda.*

| Horario | Acción | Efecto |
|---------|--------|--------|
| **6:00–9:00** | Abrir ventanas al NE. Ventilación cruzada total. | Renovar el aire nocturno acumulado, enfriar masa térmica. |
| **9:00–12:00** | Cerrar ventanas del E. Iniciar cierre de persianas en fachada E. Mantener abierto el N. | Evitar que el sol de media mañana caliente los espacios. |
| **12:00–17:00** | Cerrar todo. Solo micro-aperturas al N. Persianas, celosías y aleros trabajando al máximo. | Aislar del pico de calor. La doble altura mantiene convección sin abrir. |
| **17:00–19:00** | Cerrar protecciones del O. Abrir ventanas del NE y S. | El aire exterior se enfría, iniciar ventilación nocturna. |
| **19:00–6:00** | Ventilación cruzada abierta al máximo (con mallas mosquito). | El aire nocturno enfría la masa térmica para el día siguiente. |
| **Purga extrema** | Abrir TODO 10–15 min al amanecer. | Expulsar el aire caliente acumulado en días extremos. |

Ajustar por temporada: en invierno ("nortes") reducir apertura al mínimo;
en suradas (primavera) mantener cerrado.

*Salida: Tabla de horarios de apertura para incluir en el manual de usuario.*

### 3.6 Estrategias para Extracción de Malos Olores

*Análisis de cómo diseñar la ventilación para evitar que los olores se concentren
o migren a espacios nobles.*

#### Flujo de aire limpio → sucio

- [ ] **Recorrido del aire:** El flujo debe ir siempre de lo más limpio a lo más sucio:
      recámaras → sala → cocina → servicio → exterior.
- [ ] **Presurización de espacios nobles:** Las recámaras y sala deben estar en
      barlovento (entra más aire del que sale). Los servicios en sotavento
      (las salidas de aire/extractores jalan los olores hacia afuera).
- [ ] **Evitar que el aire pase de cocina a recámaras.**

#### Baños

- [ ] **Ventilación natural directa:** Siempre que sea posible, baño con ventana al
      exterior orientada al viento dominante. Apertura ≥5% del área del piso.
- [ ] **Pozo de ventilación (ducto):** En baños sin ventana exterior, pozo vertical
      a cubierta con efecto chimenea. Diámetro mínimo 15 cm. Sombrerete de
      extracción estática (turbina eólica pasiva) en la salida.
- [ ] **Ubicación:** Baños cerca de muros exteriores para minimizar ductos. No
      enterrar baños en el centro de la planta sin ventilación.
- [ ] **Extractor mecánico de respaldo:** Con temporizador (5–10 min después de
      apagar la luz). Solo cuando la ventilación natural es insuficiente.

#### Cocina

- [ ] **Campana extractora con salida al exterior:** Obligatoria. Ducto independiente,
      liso, diámetro mínimo 15 cm, tramo horizontal lo más corto posible.
      La recirculación (carbón activado) no elimina humedad ni grasa.
- [ ] **Ventilación natural cruzada:** Ventana en cocina que genere corriente con
      otra apertura (puerta, patio de servicio).
- [ ] **Despensa:** Ventilación permanente (reja o louver en la parte superior de
      la puerta).

#### Áreas de servicio

- [ ] **Tendedero con ventilación cruzada obligatoria** (entrada y salida de aire).
- [ ] **Bodega / cuarto de limpieza:** Louver permanente en puerta o rejilla de
      ventilación alta.
- [ ] **Separación de la cocina:** El olor a humedad del lavado no debe mezclarse
      con alimentos.

*Salida: Diagrama de flujo de aire con direcciones y ubicación de extractores.*

---

## 4. ANÁLISIS CONTEXTUAL

*Entrada: Datos urbanos, históricos y sociales de la investigación.*

### 4.1 Integración Tipológica

- [ ] **Análisis de tipologías vecinas:** ¿la zona es de casas con patio central,
      casas compactas al frente, o fraccionamiento cerrado? ¿qué alturas
      predominan?
- [ ] **Decisión de mimetismo o contraste:** ¿el proyecto sigue el lenguaje del
      entorno o propone uno nuevo? Justificar.
- [ ] **Alineaciones y cornisas:** ¿el proyecto respeta la altura de cornisa
      de los vecinos? ¿respeta la línea de fachada?

*Salida: Estrategia de integración urbana (mimetismo, contraste o adaptación).*

### 4.2 Mapa de Relaciones Visuales

- [ ] Procesar los vectores visuales de la investigación en un diagrama:
  - **Visuales deseables:** Líneas que conectan espacios del proyecto
        con vistas positivas (árbol, cielo, jardín vecino).
  - **Visuales a bloquear:** Líneas que conectan con vistas negativas
        (muro ciego, transformador, azotea vecina).
  - **Visuales de privacidad:** Líneas desde el exterior hacia el interior
        del proyecto (qué debe ser opaco, qué puede ser transparente).
- [ ] Para cada espacio habitable, definir el **encuadre óptimo de ventana**
      (ángulo, altura, profundidad) que maximice la vista positiva y bloquee
      la negativa.

*Salida: Diagrama de visuales con vectores de calidad (verde = capturar,
rojo = bloquear, amarillo = negociar).*

### 4.3 Análisis de Acceso y Circulación Urbana

- [ ] **Acceso vehicular:** ¿el acceso a cochera es directo desde la calle o
      requiere retroceso? ¿se puede entrar y salir de frente?
- [ ] **Acceso peatonal:** ¿el recorrido de la banqueta a la puerta es claro,
      seguro y cubierto?
- [ ] **Conexión con el barrio:** ¿hay rutas peatonales hacia equipamiento
      cercano? ¿el proyecto se conecta o se aísla?
- [ ] **Ruido:** Mapa de isófonas (fuentes de ruido + decaimiento por distancia).
      Definir barreras acústicas necesarias (muros, vegetación, doble vidrio).

*Salida: Diagrama de accesos y circulaciones urbanas.*

---

## 5. ANÁLISIS DEL PROGRAMA (DIAGRAMA ESPACIAL SOMA)

*Entrada: Programa arquitectónico del Dashboard (espacios Deseado, Complementario,
Lujo).*

### 5.1 Clasificación por Zona SOMA

- [ ] Cada espacio del programa se asigna a una de las 5 zonas:
  | Zona | Espacios típicos |
  |------|------------------|
  | **Social** | Sala, comedor, terraza, jardín, recibidor |
  | **Descanso** | Recámaras, estudio, área de lectura, cuarto de TV íntimo |
  | **Operativa** | Cocina técnica, oficina, taller, gimnasio, lavandería |
  | **Soporte** | Bodega, cochera, cuarto de servicio, instalaciones |
  | **Transición** | Pasillos, vestíbulo, escaleras, portal de entrada |
- [ ] Contar m² por zona y calcular porcentaje del total.
- [ ] Evaluar el balance: una casa saludable tiene ~30% social, ~25% descanso,
      ~20% operativa, ~15% soporte, ~10% transición.
      Desviaciones significativas indican un desbalance que el diseño debe
      resolver.

*Salida: Tabla de programa clasificado con porcentajes por zona.*

### 5.2 Matriz de Relaciones Espaciales

- [ ] Para cada par de espacios, determinar el tipo de relación:
  | Relación | Símbolo | Significado |
  |----------|---------|-------------|
  | Contigüidad necesaria | ██ | Deben estar juntos (cocina-comedor) |
  | Contigüidad deseable | ▓▓ | Es mejor que estén cerca (recámara-baño) |
  | Independencia | ░░ | Da igual (estudio-cochera) |
  | Separación necesaria | ██ | Deben estar lejos (recámaras-taller ruidoso) |
- [ ] Construir la **matriz de relaciones** (cuadro de doble entrada con todos
      los espacios).
- [ ] Identificar **clusters** (grupos de espacios con alta relación entre sí).

*Salida: Matriz de relaciones + clusters programáticos.*

### 5.3 Diagrama Espacial SOMA (Grafo)

- [ ] Usar el **DiagramaSoma.html** (en esta misma carpeta) para graficar
      las relaciones como un grafo de nodos (espacios) y aristas (relaciones).
- [ ] Los nodos se colorean por zona SOMA (Social, Descanso, Operativa, Soporte,
      Transición).
- [ ] El grosor de la arista indica la intensidad de la relación.
- [ ] El grafo revela:
  - **Espacios centrales** (más conexiones): son el corazón del proyecto.
  - **Espacios aislados** (menos conexiones): pueden ubicarse en extremos.
  - **Cuellos de botella:** espacios por donde pasa toda la circulación
        y pueden congestionarse.
- [ ] Exportar el grafo como PNG para incluirlo en la guía de diseño.

*Salida: Grafo de relaciones espaciales (Diagrama SOMA).*

### 5.4 Análisis de Eficiencia del Programa

- [ ] **Relación área útil / área construida:** ¿cuánto del área total es
      realmente habitable vs circulación y muros? Objetivo: >80%.
- [ ] **Área de circulación:** ¿los pasillos son eficientes o hay metros
      perdidos? Objetivo: <12% del área total.
- [ ] **Flexibilidad:** ¿hay espacios que puedan cambiar de uso en el futuro?
      (oficina → recámara, bodega → baño).
- [ ] **Capacidad de ampliación:** ¿el programa contempla crecimiento futuro?
      ¿dónde se ubicaría?

*Salida: Indicadores de eficiencia del programa.*

---

## 6. ANÁLISIS COMPLEMENTARIOS

### 6.1 Análisis de Iluminación Natural

#### Porcentaje de vano recomendado por espacio

"No se trata de inundar de luz, sino de dosificar la alegría."

| Espacio | % vano/piso recomendado | Notas |
|---------|------------------------|-------|
| Recámaras | 12–18% | Luz suave, evitar sol directo en cama. Ventana al N o E. |
| Sala / Estar | 18–25% | Luz ambiental amplia, sin deslumbramiento directo. |
| Comedor | 15–20% | Luz media, que ilumine la mesa sin encandilar. |
| Cocina | 15–25% | Luz natural en área de trabajo. Evitar sombra del cuerpo. |
| Baños | 10–15% | Suficiente para aseo diurno sin calentar el espacio. |
| Pasillos / Circulaciones | 8–12% | Luz indirecta, sugerente. Tragaluz o ventana alta. |
| Estudio / Oficina | 20–30% | Luz pareja, idealmente N (luz fría constante) |
| Escaleras | 10–15% | Seguridad ante todo. Luz cenital o ventana en descanso. |

**Clave bioclimática para Mérida:**
- Un **15–20%** bien orientado (N o NE con protección) da mejor confort que un
  **30%** mal orientado (E u O sin protección).
- Dos ventanas pequeñas en muros opuestos (ventilación cruzada + luz bilateral)
  es mejor que una ventana grande en un solo muro.
- Un **tragaluz pequeño** (5–8%) con tubo de luz difusa alegra un pasillo o
  baño interior sin aportar calor significativo.
- La **luz reflejada** (piso claro, muros blancos, jardín exterior claro)
  multiplica la luminosidad sin aumentar la ganancia térmica.

**Regla de oro:** Un pequeño rayo de sol matutino (15–20 min) en un espacio
lo activa psicológicamente. Más de 2 horas de sol directo continuo lo vuelve
inhabitable sin A/C en clima cálido-húmedo.

#### Factor de Luz Diurna (FLD)

- [ ] Simular el **FLD** en espacios clave:
  - Sala/estar: FLD >3% (bien iluminado).
  - Recámaras: FLD 1.5–3% (luz suave).
  - Pasillos: FLD 0.5–1.5% (luz ambiental).
- [ ] **Penetración de luz:** calcular hasta dónde llega la luz natural desde
      la ventana (regla: 1.5× la altura del dintel).
- [ ] **Sombra arrojada:** ¿los aleros proyectan sombra sobre la ventana en
      verano? ¿el sol de invierno entra por debajo del alero?

*Método: Maqueta virtual con SketchUp + sombras, o tabla de cálculo de
ángulo solar.*

### 6.2 Análisis Acústico

- [ ] **Fuentes de ruido externas:** clasificar por tipo (continuo: tráfico,
      intermitente: perros, puntual: campanas) y nivel (dB aproximado).
- [ ] **Mapa de ruido interior:** ¿qué espacios necesitan silencio (recámaras,
      estudio) y cuáles pueden tener ruido (sala, cocina, taller)?
- [ ] **Barreras acústicas:**
  - Vegetación densa: reduce 5–10 dB.
  - Muro de bloque macizo: reduce 30–40 dB.
  - Doble vidrio (6+12+6 mm): reduce 30–35 dB.
  - Distancia: cada 30 m de separación reduce ~5 dB.
- [ ] **Aislamiento entre espacios:** los muros entre recámara y sala/estudio
      deben tener masa suficiente (tabique de barro, concreto) o doble muro
      con cámara de aire.

*Salida: Mapa de ruido con recomendaciones de aislamiento por espacio.*

### 6.3 Análisis Proxémico (Relaciones de Distancia)

- [ ] Revisar las distancias entre mobiliario en cada espacio contra estándares
      antropométricos:
  - Circulación mínima entre muebles: 0.90 m.
  - Frente de cocina entre encimera y gabinete: 1.20 m.
  - Distancia mesa-comedor a muro: 0.90 m (silla + paso).
  - Ancho de cama + paso en recámara: 1.90 m (matrimonial) + 0.60 m
        de paso a cada lado.
- [ ] Identificar espacios donde el usuario esté forzado a pasar cerca de otro
      (conflicto de territorialidad).

*Salida: Checklist de verificación proxémica por espacio.*

### 6.4 Análisis de Ciclo de Vida y Mantenimiento

- [ ] **Durabilidad:** ¿los materiales seleccionados resisten el clima de Mérida
      (sol, humedad, salitre en zonas costeras)?
- [ ] **Mantenimiento:** ¿el cliente puede mantener los materiales? (pisos de
      madera requieren barnizado periódico, concreto pulido es casi cero
      mantenimiento).
- [ ] **Ciclo de vida:** ¿la distribución soporta cambios familiares (llegada
      de hijos, envejecimiento, salida de hijos)?

*Salida: Notas de mantenimiento para la guía de diseño.*

---

## 7. SÍNTESIS DE ANÁLISIS

Al completar todos los análisis, se genera un **documento de síntesis** que
contiene:

1. **Partido arquitectónico:** Una frase + un diagrama que resume la estrategia
   general del proyecto (orientación, zonificación, carácter).
2. **Estrategias de diseño:** Lista priorizada de decisiones de diseño derivadas
   del análisis (máximo 10).
3. **Constraints y oportunidades:** Lo que el proyecto NO puede hacer (por norma,
   clima, presupuesto) y lo que DEBE aprovechar (vista, viento, árbol).
4. **Perfil del proyecto:** UserEntity + CreativeCore + 10 ejes + adjetivo rector.
5. **Diagrama espacial (grafo):** Relaciones entre espacios con zonificación SOMA.
6. **Zonificación térmica:** Planta dividida en zonas de confort natural, híbrido
   y asistido.

Este documento de síntesis es la **entrada directa a la fase de Conceptualización**
(Etapa 4 del ciclo SOMA).

---

*El análisis no es el fin, es el medio. No se trata de tener muchos datos,
sino de tener claridad sobre lo que esos datos exigen del diseño.*

---

## FUENTES

- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — análisis de circulación, jerarquía espacial, relación luz-forma.
- **Francis D.K. Ching**, *Building Construction Illustrated* (6th ed., 2020) — criterios de ventilación, iluminación y acústica en clima cálido.
- **C. M. Deasy**, *Design Places for People* (1974) — análisis del comportamiento humano como base del diseño, observación de patrones de uso.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — análisis de la función como generadora de forma, eficiencia programática.
- **Edward T. Hall**, *The Hidden Dimension* (1966) — teoría proxémica, distancias interpersonales, territorialidad.
- **Christopher Alexander**, *A Pattern Language* (1977) — patrones 107 (wings of light), 128 (indoor sunlight), 135 (light on two sides), 159 (light from two sides), 161 (sunny place), 180 (window place), 198 (closets between rooms). (patternlanguage.com)
- **Victor Olgyay**, *Design with Climate: Bioclimatic Approach to Architectural Regionalism* (1963) — carta solar, estrategias pasivas para clima cálido-húmedo.
- **Baruch Givoni**, *Climate Considerations in Building and Urban Design* (1998) — confort térmico, ventilación natural, estrategias para clima cálido-húmedo.
- **Christian Norberg-Schulz**, *Genius Loci: Towards a Phenomenology of Architecture* (1979) — fenomenología del lugar, espíritu del sitio, refuerza el Análisis Contextual.
- **Rudolf Arnheim**, *Visual Thinking* (1969) — percepción visual aplicada al análisis de la forma arquitectónica, composición de vistas.
- **Roger H. Clark & Michael Pause**, *Precedents in Architecture: Analytic Diagrams, Formative Ideas, and Partis* (3rd ed., 2005) — análisis diagramático de edificios canónicos, metodología visual.
- **John Zeisel**, *Inquiry by Design: Tools for Environment-Behavior Research* (1984) — investigación social como insumo del análisis de sitio y contexto.
- **Oscar Newman**, *Defensible Space: Crime Prevention Through Urban Design* (1972) — territorialidad y prevención del crimen a través del diseño, aplicable al análisis de espacio público.
- **Jan Gehl**, *Life Between Buildings: Using Public Space* (1971) — espacio público y comportamiento peatonal, análisis de accesos y circulación urbana.
- **Ken Yeang**, *The Skyscraper Bioclimatically Considered* (1996) — estrategias bioclimáticas verticales (referencia complementaria para proyectos en altura).
- **Christopher Alexander**, *Notes on the Synthesis of Form* (1964) — descomposición del problema de diseño en subproblemas independientes, base del análisis programático.
- **Charles J. Holahan**, *Psicología Ambiental: Un Enfoque General* (1982) — percepción ambiental, cognición espacial, mapas cognitivos del usuario.
- **PROTOCOLO_INVESTIGACION_PREVIA.md** (SOMA, 2026) — datos de entrada: levantamiento de sitio, normativa, clima, contexto urbano.
- **Normativas de Construcción Mérida** (SOMA, 2026) — COS, CUS, restricciones, alturas.
