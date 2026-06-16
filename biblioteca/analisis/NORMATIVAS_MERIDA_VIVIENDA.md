# Normativas Aplicables — Diseño de Vivienda en Mérida

> Biblioteca de Análisis SOMA
> Fuentes: Reglamento de Construcciones del Municipio de Mérida (2018), NOM-020-ENER-2011
> Clima: cálido-húmedo, Mérida, Yucatán

---

## 1. Reglamento de Construcciones del Municipio de Mérida

### 1.1 Requisitos Mínimos de Vivienda

**Artículo 68.** Solo se autorizará la construcción de viviendas que tengan como mínimo un espacio destinado a **dormitorio con guardarropa**, aparte de contar con sus servicios completos de **cocina y baño**.

**Artículo 69.** Cada vivienda debe contar con servicios propios de baño: cuando menos un **inodoro, una regadera** y uno de los siguientes: **lavabo, fregadero o lavadero**.

### 1.2 Normas de Proyecto Arquitectónico

**Artículo 63.** Las Normas Técnicas Complementarias (NTC) rigen el proyecto arquitectónico de todo inmueble habitable, sobre todo la **vivienda**. Son emitidas por la Dirección de Desarrollo Urbano y publicadas en Gaceta Municipal.

**Artículo 64.** El proyecto arquitectónico se regirá con base en las **Normas Técnicas Complementarias** y demás disposiciones legales aplicables.

**Artículo 65.** La **altura máxima** de edificios no podrá exceder del **doble del ancho de la vialidad** de su ubicación, incluyendo aceras. En predios en esquina, la medida base será la vialidad más ancha.

**Artículo 66.** Ventanas hacia colindancias a partir del segundo piso que no cumplan 1.00 m desde la línea de separación: **antepecho no menor a 1.50 m** o elemento arquitectónico que evite vistas oblicuas.

**Artículo 67.** El destino de cada espacio debe ser **congruente con su ubicación, funcionamiento y dimensión**. Debe indicarse en planos.

### 1.3 Norma Bioclimática

**Artículo 77.** Toda construcción en Mérida debe sujetarse a los criterios de la **Norma Técnica Complementaria en materia de eficiencia energética y diseño bioclimático** para mejorar el medio ambiente, preservar recursos naturales y salvaguardar la seguridad del usuario.

### 1.4 Circulaciones

**Artículo 79.** Circulaciones (corredores, túneles, pasillos, escaleras, rampas) deben ajustarse a dimensiones mínimas establecidas en el Reglamento y NTC.

**Artículo 80.** Todos los locales deben contar con salidas y pasillos que conduzcan directamente a puertas de salida o escaleras. Los pasillos de uso público no deben tener salientes que disminuyan el ancho interior requerido.

**Artículo 81.** Toda edificación debe tener **escaleras o rampas peatonales** que comuniquen todos sus niveles, aun cuando existan elevadores.

### 1.5 Estacionamientos

**Artículo 83.** Estacionamientos públicos:
- Circulaciones peatonales (aceras, andadores, escaleras, rampas) separadas de vehiculares
- Edificios hasta 3 plantas: se puede prescindir de elevadores si hay escaleras/rampas de mínimo **1.20 m de ancho**
- Más de 3 plantas: obligatorio elevador(es)

**Artículo 84.** El estacionamiento privado es complementario al uso de suelo y está amparado por la Licencia de Uso de Suelo. No puede modificarse ni cobrarse.

### 1.6 Accesibilidad

**Artículo 82.** Edificios de uso público o común deben tener **libre acceso, tránsito y uso confortable** para personas con discapacidad, ya sea para trabajo, educación, vivienda o recreación.

### 1.7 Aguas Pluviales

**Artículo 70.** Las aguas pluviales de techos y terrazas deben drenarse **dentro de cada predio** por instalaciones específicas. No pueden tener salida a la vía pública ni drenar sobre predios colindantes.

### 1.8 Industria y Talleres (Colindancias)

**Artículo 75.** Edificios para bodegas, industrias o talleres: muros altos (mín. 3.00 m) para impedir paso de ruidos o residuos a vecinos. Separación mínima de colindancias:
- Edificios de hasta 6.00 m de altura: **1.20 m**
- Mayores a 6.00 m: **20% de la altura** hasta 3.50 m

---

## 2. NOM-020-ENER-2011 — Envolvente de Edificios para Uso Habitacional

> Norma Oficial Mexicana de aplicación federal. Limita la **ganancia de calor** a través de la envolvente del edificio.

### 2.1 Definiciones Clave

| Término | Definición |
|---------|------------|
| **Envolvente** | Estructura que limita un espacio por medio de techos, paredes, ventanas, domos o tragaluces |
| **Muro masivo** | Muro con densidad ≥ 600 kg/m³ (block de concreto, tabique, piedra) |
| **Muro ligero** | Muro con densidad < 600 kg/m³ (panel yeso, madera, acero) |
| **Coeficiente de sombreado** | Valor adimensional entre 0 y 1 determinado por la sombra que proyecta un dispositivo |
| **Factor de ganancia solar** | Promedio de radiación solar que recibe cada orientación, en W/m² |
| **Edificio de referencia** | Edificio hipotético con misma orientación, mismas condiciones que el proyectado, usado como comparación |

### 2.2 Método de Verificación

La ganancia total de calor a través de la envolvente del edificio proyectado (**G_proy**) debe ser **menor o igual** a la del edificio de referencia (**G_ref**):

```
G_proy ≤ G_ref
```

**Componentes de la ganancia de calor:**
1. **Ganancia por conducción** — a través de partes opacas (muros, techos) y no opacas (ventanas)
2. **Ganancia por radiación solar** — a través de partes no opacas (ventanas, domos)

### 2.3 Factores de Corrección por Sombreado Exterior

Los volados (aleros) sobre ventanas reducen la ganancia solar. El factor de corrección de sombreado (**Se**) depende de la relación **L/H** (proyección del volado / altura de ventana) y la orientación:

| L/H | Norte | Este y Oeste | Sur |
|-----|-------|-------------|-----|
| 0.00 | 1.00 | 1.00 | 1.00 |
| 0.25 | — | 0.78 | — |
| 0.50 | — | 0.57 | — |
| 0.75 | — | 0.45 | — |
| 1.00 | — | 0.37 | — |

*Nota: Los valores varían según tipo de volado (I: con extensión lateral ≥ proyección; II: sin extensión lateral). Ver tablas completas en Apéndice A.2 de la NOM.*

### 2.4 Aplicación Práctica para Vivienda en Mérida

| Elemento | Estrategia |
|----------|------------|
| **Cubierta** | Color claro (reflectividad ≥ 0.70), cámara de aire ventilada, aislamiento térmico (R ≥ 1.5 m²K/W) |
| **Muros** | Muro masivo (block de concreto, tabique) con repellado exterior claro; muro doble con cámara de aire en orientaciones E y O |
| **Ventanas** | Volado/alero con L/H ≥ 0.50 en E y O, vidrio de control solar (coeficiente de sombreado ≤ 0.60) |
| **Orientación** | Fachadas largas orientadas N-S para minimizar radiación en E-O |
| **Protección solar** | Partesoles, celosías, pérgolas — todos reducen el factor de ganancia solar |

---

## 3. Referencias a las Normas Técnicas Complementarias (NTC)

Las NTC se publican en la Gaceta Municipal 932 (5 enero 2018) como anexos al Reglamento:

| Anexo | Contenido |
|-------|-----------|
| **NTC Eficiencia Energética y Diseño Bioclimático** | Criterios específicos de diseño pasivo para Mérida: orientación, ventilación, protección solar, aislamiento, reflectancia, estrategias bioclimáticas |
| **NTC para Proyecto Arquitectónico** (Suplemento I y II) | Dimensiones mínimas de espacios, alturas libres, proporciones de vanos, requisitos de habitabilidad, especificaciones técnicas de diseño |

*Nota: El contenido detallado de las NTC se encuentra en el PDF `gaceta_932_ntc_merida.pdf` (formato 2 columnas, extracción parcial). Se recomienda consulta directa del PDF para valores exactos.*

---

## 4. Tabla de Artículos por Tema de Diseño

| Tema | Artículo / Norma | Aplica a |
|------|-----------------|----------|
| Programa mínimo de vivienda | RCM Art. 68–69 | Toda vivienda |
| Normas de proyecto arquitectónico | RCM Art. 63–64 | Todo proyecto |
| Altura máxima de edificación | RCM Art. 65 | Toda edificación |
| Ventanas en colindancias | RCM Art. 66 | Segundo piso+ |
| Congruencia de espacios | RCM Art. 67 | Todo proyecto |
| Aguas pluviales | RCM Art. 70 | Toda edificación |
| Diseño bioclimático | RCM Art. 77 | Toda edificación |
| Accesibilidad universal | RCM Art. 82 | Edificios públicos/comunes |
| Circulaciones mínimas | RCM Art. 79–81 | Toda edificación |
| Estacionamientos | RCM Art. 83–84 | Según uso |
| Separación a colindancias (talleres) | RCM Art. 75 | Usos no habitacionales |
| Ganancia de calor envolvente | NOM-020-ENER-2011 | Toda vivienda |
| Factor de sombreado exterior | NOM-020 Apéndice A.2 | Ventanas con alero/volado |
| Transmitancia térmica | NOM-020-ENER-2011 | Muros, techos, vidrios |

> **Abreviaturas:** RCM = Reglamento de Construcciones de Mérida; NTC = Normas Técnicas Complementarias

---

## 5. Requisitos de Planos para Licencia de Construcción

Los requisitos varían según la magnitud de la obra (Art. 29 RCM).

### 5.1 Obra ≤ 45 m² cubiertos en PB y bardas ≤ 2.50 m

| Documento | Descripción |
|-----------|-------------|
| Escritura de propiedad | Copia del testimonio o documento notariado que compruebe la posesión |
| Pago de predial | Estar al corriente |
| **2 croquis** | Tamaño carta o doble carta, con medidas y escalas. Puede usarse la chepina catastral para señalar la ampliación |
| INAH | Autorización del INAH si está en Zona de Monumentos o Protección Arqueológica |
| Licencia de Uso de Suelo | Solo si el uso es diferente a vivienda |

### 5.2 Obra > 45 m² cubiertos en PB o cualquier superficie en PA

| Documento | Descripción |
|-----------|-------------|
| **5 juegos de planos** | Tamaño doble carta o mayor, legibles, con firma de PCM. Deben incluir: |
| a) Planta de localización | Ubicando el terreno con radio de 250.00 m |
| b) Planta de conjunto | Acotada, señalando ubicación de la construcción, pendientes y descargas pluviales |
| c) Planta(s) arquitectónica(s) de levantamiento | Debidamente acotadas (solo para ampliación) |
| d) Planta(s) arquitectónica(s) | Escalas **1:50, 1:75, 1:100 o 1:125**, acotadas y referenciadas a ejes, con nombre de cada área o local |
| e) Fachadas o elevaciones | Vistas a la vía pública o privada, mismas escalas, acotadas |
| f) **2 cortes representativos** | Escalas 1:50 a 1:125, acotados, con referencias de niveles. Uno debe incluir secciones de **baño(s) y escalera(s)** |
| g) Sistema de aguas residuales | Ubicación del sistema de tratamiento y cisterna |
| h) Memoria(s) de cálculo | Cuando lo indique el Art. 12 |
| i) Archivo digital | AutoCAD 2010 en formato **DWG** |
| INAH | Autorización del INAH si aplica (Zona de Monumentos o Arqueológica) |
| Licencia de Uso de Suelo | Si el uso es diferente a vivienda |
| Autorización vial | Para usos que lo requieran (SSP o Policía Municipal) |

### 5.3 Edificios de Habitación Multifamiliar Vertical (> 2 niveles), Comercio, Oficinas, etc.

Además de todo lo anterior:
| Documento | Descripción |
|-----------|-------------|
| Memorias de diseño | De todas las instalaciones necesarias para el funcionamiento y seguridad |
| Autorizaciones complementarias | Estudios y resolutivos determinados en la Licencia de Uso de Suelo |

### 5.4 Notas Importantes

- **PCM**: Toda obra > 45 m² requiere firma de Perito en Construcción Municipal
- **Planos**: Deben indicar el **destino de cada espacio** (Art. 67), congruente con su ubicación, funcionamiento y dimensión
- **Escaleras/rampas**: Toda edificación debe tener escaleras o rampas peatonales que comuniquen todos sus niveles (Art. 81)
- **Planta baja ≤ 45 m² sin PCM**: Solo se requiere croquis (no planos formales), pero se limita a vivienda unifamiliar básica
- **Uso diferente a vivienda**: Siemrequiere Licencia de Uso de Suelo vigente

---

## 6. Resumen de Criterios de Diseño para Vivienda

| Aspecto | Requisito / Recomendación |
|---------|--------------------------|
| **Dormitorio mínimo** | 1 dormitorio con guardarropa |
| **Baño mínimo** | Inodoro + regadera + lavabo/fregadero/lavadero |
| **Cocina** | Obligatoria, sin especificación dimensional en reglamento |
| **Altura máxima** | 2× ancho de vialidad |
| **Separación a colindancia (ventanas 2° piso+)** | ≥ 1.00 m o antepecho ≥ 1.50 m |
| **Ganancia de calor envolvente** | G_proy ≤ G_ref (NOM-020) |
| **Alero mínimo recomendado** | L/H ≥ 0.50 en ventanas E y O |
| **Color de cubierta** | Claro (reflectividad ≥ 0.70) |
| **Muros** | Masivos en E y O; cámara de aire recomendada |
| **Aguas pluviales** | Drenaje dentro del predio |
| **Circulaciones** | Ancho mínimo de pasillos según NTC |
| **Estacionamiento** | Según tabla de compatibilidad del PMDU |

---

> Documento preparado junio 2026 — Extraído de Reglamento de Construcciones de Mérida (v. 2018), NOM-020-ENER-2011, y Gaceta Municipal 932.

