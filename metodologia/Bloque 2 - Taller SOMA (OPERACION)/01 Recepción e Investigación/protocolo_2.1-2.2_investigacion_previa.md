# PROTOCOLO: INVESTIGACIÓN PREVIA DEL PROYECTO
## Bloque 2 — Taller SOMA (Operación)
## Referencia: PROCESO DE DISEÑO 2.0 — Secciones 2.1 y 2.2

**Propósito:** Recolectar los datos brutos del sitio, clima y normativa
que se procesarán en la fase de Análisis (Sección 3 del 2.0).

**Regla fundamental:**
- **Investigación** = ¿qué hay? ¿dónde obtenerlo? Se recolecta, no se interpreta.
- **Análisis** = ¿qué significa eso para el diseño? Se procesa en el protocolo de
  análisis (`02 Análisis/protocolo_3.1-3.10_analisis.md`).
- Todo output de esta sección es **bruto** — archivos, fotos, tablas sin procesar.

**Procesadores:**
- `AI` — la IA ejecuta (búsquedas, descargas, lookups)
- `HUMANO` — el arquitecto ejecuta (trabajo de campo, juicio)
- `AI→HUMANO` — IA procesa datos, humano toma decisiones

---

## 2.1 Material Constante
*Fuentes que se recolectan una vez y persisten para todos los proyectos.
Si la fuente ya está en la biblioteca SOMA → copiar al proyecto.
Si es la primera vez o hay actualización → descargar de la fuente externa,
guardar en biblioteca SOMA y copiar al proyecto.*

### 2.1.1 Datos Bioclimáticos

```
[REF] 2.1.1.1 Normales Climatológicas de Mérida (P2.0 ref: 2.1.1.1)
─────────────────────────────────
INPUT:  CONAGUA / SMN (fuente externa)
OPERA:  Buscar en biblioteca SOMA (clima/INDICE_CLIMA.md). Si no existe o
        hay actualización, descargar de CONAGUA/SMN. Guardar en biblioteca
        SOMA y copiar a `referencias/clima/` del proyecto
OUTPUT: `normales_climatologicas_merida.pdf` — archivo en bruto
PROC:   AI
```

| Variable | Dato | Fuente |
|----------|------|--------|
| Clasificación Köppen | Cálido subhúmedo Aw (sabana) | García, 1973 |
| Altitud | 8 msnm | CONAGUA-SMN |
| Latitud | 20.97° N | CONAGUA-SMN |
| Temperatura media anual | 26°C | CONAGUA-SMN |
| Temperatura máxima extrema | ~40°C (abril-mayo) | CONAGUA-SMN |
| Temperatura mínima (nortes) | ~10°C (dic-ene) | CONAGUA-SMN |
| Humedad relativa media | 75–80% | Canto, 1997 |
| Precipitación | Régimen de verano (mayo-octubre) | CONAGUA-SMN |

```
[REF] 2.1.1.2 Carta Solar de Mérida (P2.0 ref: 2.1.1.2)
─────────────────────────────────
INPUT:  Latitud/longitud de Mérida (20.97°N, 89.62°O)
OPERA:  Buscar en biblioteca SOMA (clima/carta_solar_merida.png). Si no
        existe, generar con software (Ladybug, SunPath) o descargar de
        fuente confiable. Guardar en biblioteca SOMA y copiar a
        `referencias/clima/` del proyecto
OUTPUT: `carta_solar_merida.png` o `.pdf` — archivo en bruto
PROC:   AI
```

| Variable | Dato | Fuente |
|----------|------|--------|
| Radiación global promedio | 4.7 kWh/m² | CONAGUA-SMN / INEGI |
| Horas de sol promedio | ~6–7 h/día | CONAGUA-SMN |
| Trayectoria | Este → Oeste, siempre al Sur del cenit | — |

```
[REF] 2.1.1.3 Rosa de los Vientos de Mérida (P2.0 ref: 2.1.1.3)
─────────────────────────────────
INPUT:  CONAGUA / SMN (datos históricos de dirección y velocidad del viento)
OPERA:  Buscar en biblioteca SOMA (clima/rosa_vientos_merida.png). Si no
        existe, generar desde datos históricos. Guardar en biblioteca SOMA
        y copiar a `referencias/clima/` del proyecto
OUTPUT: `rosa_vientos_merida.png` o `.pdf` — archivo en bruto
PROC:   AI
```

| Variable | Dato | Fuente |
|----------|------|--------|
| Dirección predominante | E, NE, SE (Alisios) | U. Modelo |
| Vientos más frescos | NE | U. Modelo |
| Nortes (frentes fríos) | Otoño-invierno, N-NE | CONAGUA-SMN |
| Suradas (cálido) | Primavera, S-SE | CONAGUA-SMN |
| Riesgo de huracanes | Junio-noviembre, hasta 250 km/h | CONAGUA-SMN |

### 2.1.2 Normativas y Guías de Diseño

```
[REF] 2.1.2.1 Reglamento de Construcción de Mérida (P2.0 ref: 2.1.2.1)
─────────────────────────────────
INPUT:  Ayuntamiento de Mérida / IM Plan (fuente externa)
OPERA:  Buscar en biblioteca SOMA (normativas/reglamento_construccion_merida.pdf).
        Si no existe o hay actualización, descargar PDF de la fuente oficial.
        Guardar en biblioteca SOMA y copiar a `referencias/normativas/` del proyecto
OUTPUT: `reglamento_construccion_merida.pdf` — archivo en bruto
PROC:   AI
```

Parámetros a consultar específicos del predio:
- [ ] COS (Coeficiente de Ocupación del Suelo) — % máximo de desplante según zona
- [ ] CUS (Coeficiente de Utilización del Suelo) — m² máximos construibles
- [ ] Altura máxima — no exceder el doble del ancho de la vialidad (Art. 65)
- [ ] Restricciones frontales, laterales y posteriores (metros de retiro)
- [ ] Área verde permeable mínima
- [ ] Pozos de absorción — 1 por cada 350 m² impermeables

```
[REF] 2.1.2.2 Norma de Accesibilidad Universal (P2.0 ref: 2.1.2.2)
─────────────────────────────────
INPUT:  Secretaría de Desarrollo Urbano / NOM (fuente externa)
OPERA:  Buscar en biblioteca SOMA (normativas/NMX-R-050-SCFI-2006_accesibilidad.pdf).
        Si no existe, descargar PDF de fuente oficial. Guardar en biblioteca SOMA
        y copiar a `referencias/normativas/` del proyecto
OUTPUT: `norma_accesibilidad_universal.pdf` — archivo en bruto
PROC:   AI
```

| Parámetro | Valor referencia (Mérida) |
|-----------|---------------------------|
| Ancho mínimo puerta principal | 0.90 m |
| Ancho mínimo puertas interiores | 0.80 m (recámaras), 0.70 m (baños) |
| Pendiente máxima de rampa | 10% (≤3 m), 8% (≤6 m), 6% (≤9 m) |
| Diámetro de giro baño accesible | 1.50 m |
| Ancho de pasillos interiores | 0.90 m mínimo |
| Escaleras: huella mínima / peralte máx. | 0.25 m / 0.18 m |
| Barandales en escaleras y rampas | Altura 0.90–1.10 m, ambos lados |

```
[REF] 2.1.2.3 Reglamento de Uso de Suelo (P2.0 ref: 2.1.2.3)
─────────────────────────────────
INPUT:  Plan de Desarrollo Urbano de Mérida / carta urbana
OPERA:  Buscar en biblioteca SOMA (normativas/PMDU_Merida.pdf). Si no existe
        o hay actualización, descargar PDF de IM Plan. Guardar en biblioteca SOMA
        y copiar a `referencias/normativas/` del proyecto
OUTPUT: `uso_de_suelo_merida.pdf` — archivo en bruto
PROC:   AI
```

```
[REF] 2.1.2.4 Parámetros de Diseño: Neufert, Ergonomía y Antropometría
      (P2.0 ref: 2.1.2.4)
─────────────────────────────────
INPUT:  Fuentes bibliográficas externas (Neufert, Panero, Ching)
OPERA:  Buscar en biblioteca SOMA (diseno/REFERENCIAS_BIBLIOGRAFICAS.md).
        Los libros tienen copyright — solo se referencian con ISBN y lugar de
        consulta. No se descargan
OUTPUT: Referencia bibliográfica consultada en biblioteca física o digital
PROC:   AI (referenciar) + HUMANO (consultar)
```

```
[REF] 2.1.2.5 Normativas de Eficiencia Energética (P2.0 ref: 2.1.2.5)
─────────────────────────────────
INPUT:  CONUEE / NOM-020-ENER (fuente externa)
OPERA:  Buscar en biblioteca SOMA (normativas/NOM-020-ENER-2011_eficiencia_energetica.pdf).
        Si no existe o hay actualización, descargar PDF de CONUEE.
        Guardar en biblioteca SOMA y copiar a `referencias/normativas/`
OUTPUT: `nom_020_ener_eficiencia_energetica.pdf` — archivo en bruto
PROC:   AI
```

### 2.1.3 Estado del Arte en Vivienda y Repertorio Tipológico

```
[REF] 2.1.3.1 Arquetipos Históricos de la Vivienda en Yucatán (P2.0 ref: 2.1.3.1)
─────────────────────────────────
INPUT:  Fuentes externas (historia, arquitectura, urbanismo)
OPERA:  Buscar en biblioteca SOMA (arquetipos/INDICE_ARQUETIPOS.md). Si es
        la primera vez o hay nuevas fuentes, investigar y recolectar materiales
        sobre arquetipos (casa maya, colonial, porfiriana, moderna).
        Guardar en biblioteca SOMA y copiar a `referencias/arquetipos/`
OUTPUT: `arquetipo_casa_maya.pdf`, `arquetipo_casa_colonial.pdf`, etc.
        — archivos de referencia en bruto
PROC:   AI (búsqueda y recolección)
```

```
[REF] 2.1.3.2 Repertorio Local, Nacional e Internacional (P2.0 ref: 2.1.3.2)
─────────────────────────────────
INPUT:  Fuentes externas (libros, revistas, portafolios digitales)
OPERA:  Buscar en biblioteca SOMA (repertorio/REPERTORIO_PROYECTOS.md).
        Si no existen proyectos de referencia que compartan tipo, escala o clima
        con el actual, investigar y recolectar. Guardar en biblioteca SOMA y
        copiar a `referencias/repertorio/` del proyecto
OUTPUT: `proyecto_referencia_01.pdf`, `proyecto_referencia_02.jpg`, etc.
        — archivos de referencia en bruto
PROC:   AI (búsqueda y recolección)
```

```
[REF] 2.1.3.3 Patrones Importantes de Diseño SOMA (P2.0 ref: 2.1.3.3)
─────────────────────────────────
INPUT:  Fuentes externas + experiencia del arquitecto
OPERA:  Buscar en biblioteca SOMA (patrones/CATALOGO_PATRONES_DISENO.md).
        Si es primera vez, construir el catálogo de patrones SOMA
        (acontecimiento, espaciales, de uso, tectónicos, bioclimáticos).
        Se copia a `referencias/patrones/` de cada proyecto
OUTPUT: `catalogo_patrones_diseno.md` — documento vivo, se enriquece con el tiempo
PROC:   AI→HUMANO (AI compila borrador inicial, humano cura)
```

```
[REF] 2.1.3.4 Patrones de Christopher Alexander (P2.0 ref: 2.1.3.4)
─────────────────────────────────
INPUT:  "A Pattern Language" (Alexander et al., 1977) — fuente externa
OPERA:  Buscar en biblioteca SOMA (patrones/REFERENCIA_ALEXANDER.md).
        El libro tiene copyright — solo se referencia con ISBN y se consulta
        el mapeo de 34 patrones aplicables a Mérida
OUTPUT: `a_pattern_language_alexander.pdf` — archivo de referencia si se adquiere
PROC:   AI (referenciar) + HUMANO (consultar)
```

---

## 2.2 Material Variable
*Datos que se recolectan específicamente para cada proyecto.
Operación: ir al campo, medir, fotografiar, entrevistar, registrar.*

### 2.2.2 Datos del Sitio

```
[OUT] 2.2.2.1 Levantamiento Físico del Terreno (P2.0 ref: 2.2.2.1)
─────────────────────────────────
INPUT:  Visita al sitio + escrituras / plano catastral del predio
OPERA:  Medir y registrar en campo: dimensiones y forma del terreno,
        niveles y pendientes, tipo de suelo (observación superficial),
        vegetación existente, construcciones preexistentes.
        Todo se registra en croquis análogo y fotografías
OUTPUT: • `croquis_levantamiento.pdf` — croquis acotado del predio
        • `fotos_terreno/` — carpeta con fotografías en bruto
        • `datos_predio.txt` — dimensiones, área, medidas de escrituras
PROC:   HUMANO
```

Checklist de campo:
- [ ] **Topografía:** Pendientes del terreno, niveles de banqueta, punto más alto/bajo. Croquis de niveles con cotas.
- [ ] **Orientación:** Norte magnético y norte geográfico. Registrar trayectoria solar aproximada sobre el predio.
- [ ] **Dimensiones y forma:** Superficie total, frente, fondo, colindancias, forma del predio.
- [ ] **Vegetación existente:** Árboles a conservar (especies, diámetro de copa, altura), vegetación menor, áreas verdes. Fotografiar cada árbol relevante.
- [ ] **Edificaciones preexistentes:** Construcciones actuales, materiales, estado.
- [ ] **Mecánica de suelos:** Tipo de suelo (roca calcárea en Yucatán), capacidad de carga si se tiene dato. Al menos reconocimiento visual del entorno y tipo de cimentación de construcciones colindantes.

```
[OUT] 2.2.2.2 Levantamiento de Elementos Interiores del Predio (P2.0 ref: 2.2.2.2)
─────────────────────────────────
INPUT:  Visita al sitio
OPERA:  Registrar y fotografiar: árboles (especie, ubicación, diámetro),
        pozos, cenotes, cuerpos de agua, construcciones existentes (muros,
        pisos, losas, vanos, estado, materiales), acometidas (agua, drenaje,
        electricidad, gas). Registro en croquis + fotografías
OUTPUT: • `fotos_elementos_interiores/` — carpeta con fotos en bruto
        • `croquis_elementos_existentes.pdf`
PROC:   HUMANO
```

```
[OUT] 2.2.2.3 Levantamiento de Elementos Exteriores (P2.0 ref: 2.2.2.3)
─────────────────────────────────
INPUT:  Visita al sitio + recorrido del entorno inmediato
OPERA:  Registrar y fotografiar: colindancias (alturas, materiales, usos,
        estado), vialidades (ancho, tipo, flujo), banquetas (ancho, estado),
        postes (luz, teléfono, CCTV), alcantarillado, árboles públicos,
        visuales del entorno en 4 direcciones
OUTPUT: • `fotos_entorno/` — carpeta con fotos en bruto
        • `croquis_contexto_urbano.pdf`
PROC:   HUMANO
```

Checklist de contexto:
- [ ] **Tejido edificado:** Alturas, materiales, estilos y edades de construcciones vecinas.
- [ ] **Usos de suelo del entorno:** Residencial, mixto, comercial, equipamiento.
- [ ] **Transporte público:** Rutas cercanas, paradas, frecuencia.
- [ ] **Equipamiento cercano:** Escuelas, hospitales, mercados, parques. Distancias.
- [ ] **Visuales del entorno:** Fotografiar en 4 direcciones + desde posibles puntos de ventana. Elementos positivos (árboles, jardines, cielo abierto) y negativos (muros ciegos, transformadores, azoteas vecinas).
- [ ] **Seguridad:** Percepción de la zona, iluminación pública nocturna, flujo peatonal.

### 2.2.2.4 Infraestructura y Servicios

| Dato | Cómo obtenerlo |
|------|---------------|
| Acometida eléctrica | Inspección en sitio, pregunta al vecino o CFE |
| Agua potable | Junta de Agua Potable o vecinos |
| Drenaje sanitario | Observación de pozos/tomas en la calle |
| Fibra óptica / internet | Telmex, Totalplay, etc. |

- [ ] **Acometida eléctrica:** Ubicación del medidor, tipo de conexión (aérea/subterránea).
- [ ] **Agua potable:** Diámetro de toma, presión estimada, ubicación del medidor.
- [ ] **Drenaje sanitario:** Conexión a alcantarillado municipal o biodigestor/fosa séptica.
- [ ] **Agua pluvial:** Puntos de descarga. Pozos de absorción (1 c/350 m² según reglamento).
- [ ] **Gas:** Gas natural en la zona o tanque estacionario.
- [ ] **Telecomunicaciones:** Fibra óptica disponible, cobertura.
- [ ] **Vialidad:** Tipo de calle, ancho de arroyo y banquetas, estado de pavimento.

### 2.2.3 Normativas Específicas

```
[REF] 2.2.3 Normativas Específicas del Fraccionamiento (P2.0 ref: 2.2.3)
─────────────────────────────────
INPUT:  Administración del fraccionamiento o condominio (si aplica)
OPERA:  Si el predio está en fraccionamiento o condominio, solicitar el
        reglamento interno a la administración. Guardar en biblioteca SOMA
        y copiar a `referencias/normativas/especificas/` del proyecto
OUTPUT: `reglamento_fraccionamiento.pdf` — archivo en bruto (si aplica)
PROC:   AI
```

### 2.2.4 Datos Ambientales Específicos

```
[OUT] 2.2.4.1 Fuentes de Ruido (P2.0 ref: 2.2.4.1)
─────────────────────────────────
INPUT:  Visita al sitio en diferentes horarios (mañana, tarde, noche,
        entre semana, fin de semana)
OPERA:  Identificar fuentes de ruido: vialidades cercanas (flujo, tipo),
        industrias, talleres, escuelas, comercios, aires acondicionados, etc.
        Registrar ubicación en croquis y tipo. Medición cualitativa
        (bajo/medio/alto) o cuantitativa con decibelímetro
OUTPUT: • `mapa_fuentes_ruido.pdf` — croquis con ubicaciones
        • `notas_ruido.txt` — horarios críticos, descripciones
PROC:   HUMANO
```

```
[OUT] 2.2.4.2 Fuentes de Olores (P2.0 ref: 2.2.4.2)
─────────────────────────────────
INPUT:  Visita al sitio + pregunta a vecinos (opcional)
OPERA:  Identificar fuentes de olores: basurero, granja, industria, pozo
        séptico, quemas, etc. Registrar dirección del viento, horarios y
        estacionalidad
OUTPUT: • `mapa_fuentes_olores.pdf` — croquis con dirección de viento
        • `notas_olores.txt` — horarios, descripciones
PROC:   HUMANO
```

---

## Investigación Histórica

- [ ] **Evolución del predio:** Consultar en catastro municipal o vecinos si el terreno formó parte de hacienda o fraccionamiento.
- [ ] **Construcciones previas:** Preguntar si hubo edificaciones anteriores (restos de cimentaciones, pozos, rellenos).
- [ ] **Valor patrimonial:** Verificar si el predio está en zona de monumentos históricos (Centro Histórico de Mérida requiere autorización INAH).
- [ ] **Historia del barrio:** Fecha de fundación, estilo arquitectónico predominante, hitos culturales.
- [ ] **Preexistencias físicas:** Registrar árboles maduros, muros de piedra, pozos antiguos, albarradas, cenotes (común en Yucatán).

---

## Viabilidad Económica

- [ ] **Presupuesto del cliente:** Total disponible, si incluye terreno, etapas, prioridad m² vs acabados.
- [ ] **Honorarios de diseño:** $250/m² Esencial, $350/m² Integral, $850/m² Ejecutivo.

| Riesgo | Qué investigar |
|--------|---------------|
| Inundación | Historial de la colonia, topografía, drenaje municipal |
| Huracanes | Zona de vientos según reglamento |
| Suelo | Cavernas/cenotes — preguntar a vecinos |
| Contaminación | Uso previo del terreno |
| Servidumbres | Paso de instalaciones, derechos de vía |

---

## Formato de Salida

Al completar la investigación se genera la **Carpeta de Investigación del Proyecto**
en `backend/proyectos/SOMA-XXXX/`:

```
referencias/
├── clima/
│   ├── normales_climatologicas_merida.pdf
│   ├── carta_solar_merida.png
│   └── rosa_vientos_merida.png
├── normativas/
│   ├── reglamento_construccion_merida.pdf
│   ├── norma_accesibilidad_universal.pdf
│   └── nom_020_ener_eficiencia_energetica.pdf
├── arquetipos/
├── repertorio/
└── patrones/
levantamiento/
├── croquis_levantamiento.pdf
├── croquis_elementos_existentes.pdf
├── croquis_contexto_urbano.pdf
├── fotos_terreno/
├── fotos_elementos_interiores/
├── fotos_entorno/
└── datos_predio.txt
ambiente/
├── mapa_fuentes_ruido.pdf
├── nota_ruido.txt
├── mapa_fuentes_olores.pdf
└── notas_olores.txt
```

Esta carpeta es la entrada para el **PROTOCOLO DE ANÁLISIS** (`02 Análisis/protocolo_3.1-3.10_analisis.md`).

---

## FUENTES

- García, E. (1973). *Modificaciones al sistema Köppen.*
- Canto, E. (1997). *Arquitectura bioclimática en Yucatán.*
- CONAGUA — SMN. *Normales Climatológicas de Mérida.*
- H. Ayuntamiento de Mérida. (2023). *Reglamento de Construcción del Municipio de Mérida y NTC.*
- IM Plan. (2022). *Plan de Desarrollo Urbano del Municipio de Mérida.*
- NMX-R-050-SCFI-2015. *Accesibilidad Universal.*
- NMX-R-001-SCFI. *Norma Mexicana de Vivienda.*
- CONUEE. (2011). *NOM-020-ENER-2011.*
- Alexander, C. et al. (1977). *A Pattern Language.* Oxford University Press.
- Neufert, E. (1936). *El Arte de Proyectar en Arquitectura.* Gustavo Gili.
- Panero, J. & Zelnik, M. (1979). *Human Dimension & Interior Space.*
- Ching, F. (2014). *Arquitectura: Forma, Espacio y Orden.* Gustavo Gili.
- Hall, E. T. (1966). *The Hidden Dimension.* Doubleday.
