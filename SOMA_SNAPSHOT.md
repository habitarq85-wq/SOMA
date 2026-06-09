# ⚡ SOMA SNAPSHOT - ESTADO ACTUAL DEL SISTEMA
*Este documento representa la VERDAD VIGENTE del proyecto. Cualquier contradicción con otros archivos se resuelve a favor de este SNAPSHOT.*

---

## 🏛️ 1. REGLAS DE ORO (Inmutables)
- **Tesis:** "Lo protocolario se programa, lo creativo se libera."
- **Paradigma:** Taller de Diseño con tecnología como exoesqueleto (AaaP + Ingeniería del Habitar).
- **Enfoque:** Democratización del diseño mediante la automatización técnica de alta calidad. **Subsidio cruzado:** el nivel Ejecutivo financia la inclusividad del nivel Esencial.
- **Calidad innegociable:** todos los niveles reciben la misma calidad de diseño. Lo que varía es la profundidad de la información técnica y el alcance de los entregables.
- **Herramientas open source** para reducir costos operativos sin comprometer la calidad.

---

## 🏗️ 2. BLOQUES DE DESARROLLO (Pilares del Proyecto)
### BLOQUE 1: GESTIÓN DEL ENTORNO (ADM)
- Administración, costos, fiscal, organización de archivos y protocolos de negocio.
### BLOQUE 2: TALLER SOMA (OPERACIÓN)
- El proceso de diseño de 10 etapas (Recepción -> ... -> Coordinación). Es el corazón operativo.
### BLOQUE 3: LABORATORIO DE HERRAMIENTAS (I+D)
- Software, scripts (Python/pyRevit), automatización, conexión Web -> DB.
### BLOQUE 4: MARKETING Y COMUNICACIÓN (MKT)
- Página web, redes sociales, renders de autor, dossier editorial y tesis de proyectos.

---

## 🧠 3. DEFINICIONES DE DATOS ACTUALES (Cerebro SOMA)
*Configuración vigente de la estructura de información.*

### A. UserEntity (Entidad Habitante)
- **Atributos Estáticos:** Ergonomía, medidas de espacio personal.
- **Atributos Dinámicos:** Hobbies, roles de poder en el núcleo social.
- **ActivityMatrix:** Generación obligatoria de **24 slots temporales** por habitante (determina necesidades de aislamiento e iluminación).

### B. Zonificación Maestra SOMA
1. **Social** — Interacción / Público
2. **Descanso** — Introspección / Privado
3. **Operativa** — Producción / Trabajo
4. **Soporte** — Logística / Servicios
5. **Transición** — Conectividad / Cinemática

### C. Inmersión Visual (Ejes de Diseño)
1. **Fachada:** Abierta / Cerrada
2. **Privacidad:** Abierta (visibilidad total) / Recibidor (gradación de intimidad)
3. **Planta:** Abierta / Fraccionada
4. **Iluminación:** Directa / Tenue
5. **Tacto:** Textura / Liso
6. **Niveles:** Uno / Varios
7. **Paisaje:** Verde / Pétreo
8. **Escala:** Acogedor / Amplio
9. **Perfil Social:** Activo / Privado
10. **Color:** Neutral / Carácter

---

## 🛠️ 3. INFRAESTRUCTURA TÉCNICA (Backend)

### Servidor Web + Dashboard + Notificaciones (puerto 8080)
- **Archivo:** `backend/server.py` (Flask)
- **Endpoints:** `/save_immersion`, `/get_leads`, `/leads/kanban`, `/lead/<id>/pipeline`, `/activity_matrix/<temp_id>`, `/programa/<lead_id>`, `/programa/espacio` (POST/PUT/DELETE), `/cotizacion/<lead_id>`, `/cotizacion/<lead_id>/pdf`, `/cobros/<proyecto_id>`, `/cobros` (POST), `/cobros/<id>/pagar`, `/resumen_financiero`, `/` (Dashboard HTML), `/css/<path>` (CSS estático)
- **SMTP:** Gmail configurado vía SSL (puerto 465, variable `SMTP_USE_SSL=true`). Reportes a habitarq85@gmail.com. ⚠️ Railway bloquea outbound en puerto 587, se migró a 465. Envío **síncrono** (sin threads) porque Railway elimina hilos en segundo plano. Timeout SMTP 10s.
- **WhatsApp:** Twilio Sandbox. Notificaciones al +5219993619433.
- **Persistencia:** SQLite con tablas: `captura_web`, `matriz_inversion`, `cobros`, `config_fiscal`, `programa_arquitectonico`, `proyectos`, `habitantes`, `actividades`, `ejes_diseno`, `espacios`, `proyecto_datos`.
- **Diagnósticos:** `diagnosticos_master.json` (10 pasos de inmersión).
- **Reportes:** `backend/reportes/reporte_*.txt`

### App de Entrevista (puerto 5050)
- **Archivo:** `aplicaciones_python/app_inmersion/app.py` (Flask independiente)
- **Endpoints:** `/` (app), `/crear_proyecto`, `/guardar_entrevista`, `/guardar_datos_entrevista`, `/procesar_entrevista`, `/proyectos`, `/proyectos/{id}/guia`, `/proyectos/{id}/audio`, `/proyectos/{id}/datos`
- **Template:** `templates/entrevista.html` — 6 tópicos conversacionales + grabación continua + formulario post-entrevista
- **Procesamiento IA:** Whisper + DeepSeek Flash API — pendiente de instalar/configurar
- **Estructura de proyectos:** `backend/proyectos/SOMA-XXXX/` con `info.json`, `entrevista.wav`, `transcripcion.txt`, `guia_de_diseno.md`, `datos_estructurados.json`

### Dashboard (`http://localhost:8080/`)
- **Archivo:** `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/Dashboard.html` (servido desde Flask)
- **Vista lista:** leads con indicadores financieros, barras de polaridad (10 ejes), filtros por nombre/nivel, modal expediente con cobros
- **Vista Kanban:** toggle Lista/Kanban, 6 columnas (Lead → Entrevistado → Programado → Cotizado → Contratado → Pagado), flechas ◀ ▶ para mover leads
- **Programa Arquitectónico:** modal con tabs Deseado/Complementario/Lujo, inputs (espacio, m2, zona, clave núm.), tabla con botón 🔗 para relaciones, totales parciales
- **Cotización Formal:** dentro del modal de programa, pestaña Cotización, botón 📄 PDF que abre HTML imprimible (sin precios internos ni obra)
- **Cobros:** bloque financiero, registro de pagos en expediente, badges en lead cards
- **Activity Matrix:** botón MATRIZ en cada lead, grid 24h por habitante con tooltips
- Auto-refresh cada 30 segundos

---

## 🌐 4. PÁGINA WEB (Bloque 4: MKT)
- **Archivo:** `web/Pagina Web 6.html` (versión activa)
- **Hero:** Video de fondo con playlist rotativa de 4 videos (mangle, Telchac, atardecer, nocturna). `onloadeddata` para play seguro, sin `loop` para que la playlist avance. 4 frases de la carta de presentación con fade in/out a la derecha del título.
- **Portafolio:** Carrusel horizontal con 5 proyectos reales. Modal con galería dinámica por proyecto, miniaturas con proporción nativa, títulos por nombre de archivo. Preloader de imágenes para evitar transiciones trabadas.
- **Inmersión SOMA (10 pasos):** Preguntas visuales A/B sobre fachada, habitaciones, espacios, iluminación, estilo, niveles, paisaje, sensación, vida social y color.
- **Cotizador:** 3 modalidades (Por Programa, Por m², Por Inversión). 3 niveles de paquete: Esencial ($250/m²), Integral ($350/m²), Ejecutivo ($850/m²). Cargo mínimo operativo de $6,500.
- **Diagnóstico técnico:** Al elegir paquete se muestran los análisis del `diagnosticos_master.json`. Excluido de la interfaz web (solo correo/WhatsApp).
- **Notificaciones:** Los leads activan: (1) guardado en DB, (2) reporte en `backend/reportes/`, (3) correo SMTP (puerto 465 SSL) a habitarq85@gmail.com, (4) WhatsApp Twilio a Juan. Integración con App de Entrevista vía carpeta `backend/proyectos/` compartida.

## 💰 5. ESCALA DE PRECIOS OFICIAL (SOMA v3.0)
| Paquete | Precio | Entregables |
|---|---|---|
| **SOMA Esencial** | $250/m² | Diseño arquitectónico, plantas, alzados, análisis de sitio y normativa, perspectiva de proyecto. |
| **SOMA Integral** | $350/m² | Básico + moodboard de acabados, criterios de ingenierías, planos de permiso y más perspectivas. |
| **SOMA Ejecutivo** | $850/m² | Integral + planos técnicos, detalles constructivos, coordinación de ingenierías. |

- **Cargo mínimo operativo:** $6,500 MXN (se aplica silenciosamente para proteger la viabilidad de proyectos pequeños).
- **Rangos de obra (terceros):** Esencial $14,000-$16,500/m², Integral $18,500-$23,000/m², Ejecutivo $28,000-$40,000/m².

## 🚀 6. OBJETIVOS INMEDIATOS (Prioridades 19/05/2026 — Noche)

### PRIORIDAD 0 — BACKUP DE BASE DE DATOS ✅ (Completado)
- [x] **Backup automático:** script `backend/backup_db.sh` que respalda `proyectos_arquitectonicos.db` con timestamp. Primer backup ejecutado.

### PRIORIDAD 1 — BLOQUE ADMINISTRATIVO ✅ (Completado)
- [x] **Esquema de pagos 30/40/30:** Estrategia agresiva de confianza. Anticipo 30%, segundo 40%, tercero 30%. Botón "Generar 30/40/30" en Dashboard. Endpoint `POST /cobros/generar_esquema/<id>`. Contrato actualizado.
- [x] Sistema de cobros (tabla `cobros` + endpoints + UI en Dashboard)
- [x] Programa arquitectónico (tabla `programa_arquitectonico` + CRUD + UI con 3 niveles)
- [x] Cotización formal (endpoint cálculo + PDF imprimible sin precios internos)
- [x] Kanban pipeline (vista toggle, 6 estados, persistencia en DB)
- [x] Clave E{número} y relaciones diferidas (como en Arquiprograma.py original)
- [x] **Diagrama Espacial SOMA:** Migrado de Tkinter a web (`DiagramaSoma.html` + endpoints Flask). Grafo interactivo con vis-network, arrastre de nodos, filtro por zona, export PNG/SVG.

### PRIORIDAD 2 — PÁGINA WEB ✅ (Completado)
- [x] Hero quotes rotativas
- [x] Bug carrusel vertical (preloader + cleanup)
- [x] Video playlist crossfade (2 players, sin pausa entre clips)
- [x] Video opacity (0.40 final)
- [x] Landscape responsive (compactación: imagen 90px, fuentes 0.45rem)
- [x] Desktop contacto centrado y alineado con servicios
- [x] Immersion imágenes sin crop en móvil vertical
- [x] Cotizador: email síncrono, toast feedback, timeout 20s
- [x] `web/Pagina Web 6.html` creada con todas las correcciones

### PRIORIDAD 3 — MARKETING (Después de P1 + P2)
Estrategias para redes sociales, Google y otras fuentes de leads. Solo cuando el embudo completo funcione: lead → cotización → pago → factura.

### BACKLOG TÉCNICO (Pausado — no bloquea ventas)
- [ ] Instalar `faster-whisper` para transcripción local de entrevistas.
- [ ] Configurar `DEEPSEEK_API_KEY` para análisis automático.
- [ ] App de Entrevista: pruebas de audio en dispositivo móvil.
- [ ] Registro RFC de Juan en RESICO para emitir CFDI.

### ⚠️ RIESGO CRÍTICO ✅ (Resuelto)
- [x] **Backup automatizado de la DB.** Script `backend/backup_db.sh` + carpeta `backend/backups/` con timestamp. Limpieza automática de backups >30 días.

---

## 📅 ÚLTIMA ACTUALIZACIÓN: 02/06/2026 (PRECIOS V3.0 + QUOTE TABS + SCROLL REVEAL + FIXES)
- **Programa Arquitectónico en Dashboard:** Tabla `programa_arquitectonico` + CRUD endpoints + UI con 3 niveles (Deseado/Complementario/Lujo), clave E{número}, relaciones por 🔗 en mini-modal movible.
- **Cotización Formal PDF:** Endpoint `/cotizacion/<id>/pdf` con HTML imprimible. **NO muestra** precio/m², mínimo $8,000 ni obra (datos internos del taller).
- **Cobros y Finanzas:** Tabla `cobros` + `resumen_financiero` + registro de pagos en modal expediente + badges en lead cards.
- **Kanban Pipeline:** Vista toggle Lista/Kanban, 6 columnas con persistencia en DB, flechas ◀ ▶ para mover leads.
- **Dashboard servido desde Flask** (`http://localhost:8080/`) para evitar CORS.
- **Nuevas tablas DB:** `cobros`, `config_fiscal`, `programa_arquitectonico`.
- **[NUEVO] Backup automático:** `backend/backup_db.sh` con timestamp + limpieza >30 días. Primer backup ejecutado.
- **[NUEVO] Diagrama Espacial SOMA:** `DiagramaSoma.html` (web) con vis-network, arrastre, filtro zona, export PNG/SVG. Endpoints `/diagrama`, `/api/diagrama/proyectos`, `/api/diagrama/grafo/<id>`.
- **[NUEVO] Esquema de pagos 30/40/30:** Estrategia agresiva para ganar confianza. Anticipo 30%, segundo pago 40% (entrega anteproyecto), tercer pago 30% (entrega final). Contrato actualizado. Dashboard con botón "Generar 30/40/30" que auto-crea los 3 cobros. Endpoint `POST /cobros/generar_esquema/<id>`.
- **[NUEVO] Cotización PDF mejorada:** Tabla de esquema de pagos 30/40/30 + nota de vigencia de 30 días + aclaratoria de diseño vs obra.
- **[NUEVO] Activity Matrix con fallback SQLite:** Endpoint ahora consulta BD cuando no hay JSON. Scroll automático al presionar MATRIZ.
- **[NUEVO] Carta de Presentación SOMA:** Modelo empresarial completado. Documento MD + HTML editorial en `/carta-presentacion`. Visión, misión, objetivos, valores definidos.
- **[NUEVO] Pagina Web 6.html:** Hero con 4 frases rotativas + bugfix carrusel vertical (preloader + cleanup) + video playlist sin loop + projectAssets sincronizados con disco.
- **[NUEVO] Organización de Procesos:** Mapeo formal lead → proyecto → entrega → cierre documentado en `metodologia/Bloque 1 - Gestion del Entorno (ADM)/PROTOCOLO_ORGANIZACION_PROCESOS.md`. Incluye 7 fases detalladas, mapa de transición de estados, reglas de negocio, responsabilidades, indicadores de gestión y flujo de archivado.
- **[NUEVO] Trayectoria rediseñada en web:** De 3 items genéricos a línea de tiempo vertical con 5 nodos (UADY, UNAM, CDMX, DAA, SOMA), cada uno con concepto de aprendizaje. Incluye espacio para retrato.
- **[NUEVO] Email actualizado:** `taller@virtual.lab` eliminado → `habitarq85@gmail.com` en sección Contacto.
- **Corrección de flujo:** Investigación y Análisis movidos **después** del contrato en el mapa de procesos.
- **[2026-05-22] Dashboard movido a Bloque 1:** De `dashboard/` (raíz) a `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/`. Cada bloque ahora autocontenido con sus herramientas. Archivo servido desde nueva ruta en `server.py:654-668`. DB se mantiene en `backend/` (Bloque 3).
- **[2026-05-25] Retrato en Trayectoria:** Reemplazado placeholder por `recursos_graficos/Foto trayectoria/retrato final.png`. Recorte 20% superior.
- **[2026-05-25] Video Filosófico eliminado:** Sección Filosofía ya no tiene placeholder de video.
- **[2026-05-25] Carrusel Filosofía:** Slides agrandados (400px), centrados, velocidad reducida.
- **[2026-05-25] Frase portada:** Cambiada a "Que la buena arquitectura no sea la excepción, sino el punto de partida."
- **[2026-05-25] Texto Filosofía:** Reformulado tono menos agresivo.
- **[2026-05-25] Fix botón Finalizar:** Timeout 3s + AbortController en fetch para evitar que se trabe.
- Pendiente: automatización de impuestos/CFDI, faster-whisper, DeepSeek, pruebas en móvil, RFC, definir tiempos de entrega en `TIEMPOS_ENTREGA_BASE.md`, actualizar contrato y PROTOCOLO_ORGANIZACION_PROCESOS.
- **[NUEVO 2026-05-26] Definir tiempos de entrega realistas:** Los 6-8 semanas actuales del contrato eran placeholder sin justificación. Pendiente definir tabla basada en: tamaño de proyecto, paquete, iteraciones, permisos, ingenieros. Estructura base en `TIEMPOS_ENTREGA_BASE.md`.
- **[NUEVO 2026-05-26] Fuentes en todos los protocolos de Bloque 2:** Se agregó sección FUENTES a los 10 protocolos.
- **[NUEVO 2026-05-26] Expansión masiva de referencias canónicas:** Se incorporaron 43 fuentes al sistema. Archivadas en `REFERENCIAS_CANONICAS.md`.
- **[NUEVO 2026-05-26] Fondo Democratización:** Endpoint `/fondo_democratizacion` en server.py. Dashboard ahora obtiene el fondo vía API en lugar de fórmula client-side. Criterio actualizado: Ejecutivo $200/m², Integral $100/m².
- **[NUEVO 2026-05-26] Notificaciones verificables:** Endpoint `/notificaciones/status` que prueba conexión SMTP y Twilio. Dashboard muestra estado dinámico en lugar de texto estático. Ambos OK.
- **[NUEVO 2026-05-26] Protocolos numerados:** Todos los protocolos de Bloque 2 renombrados con prefijo numérico secuencial (01-08 en Diseño, 01 en Análisis). Referencias cruzadas actualizadas.
- **[NUEVO 2026-05-26] Casona Cristi:** 4 fotos nuevas agregadas a la galería web (Cocina, Comedor, Escalera, Patio).
- **[2026-05-27] Preparación para Railway:** `requirements.txt`, `Procfile`, `railway.json` creados. `server.py` actualizado: raíz `\` sirve `Pagina Web 6.html`, Dashboard en `/dashboard`, nuevas rutas `/recursos_graficos/` y `/backend/` para assets estáticos. URLs de frontend cambiadas a rutas relativas. Puerto usa `$PORT` de Railway.
- **[2026-05-28] Landscape responsive:** Nueva media query `max-height: 520px` para celular horizontal. Hero (1ra sección) mantiene 100vh, secciones siguientes auto-height. Slide titles más pequeños, imágenes carrusel con `object-fit: contain`.
- **[2026-05-28] SMTP Railway fix:** Puerto cambiado de 587 (bloqueado por Railway) a 465 SSL. Nueva variable `SMTP_USE_SSL=true` (default). `.strip()` agregado a todas las env vars.
- **[2026-05-28] Env vars:** `.strip()` en SMTP_USER, SMTP_PASSWORD, TWILIO_SID, TWILIO_TOKEN, NOTIFICACION_WHATSAPP para evitar trailing spaces en Railway.
- **[2026-05-28] Debug SMTP:** Endpoint `/notificaciones/status` ahora devuelve `error` y `trace` con el mensaje de error real.
- **[2026-05-28] Cotizador single POST:** Eliminado fetch duplicado en `registerContact()`. Ambos pasos (12 y 15) llaman a `finishImmersion()` como único punto de guardado.
- **[2026-05-28] Hero vertical mobile:** `padding-top: 15vh`, overlay `rgba(10,10,10,0.95)`. Proyectos centrados con `justify-content: center`.
- **[2026-05-28] Portfolio responsive:** Landscape modal flex column, imagen flex:1, thumbnails 70px. Títulos carrusel en borde inferior mobile/landscape.
- **[2026-05-28] Filosofía carrusel:** Slide "CALIDAD SIN JERARQUÍAS" eliminado. Flecha `→` pulse en mobile. Forzado horizontal con `!important`.
- **[2026-05-28] Servicios reestructurados:** `.services-row` agrupa imagen + lista, contacto debajo. Grid desktop `1fr 260px`, mobile `1fr auto`.
- **[2026-05-28] Trayectoria portrait:** Viñeta `::after { box-shadow: inset 0 0 30px 15px rgba(10,10,10,0.7) }`. "M. en Arq." en una línea.
- **[2026-05-28] WhatsApp:** "WhatsApp: 999 361 9433" agregado en sección Contacto.
- **[2026-05-28] Imágenes comprimidas:** 110 imágenes con Pillow (quality 80 JPG, 70 WebP). 49→44 MB. Commit `0531ffe`.
- **[BUG] Botón cotizador no visible en landscape mobile** — resuelto: compactación máxima (imagen 90px, fuentes 0.45rem, padding reducido). Pendiente verificar en vivo.
- **[BUG] Página se traba en "Enviar"** — resuelto: email revertido a síncrono + timeout 5s en fetch. Pendiente ajustar si Railway persiste.
- **[2026-05-29] Video crossfade:** Dos elementos `<video>` en vez de uno. Mientras el visible se reproduce, el oculto precarga el siguiente. Transición `opacity 0.8s ease`. Elimina el salto/pausa entre clips.
- **[2026-05-29] Video opacity:** Ajustada progresivamente: 0.4 → 0.5 → 0.45 → 0.40 (filtro más oscuro, decisión del usuario).
- **[2026-05-29] Email síncrono (Railway):** Revertido de `threading` a síncrono. Railway eliminaba los hilos antes de completar el envío. Toast ahora responde según estado del servidor (éxito, email falló, error conexión).
- **[2026-05-29] Cotizador timeout:** fetch timeout 8s → 5s (ahora 20s tras prueba).
- **[2026-05-29] Desktop contacto:** `section:last-of-type` ahora `justify-content: center; padding: 0 10%` (mismo que otras secciones). Título hereda h2 global. Textos alineados con lista de servicios via `padding-left: 25px`.
- **[2026-05-29] Landscape responsive (compactación final):** Contacto invisible por falta de espacio. Se redujo: imagen servicios 120→90px, fuentes a 0.45rem, gaps a 4px, padding sección `1vh 4% 3vh`. Timeline más compacto. Botón `padding: 4px 10px`.
- **[2026-05-29] Immersion images crop fix:** En móvil vertical, `object-fit: cover` + `aspect-ratio: 3/4` recortaban las imágenes. Cambiado a `object-fit: contain; height: auto; max-height: 200px` en 480px (1 columna) y 180px en 768px (2 columnas).
- **[2026-05-29] Email timeout fix:** Timeout cliente 5s → 20s (SMTP síncrono tardaba más de 5s). Timeout SMTP añadido (10s) para no colgarse.

**[NUEVO 2026-06-02] Programa espacios mínimos + cotizador:** Valores de programa actualizados a dimensiones mínimas funcionales + factor 1.35 integrado. Cochera 2 autos (30m²). `* 1.35` eliminado del JS.
- **[NUEVO 2026-06-02] Precios actualizados (v3.0):** Integral $400 → $350/m². Ejecutivo $1,000 → $850/m². Mínimo taller $8,000 → $6,500.
- **[NUEVO 2026-06-02] Quote-type selector:** Reemplazado `<select>` por 3 tabs visibles con activo resaltado en acento. Botones "← volver" unificados en todos los pasos del cotizador (transparente + borde #333 + flecha).
- **[NUEVO 2026-06-02] Scroll reveal bidireccional:** `classList.toggle()` en vez de `add()`. Filosofía ahora con mismo efecto que proyectos: opacidad 0.5 + translateX(-15px) → 1 + 0 al entrar/salir del viewport.
- **[NUEVO 2026-06-02] Fixes alta prioridad (11/11):** type duplicado, overflow sections, contraste #bc4b21→#d45e2c, #555→#999, #666→#aaa, alt en 31 imágenes, `<noscript>`, -webkit-backdrop-filter, :focus-visible, scroll-snap-type y proximity. Threshold scroll-reveal 0.4 → 0.65.
- **[NUEVO 2026-06-02] Hero Video Optimizado:** Sustituidos los 4 clips MP4 y la lógica compleja de rotación JS por un solo archivo `hero_loop.mp4` (29s) generado con transiciones xfade nativas. Peso reducido de 20MB a 5.6MB (72% menos).
- **[NUEVO 2026-06-02] Rutas Operativas (Bloque 3):** Creación de `RUTA_CLIENTE.md` (journey del cliente), `RUTA_ARQUITECTO.md` (workflow de diseño), y `RUTA_ADMIN.md` (operaciones de negocio).
- **[NUEVO 2026-06-02] Fusión Conceptualización:** Propuesta de unificación del protocolo teórico con el método práctico de 17 pasos. Base para el futuro "Algoritmo SOMA".

---

## Estado general por bloque

| Bloque | Estado | Crítico para arrancar |
|--------|--------|----------------------|
| **1. ADM** | Casi completo. Misión/visión/valores ✅, contrato ✅, convenio de anticipo ✅, dashboard ✅, protocolos ✅. Falta RFC en RESICO. | ⬜ RFC necesario para facturar |
| **2. Taller** | Protocolos de recepción, entrevista y análisis de sitio ✅. Diagrama espacial ✅. PROCESO DE DISEÑO establecido como eje rector del Bloque 2. Diagnóstico completado (05/06/2026). Pendiente reestructura de protocolos contra el PROCESO DE DISEÑO. | ✅ Puede operar desde hoy |
| **3. I+D** | Server Flask ✅, app de entrevista ✅, DB ✅, lead magnet endpoint ✅. Falta faster-whisper + DeepSeek para IA completo. | ✅ Puede operar sin IA (entrevista manual + guía en plantilla de Word) |
| **4. MKT** | Buyer persona ✅, manifiesto accesibilidad ✅, Instagram (6 semanas de textos) ✅, lead magnet (guía + HTML) ✅, Google My Business (guía) ✅. Falta publicar web, crear cuentas, subir contenido. | ⬜ Redes + web son el motor de clientes |

**Conclusión:** Lo único que realmente detiene el primer cliente es la web publicada y presencia en redes. El RFC es problema del cobro, no de conseguir el cliente.

---

## 📅 NUEVA PRIORIDAD — 05/06/2026: PROCESO DE DISEÑO COMO EJE RECTOR

- **[NUEVO] PROCESO DE DISEÑO establecido como checklist formal y esqueleto del Algoritmo SOMA.**
- **[NUEVO] Diagnóstico crítico completado** en `DIAGNOSTICO_PROCESO_DISEÑO.md`. 16 problemas identificados.
- **[NUEVO 2026-06-08] PROCESO DE DISEÑO 2.0 generado:** Versión expandida de los 143 items originales con estructura INPUT/OPERA/OUTPUT/PROC. Cada item clasificado por:
  - Naturaleza (`[REF]`, `[OUT]`, `[DEC]`, `[ACC]`, `[EVA]`, `[GUI]`)
  - Procesador (`AI`, `HUMANO`, `AI→HUMANO`, `HUMANO→AI`)
  - Dependencias de datos explícitas (inputs desde otros items)
  - Outputs con variantes según complejidad del proyecto
  - Citas en línea formato (Autor, Año) + sección de referencias al final
  - Referencias cruzadas a protocolos (`PROTOCOLO: ruta`) en cada sección
- **[NUEVO 2026-06-08] Análisis crítico del 2.0:** Identificó 6 problemas (extensión, falta de ramas por paquete, criterio de salida en evaluación, 5.10 mal asignado, estructura estática, 2.2.3 mal marcado). Corregidos 5.10 y 2.2.3.
- **[NUEVO 2026-06-08] Protocolos renombrados y alineados al 2.0:** Los 11 protocolos existentes fueron renombrados con la numeración del PROCESO DE DISEÑO 2.0:
  - `01 Recepción e Investigación/`: 3 protocolos (recepcion_usuario, entrevista_inmersion, investigacion_previa)
  - `02 Análisis/`: 1 protocolo (analisis)
  - `03 Diseño/`: 8 protocolos (conceptualizacion, modelado, visualizacion, representacion, evaluacion, anteproyecto, planos_tecnicos, coordinacion)
  - Sin contradicciones — todos los protocolos se alinean al 2.0
  - Referencias cruzadas agregadas en el PROCESO 2.0
- **[NUEVO 2026-06-08] Matriz de inventario completa:** 21 archivos inventariados, 11 protocolos mapeados contra 9 secciones del 2.0. Cobertura total — no hay items críticos sin protocolo.

---
## 📅 SESIÓN 08/06/2026: POBLACIÓN DE BIBLIOTECA SOMA + FLUJO DE TRABAJO REAL

- **[NUEVO] Biblioteca SOMA poblada:** 6 carpetas con contenido descargado, generado o referenciado:
  - **normativas/ (8 PDFs, 35 MB):** reglamento_construccion_merida.pdf, gaceta_932_ntc_merida.pdf, NMX-R-050-SCFI-2006_accesibilidad.pdf, NOM-020-ENER-2011_eficiencia_energetica.pdf, NOM-008-ENER-2001_envolvente_no_residencial.pdf, PMDU_Merida.pdf, PIMUS_Merida_2040.pdf, Plan_Municipal_Desarrollo_2024-2027.pdf
  - **clima/:** carta_solar_merida (PNG+PDF generados por AI), rosa_vientos_merida (PNG+PDF generados por AI), INDICE_CLIMA.md con tabla de datos históricos
  - **diseno/:** REFERENCIAS_BIBLIOGRAFICAS.md con ISBN y dónde consultar Neufert, Panero, Ching (copyright → solo referencia)
  - **arquetipos/:** INDICE_ARQUETIPOS.md con 18 recursos open-access sobre casa maya, colonial, porfiriana y moderna (todos con links directos a PDFs académicos)
  - **repertorio/:** REPERTORIO_PROYECTOS.md con 15+ proyectos de referencia (vivienda en clima cálido-húmedo/contexto patrimonial)
  - **patrones/:** CATALOGO_PATRONES_DISENO.md (42 patrones SOMA propios: espaciales, de uso, tectónicos, bioclimáticos, acontecimiento) + REFERENCIA_ALEXANDER.md (34 patrones de Alexander mapeados a Mérida)
- **[NUEVO] Estrategia de adquisición definida:** AI descarga/genera lo público (normativas, datos climáticos) y referencias lo comercial (libros copyright, CONAGUA bloqueada por mod_security). AI→HUMANO para el catálogo de patrones (AI compila borrador, humano cura).
- **[NUEVO] Flujo de trabajo real validado:** El loop INPUT→OPERA→OUTPUT del PROCESO 2.0 se probó con normativas (buscar→descargar→clasificar) y se confirmó que el patrón se replica para todas las carpetas de biblioteca.

**Próxima sesión:** Continuar con protocolos o siguiente proyecto en pipeline.

---

## 📅 SESIÓN 09/06/2026: MIGRACIÓN A RENDER + POSTGRESQL

### ✅ COMPLETADO

- **[NUEVO] Migración Railway → Render:** Creado `render.yaml` (web service + PostgreSQL gratis). Eliminado `railway.json`.
- **[NUEVO] Abstracción DB (`backend/db.py`):** Soporta SQLite (local) y PostgreSQL (producción). Detecta automáticamente según `DATABASE_URL`.
- **[NUEVO] server.py reescrito:** 30+ operaciones de BD ahora usan `db.py`. Sin cambios en lógica de negocio.
- **[NUEVO] Script de migración:** `backend/migrate_to_postgres.py` — exporta SQLite → PostgreSQL.
- **[NUEVO] Dashboard con URLs relativas:** Usa `window.location.origin` en vez de `localhost:8080`.
- **[NUEVO] Dependencia:** `psycopg2-binary` agregado.
- **Documentación:** `RUTA_CLIENTE.md` y `SOLOJUAN.md` actualizados (railway.app → onrender.com).

- **[NUEVO 09/06/2026 (tarde)] Deploy completado:** Web en `soma-arquitectura.com` con HTTPS.
- **[NUEVO] Datos migrados:** 141 registros de SQLite → PostgreSQL exitosamente.
- **[NUEVO] Dominio:** `soma-arquitectura.com` registrado y apuntando a Render via Cloudflare.
- **[NUEVO] Email profesional:** Cloudflare Email Routing → Gmail. SendGrid autenticado con SPF/DKIM.
- **[NUEVO] Web actualizada:** Email cambiado a `info@soma-arquitectura.com`.

---
## 📅 ÚLTIMA ACTUALIZACIÓN: 09/06/2026
