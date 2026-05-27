# PROTOCOLO 01: RECEPCION Y EXTRACCION
## Bloque 2 — Taller SOMA (Operacion)

Este protocolo define la captura inicial de datos del cliente. Se compone de dos
fases complementarias: la **Inmersion Web** (pre-filtro digital) y la **Entrevista
de Inmersion** (presencial). El presente documento cubre las estructuras de datos
que ambas fases deben poblar.

---

## 1. UserEntity (Entidad Habitante)

Cada habitante del proyecto debe desglosarse en:

### Atributos Estaticos
- Edad, altura (ergonomia), limitaciones fisicas/movilidad.

### Atributos Dinamicos
- Ocupacion, hobbies que requieren espacio, equipamiento personal.

### Roles de Poder
- % de decision en el diseno.
- % de tiempo de ocupacion del espacio.
- Quien financia, quien habita mas tiempo.

---

## 2. Zonificacion Maestra SOMA (Vigente)

Todo espacio y actividad se clasifica en una de estas 5 zonas:

| Zona | Tipo | Ejemplos |
|------|------|----------|
| **Social** | Interaccion / Publico | Sala, comedor, terraza, jardin social |
| **Descanso** | Introspeccion / Privado | Recamaras, area de lectura, zona de siesta |
| **Operativa** | Produccion / Trabajo | Oficina, estudio, taller, cocina (tecnica), gimnasio |
| **Soporte** | Logistica / Servicios | Lavado, bodega, cochera, cuarto de servicio, cocina (logistica) |
| **Transicion** | Conectividad / Cinematica | Pasillos, vestibulos, portal de entrada, escaleras |

---

## 3. Inmersion Visual (10 Ejes de Diseno)

Ejes capturados en el pre-filtro web mediante comparacion visual A/B.
Cada eje se registra en escala 0–10 y se inyecta como parametro de diseno.

| # | Eje | Polaridad Izquierda | Polaridad Derecha |
|---|-----|---------------------|-------------------|
| 1 | Fachada | Abierta | Cerrada |
| 2 | Privacidad | Abierta (visibilidad total) | Recibidor (gradacion de intimidad) |
| 3 | Planta | Abierta | Fraccionada |
| 4 | Iluminacion | Directa | Tenue |
| 5 | Tacto | Textura | Liso |
| 6 | Niveles | Un nivel | Varios |
| 7 | Paisaje | Verde | Petreo |
| 8 | Escala | Acogedor | Amplio |
| 9 | Perfil Social | Activo | Privado |
| 10 | Color | Neutral | Caracter |

---

## 4. CreativeCore (5 Ejes de Tension)

Ejes conceptuales para definir la intencion poetica del proyecto. Se extraen
durante la entrevista de inmersion (Topic 6: "La cereza del pastel").

| # | Eje | Polaridad A | Polaridad B |
|---|-----|-------------|-------------|
| 1 | Tension | Tension | Calma |
| 2 | Materialidad | Brutalismo | Refinamiento |
| 3 | Relacion con el exterior | Privacidad | Transparencia |
| 4 | Geometria | Ortogonalidad | Organicismo |
| 5 | Tiempo | Permanencia | Efimeridad |

---

## 5. ActivityMatrix (24 Slots)

Cada habitante genera una matriz de 24 slots (1 por hora) que determina
necesidades de aislamiento e iluminacion para la zonificacion.

### Variables por slot
- **Actividad:** Descripcion breve.
- **Aislamiento:** 0 (nulo) – 10 (absoluto).
- **Iluminacion:** Natural, Tenue, Oscuridad, Artificial.
- **Zona SOMA:** Social / Descanso / Operativa / Soporte / Transicion / (fuera).

### Formato de captura

```
Habitante: [nombre]
| Hora | Actividad | Aisl. | Iluminacion | Zona SOMA |
|------|-----------|-------|-------------|-----------|
| 0:00 | Duerme    | 5     | Oscuridad   | Descanso  |
| ...  | ...       | ...   | ...         | ...       |
| 23:00| ...       | ...   | ...         | ...       |
```

### Salida esperada
- Mapa de calor de 24h por habitante.
- Determinacion de necesidades de aislamiento acustico/visual.
- Determinacion de preferencias de iluminacion por franja horaria.
- Alimentacion del grid interactivo en el Dashboard (colores SOMA por zona).

---

## 6. Matriz de Inversion (EconomicEntity)

- **Capacidad Total:** Presupuesto global disponible.
- **Prioridad de Gasto:** Invertir en estructura (espacios grandes) vs. acabados
  (detalles de lujo).
- **Fases:** Construccion unica o por etapas segun flujo de efectivo.

---

## 7. Requerimientos Tecnicos No Evidentes

- **Almacenamiento especifico:** Colecciones, equipamiento deportivo, instrumentos.
- **Crecimiento futuro:** Espacios convertibles (oficina que sea recamara, etc.).
- **Mantenimiento:** Capacidad del cliente para cuidar materiales vivos (madera,
  plantas, piedra natural).

---

## FUENTES

- **Edward T. Hall**, *The Hidden Dimension* (1966) — teoría proxémica: bases de las distancias interpersonales que alimentan la UserEntity.
- **C. M. Deasy**, *Design Places for People* (1974) — metodología de observación de usuarios, extracción de patrones de comportamiento para diseño.
- **Christopher Alexander**, *A Pattern Language* (1977) — patrones de vida doméstica que informan la recolección de datos del usuario. (patternlanguage.com)
- **Robert Sommer**, *Personal Space: The Behavioral Basis of Design* (1969) — territorialidad, espacio personal, bases para la UserEntity.
- **William Peña**, *Problem Seeking: An Architectural Programming Primer* (5th ed., 2012) — método de programación arquitectónica en 4 fases (Metas, Hechos, Conceptos, Necesidades), validación directa del flujo SOMA.
- **Donna Duerk**, *Architectural Programming: Information Management for Design* (1993) — técnicas de entrevista y extracción de datos del cliente, refuerza UserEntity.
- **Edith Cherry**, *Programming for Design: From Theory to Practice* (1998) — de la teoría al programa arquitectónico, puente entre Recepción y Conceptualización.
- **John Zeisel**, *Inquiry by Design: Tools for Environment-Behavior Research* (1984) — investigación social como insumo de diseño, valida Inmersión y ActivityMatrix.
- **Charles J. Holahan**, *Psicología Ambiental: Un Enfoque General* (1982 / original *Environmental Psychology*, Random House) — relación entre comportamiento y entorno construido, bases psicológicas de la UserEntity y percepción del espacio.
- **Francis D.K. Ching**, *Architecture: Form, Space, & Order* (4th ed., 2014) — principios de escala humana y ergonomía en el espacio. (Referencia de apoyo para la entrevista)
