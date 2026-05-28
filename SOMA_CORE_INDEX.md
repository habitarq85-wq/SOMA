# SOMA - MATRIZ DE DESARROLLO INTEGRAL

Este documento es el índice maestro para el agente SOMA. Debe actualizarse al final de cada sesión.

## ESTRUCTURA DEL REPOSITORIO

| Carpeta | Contenido |
|---------|-----------|
| `/web` | Sitio oficial (Pagina Web 6.html activa) |
| `/dashboard` | Dashboard de gestión de leads y proyectos |
| `/backend` | Servidor Flask, SQLite, reportes y proyectos de entrevista |
| `/aplicaciones_python` | App de Entrevista y herramientas de programa arquitectónico |
| `/metodologia` | Protocolos de diseño organizados por bloque |
| `/recursos_graficos` | Portafolio, plantillas e imágenes de inmersión |
| `/scripts_automatizacion` | Herramientas para pyRevit, Blender y optimización |

## DOCUMENTOS PRINCIPALES (Raíz del proyecto)

| Documento | Propósito | Prioridad si contradice |
|-----------|-----------|------------------------|
| `SOMA_SNAPSHOT.md` | Estado actual del sistema — verdad vigente | Máxima |
| `BITACORA_SOMA.md` | Memoria evolutiva del proyecto | Contexto histórico |
| `SOLOJUAN.md` | Instrucciones literales y reflexiones del fundador | Máxima (en su sección) |
| `SOMA_CORE_INDEX.md` | Índice maestro de desarrollo por bloques | Organizacional |

## BLOQUE 1: GESTIÓN DEL ENTORNO (ADM) — PRIORIDAD #1
- [x] **Modelo Empresarial:** Carta de presentación con visión, misión, objetivos y valores. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/CARTA_PRESENTACION_SOMA.md`.
- [x] **Organización de Procesos:** Mapeo del flujo lead → proyecto → entrega → cierre. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_ORGANIZACION_PROCESOS.md`.
- [x] **Sistema de Cobros:** Esquema 30/40/30 implementado. Dashboard con botón "Generar 30/40/30". Endpoint `POST /cobros/generar_esquema/<id>`.
- [x] **Registro de Pagos:** Resumen financiero en Dashboard, badges de pago por lead, tabla de cobros en expediente.
- [ ] **Definir Tiempos de Entrega:** Pendiente de definición basada en experiencia de Juan (tamaño + paquete + factores). Estructura base en `TIEMPOS_ENTREGA_BASE.md`.
- [ ] **Automatización de Impuestos:** Cálculo de ISR/IVA, generación de CFDI, reportes fiscales.
- [x] **Protocolo de Presupuesto:** Precios oficiales, cargo mínimo, subsidio cruzado. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_PRESUPUESTO_Y_VIABILIDAD.md`.

## BLOQUE 2: TALLER SOMA (OPERACIÓN)
- [x] **Recepción de Información:** Pre-filtro Web (Activo) + App de Entrevista con 6 tópicos.
- [x] **Programa Arquitectónico:** Módulo en Dashboard para capturar Deseado + Complementario + Lujo. Endpoints CRUD + cotización formal.
- [x] **Investigación (recolección de datos):** Protocolo en `01 Recepción e Investigación/PROTOCOLO_INVESTIGACION_PREVIA.md`. Solo dice qué investigar, dónde obtenerlo y cómo registrarlo. Cubre: levantamiento del sitio, infraestructura, contexto urbano, parámetros de accesibilidad, historia del lugar, datos climáticos de Mérida (ya disponibles), normativa, perfil del usuario, contexto social, viabilidad y riesgos. Con fuentes citadas.
- [x] **Análisis:** Protocolo en `02 Análisis/01_PROTOCOLO_ANALISIS.md` + formato de salida en `02 Análisis/EJEMPLO_GUIA_DISENO.md`. Procesa datos de investigación en decisiones de diseño. Cubre: sitio (bounding box, conflictos, macrozonificación), usuario (UserEntity, 10 ejes → partido arquitectónico, CreativeCore), bioclimático (carta solar, ventilación, selección de estrategias pasivas, zonificación térmica, ciclo diario de aperturas, extracción de malos olores), contextual (tipología, visuales, accesos), programa (zonificación SOMA, matriz de relaciones, Diagrama Espacial, eficiencia), complementarios (iluminación con % óptimo por espacio, acústica, proxémica, ciclo de vida) y síntesis (entrada a Conceptualización).
- [x] **Conceptualización:** Protocolo en `03 Diseño/PROTOCOLO_CONCEPTUALIZACION.md`. Traduce la síntesis del análisis en: Idea Matriz, Mensaje Arquitectónico, Intenciones de Diseño (espaciales, tectónicas, bioclimáticas), Moldeado Formal (diagrama de masas, operaciones, zonificación SOMA en volumen, recorridos, 3 opciones volumétricas) y Validación del Concepto. Salida → entrada a Modelado.
- [x] **Diagrama Espacial SOMA:** Migrado de Tkinter a web (`DiagramaSoma.html` + vis-network + endpoints Flask). Filtro por zona, arrastre de nodos, export PNG/SVG.
- [x] **Modelado:** Protocolo en `03 Diseño/PROTOCOLO_MODELADO.md`. Traduce el concepto a modelo 3D. Cubre: construcción del volumen base, LOD según paquete (200/300/350+), organización por capas y colores SOMA, modelado por sistemas (estructura, arquitectura, circulaciones, instalaciones), verificación vs programa/constraints, checklist y pruebas visuales mínimas. Salida → Visualización y Planos.
- [x] **Visualización:** Protocolo de Arte y Perspectivas. Planeado (9 secciones: vistas obligatorias, estilo SOMA, flujo Revit→D5→Photoshop, setup de cámaras, catálogo de materiales, postproducción, checklist, archivo). Pendiente de implementar en `03 Diseño/PROTOCOLO_VISUALIZACION.md`.
- [x] **Representación Integral:** Protocolo de Presentación. Planeado (dossier editorial en HTML con efectos scroll-reveal, template parametrizable, exportación a PDF). Pendiente de implementar en `03 Diseño/dossier/plantilla_dossier.html`.
- [x] **Evaluación:** Indicadores de Habitabilidad y Rendimiento. Planeado (auditoría de indicadores térmicos, acústicos, iluminación, programa, proxémica y normativos; tabla de resultados ✅/⚠️/❌ con ajustes). Pendiente de implementar en `03 Diseño/PROTOCOLO_EVALUACION.md`.
- [ ] **Anteproyecto:** Definición de Elementos.
- [ ] **Planos Técnicos:** Protocolo de Fabricación.
- [ ] **Coordinación:** Gestión de Ingenierías.

## BLOQUE 3: LABORATORIO DE HERRAMIENTAS (I+D)
- [x] **Aplicaciones:** App de Entrevistas (Ejes de Inmersión y ActivityMatrix operativos en Backend). App de Entrevista v2 con 6 tópicos + grabación + post-formulario.
- [x] **Automatización:** Procesamiento con DeepSeek Flash (pendiente de API key). Whisper (pendiente de instalación).
- [x] **Programación:** Backend Flask (Persistencia y Correo reparados, SMTP SSL puerto 465, Twilio funcional), Persistencia SQLite. Env vars con `.strip()`. Debug endpoint `/notificaciones/status` con error real.
- [x] **Activity Matrix en Dashboard:** Endpoint `GET /activity_matrix/<temp_id>`, grid 24h interactivo con tooltips y colores SOMA por habitante. Fusión de leads captura_web + proyectos app_inmersion.
- [x] **Pruebas de Sistema:** Revisión Dashboard y Funcionamiento Cotizador (Finalizado).

## BLOQUE 4: MARKETING Y COMUNICACIÓN (MKT)
- [x] **Presencia Digital:** Página Web V2 (`web/Pagina Web 6.html`), Dashboard Editorial, Dashboard de Gestión.
- [x] **Hero Web:** 4 frases rotativas de Carta de Presentación. Video playlist rotativa sin loop.
- [x] **Carrusel Vertical (Portafolio):** Transition fix con preloader + cleanup. `decodeURIComponent` en títulos. Nombres de archivo sincronizados con disco.
- [ ] **Material de Publicación:** Portafolio, Tesis de Proyectos.
- [x] **Imágenes de Inmersión:** 40 imágenes placeholder en `recursos_graficos/Inmersion/` (2 por opción). HTML actualizado con rutas locales. Pendiente reemplazo por imágenes propias del usuario.
- [ ] **Estrategias:** Alianzas comerciales, Promoción.

---

## 🎯 PRIORIDADES 28/05/2026 — ROADMAP A PRODUCCIÓN

| Prioridad | Acción | Por qué |
|-----------|--------|---------|
| 🔥 Crítica | **Cerrar 1 cliente real** | Probar el ciclo completo valida o rompe supuestos |
| 🔥 Crítica | **Conseguir RFC en RESICO** | Sin factura no hay cobro formal |
| 🔥 Crítica | **Revocar credenciales viejas + Railway env vars** | SMTP y Twilio expuestos en git history |
| Alta | **Verificar SMTP en Railway (puerto 465)** | Último push migró a SSL, falta confirmar conexión |
| Alta | **Dominio propio** | `soma.up.railway.app` no inspira confianza |
| Media | **Migrar a PostgreSQL** | SQLite en Railway se pierde al reiniciar |
| Media | **faster-whisper + DeepSeek** | Automatización real del análisis |
| Media | **Optimizar web: CDN o Cloudflare** | Velocidad de carga en celular |
