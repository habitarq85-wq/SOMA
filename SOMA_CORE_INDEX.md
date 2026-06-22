# SOMA - MATRIZ DE DESARROLLO INTEGRAL

Este documento es el índice maestro para el agente SOMA. Debe actualizarse al final de cada sesión.

## ESTRUCTURA DEL REPOSITORIO

| Carpeta | Contenido |
|---------|-----------|
| `/web` | Sitio oficial (Pagina Web 6.html activa) |
| `/dashboard` | Dashboard de gestión de leads y proyectos |
| `/backend` | Servidor Flask, SQLite, reportes y proyectos de entrevista |
| `/aplicaciones_python` | App de Entrevista y herramientas de programa arquitectónico |
| `/metodologia` | Protocolos de diseño organizados por bloque (incluye RUTA_CLIENTE.md, RUTA_ARQUITECTO.md y RUTA_ADMIN.md en Bloque 3) |
| `/scripts_automatizacion` | Herramientas para pyRevit, Blender y optimización |
| `/recursos_graficos` | Portafolio, plantillas e imágenes de inmersión |
| `/scripts_automatizacion` | Herramientas para pyRevit, Blender y optimización |

## DOCUMENTOS PRINCIPALES (Raíz del proyecto)

| Documento | Propósito | Prioridad si contradice |
|-----------|-----------|------------------------|
| `SOMA_SNAPSHOT.md` | Estado actual del sistema — verdad vigente | Máxima |
| `BITACORA_SOMA.md` | Memoria evolutiva del proyecto | Contexto histórico |
| `SOLOJUAN.md` | Instrucciones literales y reflexiones del fundador | Máxima (en su sección) |
| `SOMA_CORE_INDEX.md` | Índice maestro de desarrollo por bloques | Organizacional |
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROCESO DE DISEÑO` | Checklist formal original (v1). Eje rector del Algoritmo SOMA | Máxima en Bloque 2 |
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/PROCESO DE DISEÑO 2.0` | Versión expandida con INPUT/OPERA/OUTPUT/PROC + referencias bibliográficas + PROTOCOLO cruzados. Clasifica naturaleza y procesador (AI/HUMANO) | Máxima en Bloque 2 |
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/protocolos/` | 11 protocolos renombrados con numeración del 2.0 (ej: `protocolo_4.1-4.10_conceptualizacion.md`). Cubren el "cómo" detallado | Operativa
| `metodologia/Bloque 2 - Taller SOMA (OPERACION)/DIAGNOSTICO_PROCESO_DISEÑO.md` | Análisis crítico del PROCESO DE DISEÑO vs protocolos (05/06/2026) | Organizacional |
| `/biblioteca` | Repositorio central de fuentes (normativas, clima, diseno, arquetipos, repertorio, patrones) que persiste entre proyectos. Primer proyecto descarga, siguientes copian. | Operativa |

## BLOQUE 1: GESTIÓN DEL ENTORNO (ADM) — PRIORIDAD #1
- [x] **Modelo Empresarial:** Carta de presentación con visión, misión, objetivos y valores. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/CARTA_PRESENTACION_SOMA.md`.
- [x] **Organización de Procesos:** Mapeo del flujo lead → proyecto → entrega → cierre. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_ORGANIZACION_PROCESOS.md`.
- [x] **Sistema de Cobros:** Esquema 30/40/30 implementado. Dashboard con botón "Generar 30/40/30". Endpoint `POST /cobros/generar_esquema/<id>`.
- [x] **Registro de Pagos:** Resumen financiero en Dashboard, badges de pago por lead, tabla de cobros en expediente.
- [ ] **Definir Tiempos de Entrega:** Pendiente de definición basada en experiencia de Juan (tamaño + paquete + factores). Estructura base en `TIEMPOS_ENTREGA_BASE.md`.
- [ ] **Automatización de Impuestos:** Cálculo de ISR/IVA, generación de CFDI, reportes fiscales.
- [x] **Protocolo de Presupuesto:** Precios oficiales v3.0 ($250/$350/$850), cargo mínimo $6,500, subsidio cruzado. En `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_PRESUPUESTO_Y_VIABILIDAD.md`.

## BLOQUE 2: TALLER SOMA (OPERACIÓN)
- [x] **Recepción de Información:** Pre-filtro Web (Activo) + App de Entrevista con 6 tópicos. Protocolo alineado al 2.0.
- [x] **Programa Arquitectónico:** Módulo en Dashboard. Endpoints CRUD + cotización formal.
- [x] **Investigación (recolección de datos):** Protocolo en `01 Recepción e Investigación/protocolo_2.1-2.2_investigacion_previa.md`. Cubre levantamiento del sitio, clima, normativa, usuario, contexto. Con fuentes citadas.
- [x] **Análisis:** Protocolo en `02 Análisis/protocolo_3.1-3.10_analisis.md`. Procesa datos de investigación en decisiones de diseño. Cubre: sitio, usuario, bioclimático, contextual, programa, iluminación, acústica, proxémica y síntesis.
- [x] **Conceptualización:** Protocolo en `03 Diseño/protocolo_4.1-4.10_conceptualizacion.md`. Idea Matriz, Mensaje Arquitectónico, Intenciones, Moldeado Formal, Validación.
- [x] **Modelado:** Protocolo en `03 Diseño/protocolo_4.3-5.2_modelado.md`. LOD, organización por capas, ciclos cortos de verificación.
- [x] **Visualización:** Protocolo en `03 Diseño/protocolo_5.3-5.11_visualizacion.md`. Flujo Revit→D5→Photoshop, estilo SOMA sistemático.
- [x] **Representación Integral:** Protocolo en `03 Diseño/protocolo_7.1-7.2_representacion.md`. Dossier editorial HTML con identidad SOMA.
- [x] **Evaluación:** Protocolo en `03 Diseño/protocolo_4.9-4.15_evaluacion.md`. Indicadores térmicos, lumínicos, acústicos, programáticos, proxémicos y normativos con ISO/NOM.
- [x] **Anteproyecto:** Protocolo en `03 Diseño/protocolo_6-8_anteproyecto.md`. Escalas, contenido de láminas, checklist, naming.
- [x] **Planos Técnicos:** Protocolo en `03 Diseño/protocolo_9.3_planos_tecnicos.md`. Detalles constructivos capa por capa, ISO 13567.
- [x] **Coordinación:** Protocolo en `03 Diseño/protocolo_9.1-9.2_coordinacion.md`. Flujo 20/60/100%, resolución de conflictos, bitácora.
- [x] **Diagrama Espacial SOMA:** `DiagramaSoma.html` + vis-network + endpoints Flask.
- [x] **Biblioteca SOMA:** Repositorio central de fuentes creado en `/biblioteca/` con 6 subcarpetas pobladas:
  - `normativas/` — 8 PDFs (reglamento, NTC, NOMs, PMDU, PIMUS, PMD)
  - `clima/` — Carta solar y rosa de vientos generadas + índice climático
  - `diseno/` — Referencia bibliográfica (Neufert, Panero, Ching)
  - `arquetipos/` — Índice con 18 recursos open-access sobre vivienda yucateca
  - `repertorio/` — 15+ proyectos de referencia filtrados por clima/tipo
   - `patrones/` — Catálogo SOMA de 42 patrones + referencia Alexander (34 patrones mapeados)
   - `analisis/` — 6 documentos VIVIENDA: Alexander, Gibson, Panero, Normativas Mérida, NMX Accesibilidad, Catálogo SOMA

## BLOQUE 3: LABORATORIO DE HERRAMIENTAS (I+D)
- [x] **Aplicaciones:** App de Entrevistas (Ejes de Inmersión y ActivityMatrix operativos en Backend). App de Entrevista v2 con 6 tópicos + grabación + post-formulario.
- [x] **Automatización:** Procesamiento con DeepSeek Flash (pendiente de API key). Whisper (pendiente de instalación).
- [x] **Programación:** Backend Flask (Persistencia y Correo reparados, SendGrid API activo, Railway no bloquea HTTPS), Persistencia SQLite. Env vars con `.strip()`. Debug endpoint `/notificaciones/status` (verifica API key).
- [x] **Activity Matrix en Dashboard:** Endpoint `GET /activity_matrix/<temp_id>`, grid 24h interactivo con tooltips y colores SOMA por habitante. Fusión de leads captura_web + proyectos app_inmersion.
- [x] **Pruebas de Sistema:** Revisión Dashboard y Funcionamiento Cotizador (Finalizado).

## BLOQUE 4: MARKETING Y COMUNICACIÓN (MKT)
- [x] **Presencia Digital:** Página Web V2 (`web/Pagina Web 6.html`), Dashboard Editorial, Dashboard de Gestión.
- [x] **Hero Web:** 4 frases rotativas de Carta de Presentación. Video playlist crossfade (2 players, sin pausa). Opacidad final 0.40.
- [x] **Carrusel Vertical (Portafolio):** Transition fix con preloader + cleanup. `decodeURIComponent` en títulos. Nombres de archivo sincronizados con disco.
- [ ] **Material de Publicación:** Portafolio, Tesis de Proyectos.
- [x] **Imágenes de Inmersión:** 20 imágenes propias en 10 carpetas. Mobile: `object-fit: contain` sin recorte.
- [ ] **Estrategias:** Alianzas comerciales, Promoción.

---

## BLOQUE 5: SITIO WEB (MKT) — Sesión 29/05/2026
- [x] **Cotizador: single POST** — Eliminado fetch duplicado en paso 12. Solo `finishImmersion()` al final.
- [x] **Hero mobile vertical:** `padding-top: 15vh`, overlay más oscuro `0.95`.
- [x] **Portfolio mobile:** Proyectos centrados, títulos carrusel en borde inferior.
- [x] **Portfolio landscape:** Modal flex column, imagen flex:1, thumbnails 70px.
- [x] **Carrusel filosofía horizontal:** Forzado con `!important`, flecha `→` hint en mobile, slide "CALIDAD SIN JERARQUÍAS" eliminado.
- [x] **Servicios:** `.services-row` agrupa imagen + lista, contacto debajo.
- [x] **Trayectoria portrait:** Viñeta `::after` en foto, "M. en Arq." en una línea.
- [x] **WhatsApp en contacto:** "999 531 4093" visible.
- [x] **110 imágenes comprimidas:** Pillow quality 80/70, 49→44 MB. Commit `0531ffe`.
- [x] **Video crossfade:** 2 players, sin pausa entre clips. Opacidad final 0.40.
- [x] **Email SendGrid:** Reemplazó SMTP (Railway bloquea puertos SMTP). Timeout cliente 20s.
- [x] **Landscape compact:** Imagen 90px, fuentes 0.45rem, padding reducido. Contacto visible.
- [x] **Immersion images:** `object-fit: contain` en móvil vertical, sin recorte.
- [x] **Desktop contacto:** Centrado, alineado con servicios (`padding-left: 25px`).

## 🧪 BLOQUE 6: SITIO WEB (MKT) — Sesión 02/06/2026
- [x] **Precios v3.0:** Integral $350/m², Ejecutivo $850/m², mínimo taller $6,500.
- [x] **Programa espacios mínimos:** Valores actualizados con factor 1.35 integrado, cochera 30m². `* 1.35` eliminado del JS.
- [x] **Quote-type tabs:** `<select>` reemplazado por 3 tabs visibles. Activo en acento, inactivos translúcidos.
- [x] **Botón volver unificado:** Todos los pasos del cotizador con `← volver` estilo transparente + borde #333.
- [x] **Scroll reveal bidireccional:** `classList.toggle()` en proyectos y filosofía. Efecto agregado a filosofía (opacity + translateX).
- [x] **Fixes alta prioridad (11/11):** type duplicado, overflow sections, contraste (#bc4b21→#d45e2c, #555→#999, #666→#aaa), alt en 31 imágenes, `<noscript>`, -webkit-backdrop-filter, :focus-visible, scroll-snap-type y proximity. Threshold 0.65.
- [x] **Video Hero Optimizado:** Fusión de 4 clips MP4 en `hero_loop.mp4` único de 29s con crossfades. 5.6MB (72% más ligero). Lógica JS compleja de players reemplazada por `<video loop>` nativo.
- [x] **Rutas Operativas SOMA:** Creados `RUTA_CLIENTE.md`, `RUTA_ARQUITECTO.md` y `RUTA_ADMIN.md` para cubrir todo el modelo de negocio y diseño.
- [x] **Algoritmo SOMA (Base):** Creado `FUSION_CONCEPTUALIZACION.md` integrando el protocolo teórico con la práctica de 17 pasos.
- [x] **Algoritmo SOMA (Visual):** HTML interactivo (`web/algoritmo_soma.html`) + diagrama SVG (`recursos_graficos/algoritmo_soma_diagrama.svg`). 16 pasos visualizados en 4 fases con interacción expandible.

## 🧪 BLOQUE 7: SITIO WEB (MKT) — Sesión 17/06/2026
- [x] **Flujo cotizador:** Paso 12 eliminado. Contacto → directo a Escala e Inversión.
- [x] **Textos paquetes:** Lenguaje claro para público general. Detalles técnicos en letras chiquitas.
- [x] **Recámaras separadas:** Principal (16m²) y Secundaria (12m²) como checkboxes.
- [x] **Otros dinámico:** Filas con nombre + m² + botón +/×. Sin cantidad.
- [x] **Padding btn-back:** Corregido para no montarse en imágenes.

## 🎯 PRIORIDADES 29/05/2026 — ROADMAP A PRODUCCIÓN

| Prioridad | Acción | Por qué |
|-----------|--------|---------|
| 🔥 Crítica | **Cerrar 1 cliente real** | Probar el ciclo completo valida o rompe supuestos |
| 🔥 Crítica | **Conseguir RFC en RESICO** | Sin factura no hay cobro formal |
| ✅ Hecha | **Dominio propio** | `soma-arquitectura.com` registrado + Cloudflare |
| ✅ Hecha | **Autenticar dominio en SendGrid** | SPF/DKIM configurado. Correos desde `info@...` |
| ✅ Hecha | **Migrar a PostgreSQL** | SQLite → PostgreSQL vía Render. `db.py` maneja ambos backends |
| Media | **faster-whisper + DeepSeek** | Automatización real del análisis |
| Media | **Optimizar web: CDN o Cloudflare** | Velocidad de carga en celular |
| ✅ Hecha | **Migrar a Render** | Railway → Render con PostgreSQL gratis. `render.yaml` |
| Alta | **Dashboard con login** | Proteger `/dashboard` con contraseña |
