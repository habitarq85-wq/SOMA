# PROTOCOLO DE ANÁLISIS
## Bloque 2 — Taller SOMA (Operación)
## Referencia: PROCESO DE DISEÑO 2.0 — Sección 3 (Items 3.1 a 3.10)

**Diferencia clave:**
| Fase | Qué se hace | Pregunta |
|------|------------|----------|
| **Investigación** | Recolectar datos brutos | ¿Qué hay? |
| **Análisis** | Procesar datos en información de diseño | ¿Qué significa? |

**Regla:** No se puede analizar lo que no se investigó. Todo análisis parte
de un dato de la fase de investigación.

---

## 3.1 Gráfico General del Sitio

```
[OUT] 3.1 Gráfico General del Sitio (P2.0 ref: 3.1)
─────────────────────────────────
INPUT:  2.2.2.1 `croquis_levantamiento.pdf` + `datos_predio.txt`
        2.2.2.2 `croquis_elementos_existentes.pdf`
        2.2.2.3 `croquis_contexto_urbano.pdf`
        2.2.4.1 `mapa_fuentes_ruido.pdf`
        2.2.4.2 `mapa_fuentes_olores.pdf`
        2.1.1.1 `normales_climatologicas_merida.pdf`
        2.1.1.2 `carta_solar_merida.pdf`
        2.1.1.3 `rosa_vientos_merida.pdf`
OPERA:  Integrar croquis y datos brutos en un solo gráfico de síntesis
        que superponga capas: geometría, niveles, vegetación, colindancias,
        vialidades, banquetas, acometidas, fuentes de ruido/olor, recorrido
        solar y dirección de viento
OUTPUT: Lámina única de síntesis del sitio — capa base para todo análisis
PROC:   HUMANO
```

### 1.1 Volumetría Regulatoria (Bounding Box)
- [ ] A partir de COS: calcular área máxima de desplante
- [ ] A partir de CUS: calcular área máxima construible total
- [ ] A partir de restricciones: trazar envolvente máxima edificable
- [ ] A partir de altura máxima: definir cuántos niveles caben
- [ ] Trazar el **polígono de construcción permitido**
- [ ] Identificar zonas "muertas" aprovechables (jardines, patios, estacionamiento)

### 1.2 Mapa de Conflictos Sitio-Diseño
- [ ] Cruce topografía + COS: ¿la pendiente afecta el desplante?
- [ ] Cruce vegetación + Bounding Box: ¿árboles dentro del polígono construible?
- [ ] Cruce infraestructura + diseño: ¿acometidas donde se necesitan?
- [ ] Cruce acústica + zonificación: ¿ruido afecta ubicación de recámaras?
- [ ] Cruce visuales + orientación: ¿mejor vista = peor orientación?

### 1.3 Diagrama de Aprovechamiento del Predio
- [ ] Dibujar soleamiento por hora sobre el polígono construible
- [ ] Dibujar franjas de viento dominante
- [ ] Identificar **área premium** (N, viento NE, buena vista, buen acceso)
- [ ] Identificar **área de servicio** (zonas calientes E/O, ruidosas, sin vista)
- [ ] Proponer macro-zonificación (construcción, jardín, acceso, servicio)

---

## 3.2 Gráfico Particular Ambiental

```
[OUT] 3.2 Gráfico Particular Ambiental (P2.0 ref: 3.2)
─────────────────────────────────
INPUT:  3.1 Gráfico General del Sitio
        2.2.4.1-2 Fuentes de ruido y olores
        2.2.2.3 Contexto urbano
OPERA:  Generar gráfico específico: visuales (exterior→interior y viceversa),
        gradiente de ruido, gradiente de temperatura (islas de calor),
        gradiente de ventilación (canales de viento), conflictos de
        infraestructura, visuales perjudiciales
OUTPUT: Lámina de análisis ambiental particular
PROC:   HUMANO
```

---

## 3.3 Programa Arquitectónico

```
[OUT] 3.3 Programa Arquitectónico (P2.0 ref: 3.3)
─────────────────────────────────
INPUT:  2.2.1.1 `respuestas_inmersion_web.json`
        2.2.1.2 `notas_campo_entrevista.txt`
        2.1.2.4 Tablas Neufert (dimensiones mínimas)
        Catálogo SOMA de espacios mínimos v3.0
OPERA:  Desglosar necesidades del usuario en espacios. Clasificar:
        Deseado / Complementario / Lujo. Cada espacio con nombre, m²,
        zona SOMA y observaciones
OUTPUT: Tabla de programa arquitectónico en BD + totales por zona
PROC:   AI→HUMANO (AI sugiere espacios mínimos, humano ajusta)
```

### 5.1 Clasificación por Zona SOMA
| Zona | Espacios típicos |
|------|------------------|
| **Social** | Sala, comedor, terraza, jardín, recibidor |
| **Descanso** | Recámaras, estudio, área de lectura, cuarto TV íntimo |
| **Operativa** | Cocina, oficina, taller, gimnasio, lavandería |
| **Soporte** | Bodega, cochera, cuarto servicio, instalaciones |
| **Transición** | Pasillos, vestíbulo, escaleras, portal |

- [ ] Contar m² por zona y calcular % del total
- [ ] Evaluar balance: ~30% social, ~25% descanso, ~20% operativa, ~15% soporte, ~10% transición

---

## 3.4 Diagrama de Relaciones Espaciales

```
[OUT] 3.4 Diagrama de Relaciones Espaciales (P2.0 ref: 3.4)
─────────────────────────────────
INPUT:  3.3 Programa Arquitectónico
        Zonificación Maestra SOMA (Social, Descanso, Operativa, Soporte, Transición)
OPERA:  Para cada par de espacios determinar: conexión directa, visual,
        acústica, proximidad deseada o separación requerida
OUTPUT: • Diagrama de burbujas con relaciones
        • Matriz de relaciones (doble entrada)
        • Input para Diagrama Espacial SOMA
PROC:   HUMANO→AI
```

Matriz de tipos de relación:
| Relación | Símbolo | Ejemplo |
|----------|---------|---------|
| Contigüidad necesaria | ██ | Cocina-comedor |
| Contigüidad deseable | ▓▓ | Recámara-baño |
| Independencia | ░░ | Estudio-cochera |
| Separación necesaria | ██ | Recámaras-taller |

### Diagrama Espacial SOMA (Grafo)
- [ ] Usar `DiagramaSoma.html` para graficar relaciones como grafo
- [ ] Nodos por zona SOMA, aristas por intensidad de relación
- [ ] Identificar: espacios centrales, aislados, cuellos de botella
- [ ] Exportar PNG para guía de diseño

---

## 3.5 Selección de Patrones de Diseño SOMA

```
[DEC] 3.5 Selección de Patrones SOMA (P2.0 ref: 3.5)
─────────────────────────────────
INPUT:  2.1.3.3 `catalogo_patrones_diseno.md` (42 patrones)
        2.2.1.1 Perfil de diseño del usuario
        2.2.1.2 Notas de entrevista
        3.1 Gráfico del sitio
        3.3 Programa Arquitectónico
OPERA:  AI revisa el catálogo y selecciona patrones según clima,
        cultura, tipología, perfil del usuario, programa y sitio.
        Humano evalúa pertinencia y ajusta
OUTPUT: Checklist de patrones aplicables al proyecto
PROC:   AI→HUMANO
```

---

## 3.6 Selección de Patrones de Alexander

```
[DEC] 3.6 Selección Patrones Christopher Alexander (P2.0 ref: 3.6)
─────────────────────────────────
INPUT:  2.1.3.4 `REFERENCIA_ALEXANDER.md` (34 patrones mapeados)
        2.2.1 Perfil del usuario
        3.1 Gráfico del sitio
        3.3 Programa Arquitectónico
OPERA:  AI preselecciona patrones aplicables (escala del espacio, clima,
        cultura, tipo de relaciones). Humano evalúa y ajusta
OUTPUT: Checklist de patrones de Alexander aplicables
PROC:   AI→HUMANO
```

---

## 3.7 Restricciones Normativas

```
[DEC] 3.7 Selección de Normativas Aplicables (P2.0 ref: 3.7)
─────────────────────────────────
INPUT:  2.1.2.1 `reglamento_construccion_merida.pdf`
        2.1.2.3 `uso_de_suelo_merida.pdf`
        2.2.3 `reglamento_fraccionamiento.pdf` (si aplica)
        2.2.2.1 `datos_predio.txt`
OPERA:  Extraer valores numéricos aplicables al predio concreto:
        COS, CUS, área verde, altura máxima, retiros, cajones
OUTPUT: Ficha de restricciones numéricas + envolvente normativa
PROC:   AI
```

---

## 3.8 Premisas Ergométricas y Antropométricas

```
[GUI] 3.8 Premisas Ergométricas (P2.0 ref: 3.8)
─────────────────────────────────
INPUT:  2.1.2.4 Tablas Neufert, Panero, Ching
        3.3 Programa Arquitectónico
OPERA:  Extraer dimensiones mínimas y recomendadas por espacio:
        pasillos, alturas, áreas de mobiliario, espacios de giro
OUTPUT: Tabla de premisas ergométricas por espacio del proyecto
PROC:   AI (lookup de estándares contra programa)
```

---

## 3.9 Estrategias de Diseño Arquitectónico

```
[GUI] 3.9 Estrategias de Diseño (P2.0 ref: 3.9)
─────────────────────────────────
INPUT:  3.1, 3.2 Gráficos de sitio y ambiente
        3.5, 3.6 Patrones seleccionados
        3.7 Restricciones normativas
        3.8 Premisas ergométricas
OPERA:  Sintetizar análisis en estrategias concretas organizadas
        por tipo de afectación
OUTPUT: Conjunto de estrategias de diseño del proyecto
PROC:   AI→HUMANO
```

### 3.9.1 Estrategias de Extracción de Malos Olores
- [ ] **Recorrido del aire:** limpio → sucio (recámaras → sala → cocina → servicio)
- [ ] **Presurización:** espacios nobles en barlovento, servicios en sotavento
- [ ] **Baños:** ventilación natural directa o pozo vertical con efecto chimenea
- [ ] **Cocina:** campana extractora con salida exterior, ducto independiente
- [ ] **Áreas de servicio:** tendedero con ventilación cruzada obligatoria

### 3.9.2 Estrategias de Mitigación de Ruido
- [ ] Clasificar fuentes (continuo/intermitente/puntual)
- [ ] Ubicar espacios silenciosos vs ruidosos
- [ ] Barreras acústicas según nivel: vegetación (5-10 dB), muro macizo (30-40 dB), doble vidrio (30-35 dB)
- [ ] Masa suficiente en muros entre recámaras y espacios ruidosos

### 3.9.3 Estrategias Bioclimáticas para Mérida

#### Orientación
- **Norte:** Recámaras, estudio, sala (máximo confort, mínima ganancia)
- **Sur:** Aleros profundos. Comedor, circulaciones
- **Este:** Baños, cocina, desayunador
- **Oeste:** Servicio, bodega, muros ciegos o protección pesada

#### Ventilación
- [ ] Trazar ejes de ventilación cruzada (barlovento NE → sotavento SO)
- [ ] Área de salida ≥ área de entrada
- [ ] Barlovento: ventanas mayores con louvers fijos
- [ ] Sotavento: ventanas menores operables
- [ ] Ventilación nocturna segura + mallas mosquito

#### Estrategias Pasivas
| Estrategia | Beneficio | Costo | Cuándo aplica |
|------------|-----------|-------|---------------|
| Cool roof | -3.14°C [UADY] | Bajo | Techos con sol directo |
| Techo ventilado | -2°C adicional | Medio | Losas de concreto |
| Doble altura | -1.22°C [UADY] | Medio | Salas, comedores |
| Aleros >1.00 m | Reduce ganancia solar | Bajo | Fachada S y E |
| Ventilación cruzada NE-SO | Enfriamiento continuo | Bajo | Toda vivienda |
| Patio interior | Pulmón térmico | Medio | Predios medianos |
| Vegetación regional E-O | Microclima | Bajo | Espacio exterior |

**Recomendación:** Combinar mínimo 3-4 estrategias de bajo costo: cool roof + ventilación cruzada + aleros profundos.

#### Zonificación Térmica
- **Zona A (confort natural):** Recámaras N, sala N — sin A/C
- **Zona B (confort híbrido):** Comedor, cocina — ventilación + respaldo minisplit
- **Zona C (confort asistido):** Baños, lavado — extractor mecánico

#### Ciclo Diario de Aperturas
| Horario | Acción |
|---------|--------|
| 6:00–9:00 | Abrir ventanas NE. Ventilación cruzada total |
| 9:00–12:00 | Cerrar E. Mantener N. Cerrar persianas E |
| 12:00–17:00 | Cerrar todo. Solo micro-aperturas al N |
| 17:00–19:00 | Cerrar O. Abrir NE y S |
| 19:00–6:00 | Ventilación cruzada máxima (con mallas) |

### 3.9.4 Estrategias de Integración Urbana
- [ ] Análisis de tipologías vecinas: patio central, compacta, fraccionamiento
- [ ] Decisión de mimetismo o contraste (justificar)
- [ ] Mapa de relaciones visuales: deseables, a bloquear, de privacidad
- [ ] Análisis de accesos: vehicular, peatonal, conexión con el barrio

---

## 3.10 Análisis del Usuario

```
[OUT] 3.10 Análisis del Usuario (P2.0 ref: 3.10)
─────────────────────────────────
INPUT:  2.2.1.1 `respuestas_inmersion_web.json`
        2.2.1.2 `entrevista.wav` + `notas_campo_entrevista.txt`
OPERA:  Procesar datos brutos del usuario: transcripción, perfiles,
        Activity Matrix, CreativeCore, perfil de diseño
OUTPUT: Perfil completo del usuario (5 sub-items 3.10.1 a 3.10.5)
PROC:   AI→HUMANO
```

*El detalle de 3.10.1 a 3.10.5 está en el protocolo `2.2.1-3.10_recepcion_usuario.md`.*

### Perfil de UserEntity por habitante
| Dato investigación | Análisis |
|-------------------|----------|
| Edad y salud | Accesibilidad, alturas, riesgo caídas |
| Ocupación | Espacios requeridos |
| Hobbies | Mobiliario especial, área dedicada |
| Horarios | Activity Matrix, conflictos de uso |
| Rol de poder | Prioridades de diseño |

### Perfil de Diseño (10 Ejes de Inmersión)
- [ ] Polaridad dominante: ¿tiende más a A o B?
- [ ] Ejes definitorios: los de respuesta más extrema (0-2 o 8-10)
- [ ] Ejes neutros: se resuelven por contexto
- [ ] Coherencia interna: ¿contradicciones?

### CreativeCore (5 Ejes de Tensión)
- [ ] Tensión / Calma
- [ ] Brutalismo / Refinamiento
- [ ] Privacidad / Transparencia
- [ ] Ortogonalidad / Organicismo
- [ ] Permanencia / Efimeridad
- [ ] **Mensaje poético** — frase que capture la intención del proyecto
- [ ] **Adjetivo rector** — una palabra que defina la experiencia espacial

---

## Análisis Complementarios

### Iluminación Natural
| Espacio | % vano/piso recomendado | Notas |
|---------|------------------------|-------|
| Recámaras | 12-18% | Luz suave, ventana al N o E |
| Sala | 18-25% | Luz ambiental amplia |
| Comedor | 15-20% | Luz media sobre mesa |
| Cocina | 15-25% | Evitar sombra del cuerpo |
| Baños | 10-15% | Sin calentar el espacio |
| Estudio | 20-30% | Luz pareja, idealmente N |

**Regla de oro:** 15-20% bien orientado (N/NE) > 30% mal orientado (E/O sin protección).

### Análisis de Eficiencia del Programa
- [ ] Relación área útil / construida: objetivo >80%
- [ ] Área de circulación: objetivo <12%
- [ ] Flexibilidad: ¿espacios convertibles?
- [ ] Capacidad de ampliación futura

---

## Síntesis de Análisis

Al completar todos los análisis se genera el **documento de síntesis** que
contiene:
1. **Partido arquitectónico** — frase + diagrama resumen
2. **Estrategias de diseño** — máximo 10 priorizadas
3. **Constraints y oportunidades** — lo que NO puede hacer y lo que DEBE aprovechar
4. **Perfil del proyecto** — UserEntity + CreativeCore + 10 ejes + adjetivo rector
5. **Diagrama espacial** — grafo con zonificación SOMA
6. **Zonificación térmica** — confort natural / híbrido / asistido

Este documento es la **entrada directa a la fase de Conceptualización** (Sección 4).

---

## FUENTES

- Ching, F. (2014). *Arquitectura: Forma, Espacio y Orden.* Gustavo Gili.
- Deasy, C. M. (1990). *Designing Places for People.*
- Hall, E. T. (1966). *The Hidden Dimension.* Doubleday.
- Alexander, C. et al. (1977). *A Pattern Language.* Oxford University Press.
- Alexander, C. (1964). *Notes on the Synthesis of Form.*
- Olgyay, V. (1963). *Design with Climate.* Princeton University Press.
- Givoni, B. (1998). *Climate Considerations.* Van Nostrand Reinhold.
- Norberg-Schulz, C. (1979). *Genius Loci.*
- Arnheim, R. (1969). *Visual Thinking.*
- Clark, R. & Pause, M. (2005). *Precedents in Architecture.*
- Zeisel, J. (2006). *Inquiry by Design.* Norton.
- Newman, O. (1972). *Defensible Space.* Macmillan.
- Gehl, J. (1971). *Life Between Buildings.*
- Holahan, C. (1982). *Psicología Ambiental.*
- Neufert, E. (1936). *El Arte de Proyectar.* Gustavo Gili.
- Panero, J. & Zelnik, M. (1979). *Human Dimension.*
