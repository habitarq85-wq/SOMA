# RUTA DEL ARQUITECTO — SOMA Taller Virtual de Arquitectura

Checklist operativo interno: lo que Juan hace en cada fase, con qué herramientas y qué entregables produce.

```
NOTIFICACIÓN ──> INMERSIÓN ──> ANÁLISIS ──> DISEÑO ──> ENTREGA ──> CIERRE
```

---

## FASE 0 — RECEPCIÓN DEL LEAD

- [ ] Llega notificación (Twilio/SendGrid) — nuevo lead en DB
- [ ] Abrir Dashboard → ver lead en columna **lead**
- [ ] Leer respuestas de inmersión web (10 preguntas A/B)
- [ ] Contactar al cliente por WhatsApp en < 24 hrs
- [ ] Agendar entrevista presencial (6 temas, 45-60 min)
- [ ] Preparar guía de entrevista según respuestas de inmersión
- [ ] Pipeline → **entrevistado**

**Herramientas:** Dashboard, WhatsApp, App Entrevista (puerto 5050)
**Entregable:** Lead calificado + cita agendada

---

## FASE 1 — ENTREVISTA DE INMERSIÓN

- [ ] Abrir App de Entrevista en tablet/laptop
- [ ] Registrar respuestas del cliente en los 6 tópicos:
  - [ ] T1 — Historia y motivación del proyecto
  - [ ] T2 — Estilo de vida y rutina
  - [ ] T3 — Gustos estéticos y referencias
  - [ ] T4 — Necesidades espaciales
  - [ ] T5 — Presupuesto y expectativas
  - [ ] T6 — Limitaciones y restricciones
- [ ] Tomar fotos del sitio o referencias que el cliente lleve
- [ ] Guardar entrevista (POST a backend)
- [ ] Enviar resumen al cliente por WhatsApp
- [ ] Pipeline → (siguiente fase)

**Herramientas:** App Entrevista, WhatsApp
**Entregable:** Entrevista registrada + resumen al cliente

---

## FASE 2 — PROGRAMA ARQUITECTÓNICO

- [ ] Extraer lista de espacios deseada de la entrevista
- [ ] Clasificar espacios:
  - [ ] **Zona Social:** sala, comedor, cocina
  - [ ] **Zona Operativa:** estudio, bodega, lavandería
  - [ ] **Zona Descanso:** recámaras, baños
  - [ ] **Zona Soporte:** cochera, cuarto de máquinas
  - [ ] **Zona Transición:** pasillos, vestíbulo, pórtico
- [ ] Asignar m² a cada espacio (usar tabla de mínimos)
- [ ] Calcular m² total (circulación incluida)
- [ ] Asignar nivel de paquete: Esencial / Integral / Ejecutivo
- [ ] Generar cotización desde el Dashboard
- [ ] Revisar viabilidad: ¿cubre el mínimo de $6,500?
- [ ] Pipeline → **programado**

**Herramientas:** Dashboard, `01_PROTOCOLO_ANALISIS.md`
**Entregable:** Programa arquitectónico + cotización

---

## FASE 3 — CIERRE COMERCIAL

- [ ] Preparar carpeta para el cliente:
  - [ ] Carta de presentación SOMA
  - [ ] Cotización formal impresa
  - [ ] Convenio de anticipo (2 copias)
  - [ ] Contrato de diseño (2 copias)
- [ ] Presentar y explicar niveles de servicio
- [ ] Resolver dudas de alcance y entregables
- [ ] Firmar convenio + contrato (ambas partes)
- [ ] Recibir anticipo 30% (transferencia o efectivo)
- [ ] Generar recibo / nota de pago
- [ ] Generar esquema 30/40/30 en Dashboard
- [ ] Enviar confirmación por WhatsApp
- [ ] Pipeline → **contratado**

**Herramientas:** Documentos Bloque 1, Dashboard (`POST /cobros/generar_esquema`)
**Entregable:** Contrato firmado + anticipo cobrado

---

## FASE 4 — INVESTIGACIÓN DE SITIO

- [ ] Visitar el terreno (fotos, video, orientación)
- [ ] Investigar:
  - [ ] **Normativa:** USOS DE SUELO, COS, CUS, restricciones municipales
  - [ ] **Clima:** asoleamiento, rosa de vientos, precipitación anual
  - [ ] **Contexto:** alturas vecinas, materiales, lenguaje urbano
  - [ ] **Infraestructura:** vialidades, drenaje, electricidad
- [ ] Documentar todo en carpeta del proyecto
- [ ] Identificar restricciones críticas (retenciones, límites, caídas de agua)

**Herramientas:** Google Maps, Google Earth, IMNC, reglamento municipal
**Entregable:** Expediente de sitio

---

## FASE 5 — ANÁLISIS

- [ ] Procesar datos de investigación + entrevista:
- [ ] **Análisis de Sitio:** zonificar el terreno (accesos, visuales, ruido)
- [ ] **Análisis del Usuario:** UserEntity, Activity Matrix, 10 Ejes Creativos
- [ ] **Análisis Bioclimático:** carta solar, ventilación natural, zonificación térmica
- [ ] **Análisis Contextual:** lenguaje del lugar, alturas, texturas
- [ ] **Diagrama Espacial SOMA:** crear grafo de relaciones espaciales
  - [ ] Abrir `DiagramaSoma.html`
  - [ ] Agregar nodos con espacios del programa
  - [ ] Conectar aristas según relaciones (contigüidad, circulación, visual)
  - [ ] Exportar PNG del diagrama
- [ ] Redactar **Guía de Diseño** (documento rector del proyecto)
- [ ] Enviar avance al cliente (sin entregar aún)

**Herramientas:** Revit (anotaciones), DiagramaSoma.html, protocolos Bloque 2
**Entregable:** Guía de Diseño + Diagrama Espacial

---

## FASE 6 — CONCEPTUALIZACIÓN

- [ ] Definir **Idea Matriz** (una frase que condensa el concepto)
  - Ej: "La casa como mirador del manglar"
- [ ] Redactar **Mensaje Arquitectónico** (qué historia cuenta el proyecto)
- [ ] Establecer **3-5 Intenciones de Diseño** (ejes conceptuales)
- [ ] **Moldeado Formal:**
  - [ ] Volumetría inicial (sketch 2D o maqueta rápida en Revit)
  - [ ] Proporciones y jerarquías
  - [ ] Piel / materiales potenciales
- [ ] Moodboard de referencias visuales (para Integral y Ejecutivo)
- [ ] Validar intenciones contra Guía de Diseño

**Herramientas:** Sketchbook, Revit (masas), MIRO / Pinterest
**Entregable:** Idea Matriz + Intenciones + Moodboard

---

## FASE 7 — MODELADO 3D

Según nivel contratado:

- [ ] **Esencial (LOD 200):**
  - [ ] Modelo volumétrico básico
  - [ ] Muros, losas, vanos principales
  - [ ] Cubiertas y elementos mayores
- [ ] **Integral (LOD 300):**
  - [ ] Todo lo anterior + carpintería, acabados
  - [ ] Mobiliario fijo, escaleras detalladas
  - [ ] Elementos estructurales visibles
- [ ] **Ejecutivo (LOD 350+):**
  - [ ] Modelo preciso con todos los elementos constructivos
  - [ ] Uniones, juntas, transiciones de material
  - [ ] Coordinación con ingenierías

**Herramientas:** Revit (plantilla SOMA)
**Entregable:** Modelo RVT en LOD correspondiente

---

## FASE 8 — VISUALIZACIÓN

- [ ] **Esencial:** 1 perspectiva general
- [ ] **Integral:** 2-3 perspectivas + moodboard de acabados
- [ ] **Ejecutivo:** 3-5 perspectivas + recorrido virtual (opcional)
- [ ] Flujo: Revit → D5 Render → exportar → Photoshop (post)
- [ ] Aplicar estilo SOMA (iluminación natural, atmósfera habitable, escala humana)
- [ ] Revisar que todas las imágenes tengan:
  - [ ] Alt text descriptivo (para web)
  - [ ] Resolución mínima 1920px lado mayor
  - [ ] Marca de agua SOMA (opcional)

**Herramientas:** D5 Render, Photoshop, `03_PROTOCOLO_VISUALIZACION.md`
**Entregable:** Renders + dossier visual

---

## FASE 9 — EVALUACIÓN DE HABITABILIDAD

- [ ] **Térmica:** orientación, ventilación cruzada, protección solar
- [ ] **Acústica:** aislamiento entre zonas ruidosas y silenciosas
- [ ] **Iluminación:** penetración de luz natural, horas de sol directo
- [ ] **Proxémica:** dimensiones, circulaciones, relación interior-exterior
- [ ] Documentar resultados en ficha de evaluación
- [ ] Si hay problemas → iterar modelo

**Herramientas:** `05_PROTOCOLO_EVALUACION.md`, análisis manual o Climate Consultant
**Entregable:** Ficha de evaluación de habitabilidad

---

## FASE 10 — DOSSIER EDITORIAL

- [ ] Maquetar dossier tipo revista (formato carta / tabloide)
- [ ] Incluir:
  - [ ] Portada con nombre del proyecto
  - [ ] Idea Matriz + Intenciones (1 página)
  - [ ] Plantas, cortes, alzados
  - [ ] Renders y moodboard
  - [ ] Ficha técnica (m², nivel, ubicación)
- [ ] Exportar PDF para presentación al cliente

**Herramientas:** InDesign / Canva / Affinity Publisher
**Entregable:** Dossier PDF

---

## FASE 11 — ANTEPROYECTO

- [ ] Formalizar planos arquitectónicos:
  - [ ] Planta de conjunto (contexto)
  - [ ] Planta(s) arquitectónica(s) con cotas + ejes
  - [ ] Cortes (mín. 2, con alturas y niveles)
  - [ ] Alzados (los 4 frentes)
- [ ] Revisar que planos cumplan normativa local
- [ ] Presentar al cliente (puede ser digital o impreso)
- [ ] Recibir retroalimentación
- [ ] Hacer ajustes (máx. 2 rondas)
- [ ] Obtener aprobación por escrito (WhatsApp basta)
- [ ] Cobrar **segundo pago 40%**
- [ ] Registrar pago en Dashboard

**Herramientas:** Revit (láminas), `06_PROTOCOLO_ANTEPROYECTO.md`
**Entregable:** Planos de anteproyecto aprobados

---

## FASE 12 — PLANOS TÉCNICOS (solo Ejecutivo)

- [ ] Desarrollar planos ejecutivos:
  - [ ] Planta de albañilería (muros, castillos, dalas)
  - [ ] Planta de acabados (pisos, muros, plafones)
  - [ ] Cortes constructivos (escala 1:20 o 1:50)
  - [ ] Detalles constructivos (escala 1:5, 1:10)
  - [ ] Planta de instalaciones (descripción técnica)
- [ ] Coordinar con especialistas:
  - [ ] Ingeniero estructural
  - [ ] Ingeniero hidrosanitario
  - [ ] Ingeniero eléctrico
- [ ] Revisar compatibilidad entre disciplinas
- [ ] Integrar planos de especialistas al paquete final

**Herramientas:** Revit, AutoCAD, `07_PROTOCOLO_PLANOS_TECNICOS.md`, `08_PROTOCOLO_COORDINACION.md`
**Entregable:** Paquete de planos ejecutivos + ingenierías coordinadas

---

## FASE 13 — ENTREGA Y CIERRE

- [ ] Preparar paquete final:
  - [ ] Planos en PDF (alta resolución)
  - [ ] Renders en JPG/PNG
  - [ ] Dossier editorial PDF
  - [ ] Archivo RVT (si aplica)
- [ ] Subir a Google Drive / WeTransfer
- [ ] Enviar link al cliente
- [ ] Confirmar recepción y satisfacción
- [ ] Cobrar **tercer pago 30%**
- [ ] Generar CFDI / recibo de honorarios final
- [ ] Liberar Propiedad Intelectual (planos pasan al cliente)
- [ ] Registrar pago final en Dashboard
- [ ] Pipeline → **pagado**
- [ ] Archivar carpeta del proyecto
- [ ] Preguntar por referidos / testimonio
- [ ] (Opcional) Preparar caso para portafolio público

**Herramientas:** Dashboard, RECIBO_PAGO_PARCIAL.md, Google Drive
**Entregable:** Proyecto completo entregado + proyecto cerrado en sistema

---

## MAPA DE HERRAMIENTAS POR FASE

| Fase | Herramienta principal | Archivos de referencia |
|------|----------------------|----------------------|
| F0 — Recepción | Dashboard, WhatsApp | `server.py`, `Dashboard.html` |
| F1 — Entrevista | App Entrevista (5050) | `PROTOCOLO_02_ENTREVISTA_INMERSION.md` |
| F2 — Programa | Dashboard, calculadora m² | `01_PROTOCOLO_ANALISIS.md` |
| F3 — Comercial | Documentos impresos | `CONTRATO_DISENO_SOMA.md`, `CONVENIO_ANTICIPO_PAGOS.md` |
| F4 — Investigación | Google Earth, reglamento | `PROTOCOLO_INVESTIGACION_PREVIA.md` |
| F5 — Análisis | Revit, DiagramaSoma.html | `01_PROTOCOLO_ANALISIS.md` |
| F6 — Conceptualización | Sketchbook, Revit masas | `01_PROTOCOLO_CONCEPTUALIZACION.md` |
| F7 — Modelado 3D | Revit (plantilla SOMA) | `02_PROTOCOLO_MODELADO.md` |
| F8 — Visualización | D5 Render, Photoshop | `03_PROTOCOLO_VISUALIZACION.md` |
| F9 — Evaluación | Fichas manuales | `05_PROTOCOLO_EVALUACION.md` |
| F10 — Dossier | InDesign / Canva | `04_PROTOCOLO_REPRESENTACION_INTEGRAL.md` |
| F11 — Anteproyecto | Revit láminas | `06_PROTOCOLO_ANTEPROYECTO.md` |
| F12 — Técnicos (Ejec) | Revit + ingenieros | `07_PROTOCOLO_PLANOS_TECNICOS.md`, `08_PROTOCOLO_COORDINACION.md` |
| F13 — Cierre | Dashboard, Drive | `RECIBO_PAGO_PARCIAL.md` |

---

## CHECKLIST RÁPIDO PRE-ENTREGA

Antes de entregar cualquier cosa al cliente, verificar:

- [ ] ¿Los planos tienen norte, escala, y simbología?
- [ ] ¿Las cotas están completas y sin conflictos?
- [ ] ¿Los renders tienen iluminación natural y atmosfera habitable?
- [ ] ¿El dossier cuenta la historia del proyecto?
- [ ] ¿Se respetó el programa arquitectónico acordado?
- [ ] ¿Se verificó contra normativa local?
- [ ] ¿El cliente aprobó la fase anterior por escrito?
- [ ] ¿El pago correspondiente está registrado?

---

*Lo protocolario se programa, lo creativo se libera.*
