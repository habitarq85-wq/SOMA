# PROTOCOLO: PLANOS TÉCNICOS
## Bloque 2 — Taller SOMA (Operación) | Etapa 10 del Ciclo

### ¿Qué son los Planos Técnicos?

Es la documentación constructiva detallada que un contratista necesita para construir el proyecto. Solo se produce para el paquete **SOMA Ejecutivo**.

**Entrada:** Anteproyecto aprobado por el cliente (de Etapa 9).
**Salida:** Juego completo de planos técnicos + detalles constructivos.

### Principio rector

Un buen plano técnico no tiene instrucciones escritas — las cotas, las notas y los detalles deben ser tan claros que un constructor competente pueda ejecutar sin preguntar.

---

## 1. PLANOS EJECUTIVOS ARQUITECTÓNICOS (Escala 1:50)
(Fuentes: ISO 13567 — Technical product documentation, Organization and naming of layers; NOM-008-SCFI — Sistema General de Unidades de Medida; Ching, Building Construction Illustrated)

### 1.1 Plantas Ejecutivas
(Fuente: Ching, Building Construction Illustrated — Drawing Conventions)

- [ ] **Muros:** Espesor exacto con capas (block + repellado + pintura / block + cámara + tablaroca)
- [ ] **Vanos:** Identificación V-1, V-2... con dimensiones exactas de paño y derrame
- [ ] **Puertas:** Identificación P-1, P-2... con especificación (madera sólida, tambor, herrajes)
- [ ] **Acabados:** Símbolo de piso (material) en cada espacio con referencia a especificación
- [ ] **Fijaciones:** Muebles de baño y cocina acotados (wc, lavabo, campana)
- [ ] **Equipos:** Calentador, tinaco, cisterna, minisplit — ubicación exacta
- [ ] **Cotas:** Cadena de cotas completa (ejes estructurales, paños de muros, vanos)
- [ ] **Niveles:** NPT de cada espacio (precisión ±0.5cm)
- [ ] **Cortes de detalle:** Indicar con círculo y referencia (ej: "DET-01")
- [ ] **Cuadro de vanos:** Tabla en la misma lámina con dimensiones y especificaciones

### 1.2 Cortes Ejecutivos (Escala 1:25 o 1:20)
- [ ] **Composición de cubierta:** Capa por capa (losa, impermeabilizante, aislante, acabado)
- [ ] **Composición de muro exterior:** Capa por capa con espesores
- [ ] **Cimentación:** Tipo, profundidad, armado esquemático (dimensión de zapata o losa)
- [ ] **Encuentro muro-cubierta:** Detalle de junta, impermeabilización, goterón
- [ ] **Losa de entrepiso:** Espesor, capas de compresión, acabado
- [ ] **Niveles:** Benchmarks de referencia (NPT + NPT + banqueta + terreno natural)

### 1.3 Detalles Constructivos (Escala 1:10, 1:5)
- [ ] **Encuentros críticos:**
  - Muro-cubierta (impermeabilización)
  - Muro-piso (zócalo, junta)
  - Vanos (derrame, marco, burlete)
  - Cambio de material (ej: concreto-madera)
  - Escaleras (arranque, descanso, llegada)
  - Barandal (fijación a piso/muro, perfil)
  - Celosías y protecciones solares
- [ ] **Especificaciones de materiales en cada detalle:**
  - Tipo de material
  - Espesor
  - Acabado
  - Método de fijación
- [ ] **Referencias cruzadas:** Cada detalle debe tener código único y referencia al corte/planta donde se ubica

---

## 2. PLANOS DE INGENIERÍAS (Coordinados por SOMA, desarrollados por especialistas)
(Fuente: NOM-001-SEDE — Instalaciones Eléctricas; Reglamento de Construcción Mérida — Instalaciones hidrosanitarias)

### 2.1 Instalaciones Hidrosanitarias (Esquemático ejecutivo)
(Fuente: Normativa IMSS, CFE, SAPAO — estándares de instalaciones)

- [ ] **Agua fría:** Diagrama de distribución (diámetros, material, válvulas)
- [ ] **Agua caliente:** Retorno, calentador, diámetros
- [ ] **Aguas negras:** Bajadas, colector horizontal, registro, conexión municipal
- [ ] **Aguas pluviales:** Bajadas pluviales, canaletas, cisterna pluvial (si aplica)
- [ ] **Gas:** Ubicación de calentador, diámetro de tubería, ventilación

### 2.2 Instalaciones Eléctricas (Esquemático)
(Fuente: NOM-001-SEDE — Instalaciones Eléctricas)

- [ ] **Diagrama unifilar:** Tablero principal, circuitos derivados, cargas estimadas
- [ ] **Puntos de luz y contacto:** Ubicación en planta con simbología estándar
- [ ] **Cálculo de carga:** Carga total estimada, factor de demanda
- [ ] **Acometida:** Diámetro de alimentador, protección principal

### 2.3 Instalaciones Especiales (si aplica)
- [ ] **Aire acondicionado:** Ubicación de evaporadoras y condensadoras, ruta de refrigerante
- [ ] **Paneles solares:** Área requerida, orientación, estructura de soporte
- [ ] **Sistema de captación pluvial:** Filtro, cisterna, bomba (si aplica)
- [ ] **Domótica / automatización:** Diagrama de control (si aplica, solo Ejecutivo+)

---

## 3. ESPECIFICACIONES GENERALES (Documento aparte)
(Fuente: prácticas de especificación en proyectos residenciales mexicanos — Duarte Aznar)

Documento de texto con:

- **Generalidades:** Normas aplicables, calidad de materiales, mano de obra
- **Obra civil:** Excavación, relleno, cimentación (dosificación de concreto, resistencia)
- **Albañilería:** Block, repellado, aplanados, azulejos
- **Acabados:** Pintura, pisos, plafones, carpintería
- **Instalaciones:** Hidrosanitaria, eléctrica, gas (normas aplicables)
- **Carpintería:** Tipo de madera, herrajes, barniz
- **Herrería:** Perfiles, soldadura, acabado
- **Impermeabilización:** Tipo, marcas recomendadas, garantía

---

## 4. NAMING DE PLANOS

Convención:
```
SOMA-{CLIENTE}-{DISCIPLINA}-{CONTENIDO}-{NUMERO}.pdf
```

| Disciplina | Contenido | Ejemplo |
|-----------|-----------|---------|
| ARQ | PL-BAJA, PL-ALTA, CORTE-A, CORTE-B, FACH-NORTE | SOMA-LOPEZ-ARQ-PL-BAJA.pdf |
| ARQ | DET-01, DET-02 | SOMA-LOPEZ-ARQ-DET-01.pdf |
| EST* | CIMENTACION, TRABES, LOSAS | SOMA-LOPEZ-EST-CIMENTACION.pdf |
| HIDRO | AGUA, DRENAJE, PLUVIAL | SOMA-LOPEZ-HIDRO-AGUA.pdf |
| ELECTR | ILUMINACION, CONTACTOS, DIAGRAMA | SOMA-LOPEZ-ELECTR-ILUMINACION.pdf |
| GAS | GAS-LINEA, GAS-DETALLE | SOMA-LOPEZ-GAS-LINEA.pdf |

*Las disciplinas EST, HIDRO, ELECTR y GAS son planos de **especialistas externos coordinados por SOMA** (incluidos solo en paquete Ejecutivo).

---

## 5. CHECKLIST DE REVISIÓN TÉCNICA

- [ ] ¿Todas las cotas son consistentes entre planos? (planta vs corte vs detalle)
- [ ] ¿Las referencias cruzadas de detalles son correctas?
- [ ] ¿La simbología es consistente (norte, cortes, niveles)?
- [ ] ¿Las notas especifican materiales, espesores y acabados?
- [ ] ¿Las instalaciones no interfieren con la estructura? (ductos vs vigas)
- [ ] ¿Los planos de ingenierías son coherentes con los arquitectónicos?
- [ ] ¿El formato de impresión es doble carta o A3?
- [ ] ¿Cada lámina tiene: nombre de proyecto, escala, fecha, número de lámina, proyectista?

---

## 6. SALIDA DE PLANOS TÉCNICOS

1. **Juego de planos ejecutivos** en PDF (archivos individuales + PDF unificado)
2. **Archivos fuente** editables (.rvt, .dwg, .blend según herramienta)
3. **Especificaciones generales** en PDF
4. **Carpeta de planos** en `proyectos/SOMA-XXXX/planos_tecnicos/`

Este juego de planos + especificaciones es el **entregable final del paquete Ejecutivo**.

---

## FUENTES

- **Francis D.K. Ching**, *Building Construction Illustrated* (6th ed., 2020) — detalles constructivos, composición de muros, cortes ejecutivos, especificaciones.
- **Francis D.K. Ching**, *Architectural Graphics* (6th ed., 2015) — convenciones de dibujo técnico, simbología de instalaciones, organización de juegos de planos.
- **C. M. Deasy**, *Design Places for People* (1974) — como los planos tecnicos deben garantizar que la intencion de diseno se mantenga en construccion.
- **Jacques Paul Grillo**, *Form, Function and Design* (1960) — coherencia entre la documentacion tecnica y la idea formal original.
- **ISO 13567** — Technical product documentation, Organization and naming of layers. (iso.org)
- **ISO 19650-1:2018** — Organization and digitization of information about buildings and civil engineering works (BIM). (iso.org)
- **BIM Forum**, *LOD Specification* (2023) — nivel de desarrollo para planos ejecutivos (LOD 350+). (bimforum.org)
- **NOM-001-SEDE** — Instalaciones Eléctricas.
- **NOM-008-SCFI** — Sistema General de Unidades de Medida.
- **Andrea Deplazes** (ed.), *Constructing Architecture: Materials, Processes, Structures* (3rd ed., 2005) — detalles constructivos, manual tectónico para especificaciones técnicas.
- **Edward Allen**, *Fundamentals of Building Construction* (7th ed., 2019) — construcción en detalle, composición de elementos constructivos, especificaciones.
- **IMCA (Instituto Mexicano del Cemento y del Concreto)** — manuales de construcción en México: costos, materiales, rendimientos típicos. (imcyc.com)
- **NMX-R-001-SCFI-2015** — Dibujo técnico, nomenclatura oficial de planos, simbología normalizada.
- **Reglamento de Construcción del Municipio de Mérida** — requisitos de planos ejecutivos para permiso.

---

*"Un detalle constructivo vale más que mil palabras de especificación."*
