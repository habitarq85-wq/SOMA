# PROTOCOLO: RECEPCIÓN DE USUARIO — USERENTITY Y ACTIVITY MATRIX
## Bloque 2 — Taller SOMA (Operación)
## Referencia: PROCESO DE DISEÑO 2.0 — Items 2.2.1, 3.10

**Propósito:** Recolectar los datos del usuario/cliente para construir el perfil
de diseño (UserEntity, Activity Matrix, Necesidades No Visibles).

**Relación con el 2.0:**
- **2.2.1 (Investigación)** — datos brutos del usuario (inmersión web + entrevista)
- **3.10 (Análisis)** — procesamiento de esos datos en perfiles, matrices y gráficos

---

## 2.2.1 Datos del Usuario/Cliente (Investigación)

```
[REF→OUT] 2.2.1.1 Datos de Inmersión SOMA (P2.0 ref: 2.2.1.1)
─────────────────────────────────
INPUT:  Cliente responde Inmersión Web (10 ejes visuales A/B +
        formulario de contacto con nombre, teléfono, email, etc.)
OPERA:  El sistema guarda automáticamente las respuestas en la BD
        (tabla captura_web). Recuperar el registro del cliente y
        exportar respuestas crudas a carpeta del proyecto
OUTPUT: `respuestas_inmersion_web.json` (datos en bruto del cliente)
        + `datos_contacto_cliente.txt` (nombre, teléfono, email)
PROC:   AI (recuperación automática desde BD)
```

### Ejes de Inmersión Web

| # | Eje | Opción A | Opción B |
|---|-----|----------|----------|
| 1 | Fachada | Abierta | Cerrada |
| 2 | Privacidad | Abierta | Recibidor |
| 3 | Planta | Abierta | Fraccionada |
| 4 | Iluminación | Directa | Tenue |
| 5 | Tacto | Textura | Liso |
| 6 | Niveles | Uno | Varios |
| 7 | Paisaje | Verde | Pétreo |
| 8 | Escala | Acogedor | Amplio |
| 9 | Perfil Social | Activo | Privado |
| 10 | Color | Neutral | Carácter |

```
[ACC] 2.2.1.2 Entrevista Presencial SOMA (P2.0 ref: 2.2.1.2)
─────────────────────────────────
INPUT:  Cita agendada con el cliente + Guía de Entrevista
        (6 tópicos conversacionales) + respuestas de 2.2.1.1
OPERA:  Sesión presencial con el cliente. Grabar audio continuo
        mientras se conversan los 6 tópicos. Tomar notas de
        observaciones no verbales. El audio se guarda en bruto
        para transcripción posterior
OUTPUT: • `entrevista.wav` (audio en bruto)
        • `notas_campo_entrevista.txt` (observaciones del arquitecto)
PROC:   HUMANO (entrevista y grabación)
```

### Guía de 6 Tópicos Conversacionales

1. **La razón de estar aquí** — terreno, reglas, tomador de decisiones, presupuesto incluye terreno
2. **Los habitantes** — edades, salud, hobbies, quién pasa más tiempo, visitas que se quedan
3. **El programa** — recámaras, baños, PB, oficina, cochera, servicio, extras, colecciones
4. **Dinámicas y rutinas** — despertar, comidas, trabajo, llegada, mascotas, orden, materiales, clima
5. **Inversión** — presupuesto realista, etapas, metros vs acabados, honorarios incluidos
6. **La cereza del pastel** — emoción, recuerdo feliz, objeto que dicte diseño, miedos

---

## 3.10 Análisis del Usuario (Análisis)

```
[OUT] 3.10.1 Datos Demográficos (P2.0 ref: 3.10.1)
─────────────────────────────────
INPUT:  2.2.1.1 `respuestas_inmersion_web.json`
        2.2.1.2 Transcripción de entrevista
OPERA:  Extraer y organizar: edad, género, ocupación, composición
        del hogar, nivel de movilidad, roles dentro del hogar
        (quién cocina, quién trabaja desde casa, quién recibe visitas)
OUTPUT: Ficha de composición del hogar y perfiles de habitante
PROC:   AI
```

Campos a extraer por habitante:
- [ ] Nombre / rol (titular, cónyuge, hijo, familiar)
- [ ] Edad / rango de edad
- [ ] Ocupación / actividades principales
- [ ] Salud / movilidad (limitaciones, requerimientos especiales)
- [ ] Hobbies que requieran espacio dedicado
- [ ] Horarios típicos en casa (entre semana vs fin de semana)
- [ ] ¿Toma decisiones estéticas? ¿Económicas?
- [ ] Mascotas (tipo, cantidad, tamaño)

```
[OUT] 3.10.2 Matrices de Actividad / Activity Matrix (P2.0 ref: 3.10.2)
─────────────────────────────────
INPUT:  2.2.1.2 Transcripción de entrevista + notas
        3.10.1 Datos demográficos (habitantes identificados)
OPERA:  Por cada habitante, desglosar 24 slots temporales (1h c/u)
        con: actividad principal, ubicación probable, necesidad de
        aislamiento (alta/media/baja), necesidad de iluminación
        (natural/artificial/ambas), usuarios concurrentes
OUTPUT: Activity Matrix (grid 24h × N habitantes) almacenada en BD
        (tabla actividades) con tooltips por celda
PROC:   AI (estructura desde transcripción) + HUMANO (validación)
```

Zonas SOMA para asignación:
| Zona | Nombre | Ejemplos |
|------|--------|----------|
| 1 | Social | Sala, comedor, estar |
| 2 | Descanso | Recámaras, estudio |
| 3 | Operativa | Cocina, lavandería, oficina |
| 4 | Soporte | Bodega, cuarto de instalaciones, cochera |
| 5 | Transición | Pasillos, vestíbulo, escaleras |

```
[OUT] 3.10.3 Gráficos de Rutinas y Frecuencias (P2.0 ref: 3.10.3)
─────────────────────────────────
INPUT:  3.10.2 Activity Matrix
        3.3 Programa Arquitectónico (espacios)
OPERA:  Graficar a partir de la matriz: rutinas diarias por habitante,
        frecuencias de uso por espacio (alta/media/baja), horarios de
        conflicto (múltiples usuarios simultáneos), patrones de uso
OUTPUT: Gráficos de rutinas y frecuencias (dashboard o lámina)
PROC:   AI (generación de gráficos desde datos estructurados)
```

```
[OUT] 3.10.4 Perfil de Diseño (Inmersión SOMA) (P2.0 ref: 3.10.4)
─────────────────────────────────
INPUT:  2.2.1.1 `respuestas_inmersion_web.json` (10 ejes A/B)
        2.2.1.2 Transcripción de entrevista (matices cualitativos)
OPERA:  Cruzar datos de inmersión (selecciones A/B visuales) con
        observaciones cualitativas de la entrevista para construir
        un perfil de diseño completo
OUTPUT: Perfil de diseño del cliente (documento de guía)
PROC:   AI (ejes) + HUMANO (interpretación de matices)
```

```
[DEC] 3.10.5 Selección de Necesidades No Visibles (P2.0 ref: 3.10.5)
─────────────────────────────────
INPUT:  2.2.1.2 Transcripción y notas de entrevista
        Catálogo SOMA de necesidades comunes por tipo de proyecto
OPERA:  AI sugiere lista de necesidades no visibles típicas
        (almacenamiento, lavandería, bodega, tendedero, cuarto de
        instalaciones, etc.). Humano evalúa cuáles aplican y agrega
        las específicas del cliente
OUTPUT: Lista de necesidades no visibles integradas al programa
PROC:   AI→HUMANO
```

Necesidades no visibles comunes:
- [ ] Lavandería / Cuarto de lavado
- [ ] Tendedero (interior y exterior)
- [ ] Bodega / Almacenamiento general
- [ ] Despensa
- [ ] Cuarto de instalaciones (calentador, tinaco, bomba)
- [ ] Área de mascotas
- [ ] Estacionamiento de visitas
- [ ] Cuarto de herramientas / taller
- [ ] Espacio para bicicletas
- [ ] Área de carga para vehículo eléctrico

---

## Salida del Protocolo

Al completar la recepción de usuario se genera en `backend/proyectos/SOMA-XXXX/`:

```
├── info.json                    ← metadatos del proyecto
├── respuestas_inmersion_web.json ← 10 ejes A/B + contacto
├── entrevista.wav               ← audio de entrevista
├── notas_campo_entrevista.txt   ← observaciones del arquitecto
├── datos_estructurados.json     ← Activity Matrix + perfiles
├── perfil_diseno_cliente.md     ← perfil de diseño procesado
└── necesidades_no_visibles.md   ← checklist complementario
```

## FUENTES

- Hall, E. T. (1966). *The Hidden Dimension.* Doubleday.
- Alexander, C. et al. (1977). *A Pattern Language.* Oxford University Press.
- Ching, F. (2014). *Arquitectura: Forma, Espacio y Orden.* Gustavo Gili.
- Peña, W. & Parshall, S. (2001). *Problem Seeking.* Wiley.
- Deasy, C. M. & Lasswell, T. E. (1990). *Designing Places for People.* Whitney Library of Design.
- Zeisel, J. (2006). *Inquiry by Design.* Norton.
- Holahan, C. J. (1982). *Environmental Psychology.* Random House.
