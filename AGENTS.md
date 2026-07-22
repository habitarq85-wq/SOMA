# Contexto de Sesión — Algoritmo SOMA

## Estado del Proyecto
- ✅ **DASHBOARD funcional**: Pipeline completo (3 momentos), expediente, PDFs, métricas, auth.
- ✅ **Base de datos en Supabase (Pooler IPv4)**: PostgreSQL vía `aws-0-us-east-1.pooler.supabase.com:6543`. Keep-warm cada 5 min con query SQL real (`/keepwarm`).
- ✅ **Fallback local SQLite**: Si Supabase falla, `db.py` usa automáticamente el backup local (`web/EjemploBD/proyectos_arquitectonicos.db`).
- ✅ **Backup diario**: Cron a las 12pm ejecuta `backup_pg_to_sqlite.py` para mantener el SQLite local sincronizado.
- ✅ **Cloudflare Cache**: 3 Page Rules activas (Cache Everything + Edge TTL 2h) para carga instantánea de la web.

## Sesión: 21 Jul 2026 ✅

### Bitácora del día
1. **Diagnóstico de caída**: Supabase pausó el proyecto gratuito por inactividad. Worker keep-warm no contaba como actividad de BD porque solo pingueaba el API REST.
2. **Reactivación**: Juan resumió el proyecto desde app.supabase.com. Datos intactos.
3. **Keep-warm real**: Endpoint `/keepwarm` con `SELECT 1` agregado a `server.py`. Worker actualizado para pinguear este endpoint.
4. **Backup Supabase→SQLite**: Script `backup_pg_to_sqlite.py` exporta 8 tablas (60 registros) a SQLite local.
5. **Fallback automático**: `db.py` ahora atrapa errores de conexión PostgreSQL y cae a SQLite sin intervención.
6. **Cron diario**: Backup automático cada 12pm.
7. **Push a GitHub**: Render desplegando cambios.

### Archivos creados/modificados
- `backend/backup_pg_to_sqlite.py` — Nuevo
- `backend/db.py` — Fallback PG→SQLite
- `backend/server.py` — Endpoint `/keepwarm`
- `workers/keep-warm/src/index.js` — Ping a `/keepwarm`
- `.env` — DATABASE_URL reactivado
- `AGENTS.md`, `BITACORA_SOMA.md`, `SOMA_CORE_INDEX.md`, `SOMA_SNAPSHOT.md` — Actualizados

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

---

## Sesión: 06 Jul 2026 ✅

### Bitácora del día
1. **Investigación de tendencias**: Tiny Houses, Cohousing, Coliving, Conversión casa→deptos, Vivienda sustentable. Documentadas tendencias en México/LATAM 2026.
2. **6 posts Instagram creados** con nueva composición "Editorial Split" (50/50 imagen + texto, barra acento terracota) para diferenciar temas conceptuales de posts de proyectos.
3. **Imágenes libres descargadas**: 5 fotos de Unsplash/Pexels para temas conceptuales en `recursos_graficos/img_tendencias/`.
4. **Tooling permanente**: `package.json` + `screenshot.js` instalados en `material_instagram/`. Comando: `npm run generate`. Ya no requiere instalar puppeteer cada vez.
5. **PNGs generados**: 6 imágenes en `publicaciones/` (post_06a a post_10).
6. **CONTENIDO_INSTAGRAM.md actualizado**: Semanas 7-8 agregadas con captions completos.

### Archivos creados/modificados
- `recursos_graficos/material_instagram/post_06a_tiny_houses.html` — Nuevo
- `recursos_graficos/material_instagram/post_06b_tiny_houses.html` — Nuevo
- `recursos_graficos/material_instagram/post_07_cohousing.html` — Nuevo
- `recursos_graficos/material_instagram/post_08_coliving.html` — Nuevo
- `recursos_graficos/material_instagram/post_09_conversion.html` — Nuevo
- `recursos_graficos/material_instagram/post_10_5_formas.html` — Nuevo
- `recursos_graficos/material_instagram/package.json` — Nuevo (tooling)
- `recursos_graficos/material_instagram/screenshot.js` — Nuevo (script)
- `recursos_graficos/img_tendencias/` — 5 imágenes libres
- `Bloque 4/CONTENIDO_INSTAGRAM.md` — Semanas 7-8 + captions
- `AGENTS.md` — Comando actualizado para generar PNGs

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 03 Jul 2026 ✅

### Bitácora del día
1. **Migración de Render PostgreSQL a Supabase**: Eliminada DB de Render que inyectaba `DATABASE_URL` malformada (`DATABASE_URL=postgresql://...` con key+value concatenado). Código actualizado para hacer stripping del prefijo `KEY=` en `_get_db_url()`.
2. **Problema IPv6**: Supabase free tier solo tiene IPv6 (`2600:1f18:...`). Render no puede enrutar → `Network is unreachable`. Solucionado usando **Supabase Connection Pooler** con IPv4: `aws-0-us-east-1.pooler.supabase.com:6543` con usuario `postgres.dejojumyyydrlqoegqnf`.
3. **render.yaml**: URL actualizada al pooler, quitado `pgbouncer=true` (no válido para psycopg2).
4. **db.py**: `_get_db_url()` ahora prueba `SUPABASE_URL` primero, luego `DATABASE_URL`. Hace stripping automático de `KEY=` prefix. Debug logging de env vars.
5. **server.py**: `init_db()` verifica `SUPABASE_URL` y `DATABASE_URL` para `use_pg`.
6. **Cloudflare Worker keep-warm**: Actualizado para pinguear también `https://dejojumyyydrlqoegqnf.supabase.co` cada 5 min y evitar que Supabase se pause por inactividad.
7. **Token Cloudflare**: Guardado en `.env` (gitignored). Comando deploy: `cd workers/keep-warm && source ../../.env && wrangler deploy`.
8. **Deploy exitoso**: Clientes visibles en dashboard, datos accesibles vía pooler.

### Archivos modificados
- `backend/db.py` — KEY= stripping, debug logging, SUPABASE_URL priority
- `backend/server.py` — use_pg verifica SUPABASE_URL + DATABASE_URL
- `render.yaml` — Pooler URL (IPv4), removed `pgbouncer=true`
- `workers/keep-warm/src/index.js` — Agregado ping a Supabase
- `.env` — URL pooler + Cloudflare token
- `start.sh`, `start_local.sh` — WhatsApp Baileys eliminado (sesiones anteriores)

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 26 Jun 2026 ✅

### Bitácora del día
1. **Botón Cotizador SOMA en portada**: texto naranja "Cotizador SOMA" debajo de "Taller Virtual de Arquitectura", con fondo negro 40% opacity, padding ajustado, cursor pointer. Llama a `openImmersion()`.
2. **Cache de Cloudflare**: 3 Page Rules configuradas (`/`, `/recursos_graficos/*`, `/web/*`) con Cache Everything + Edge Cache TTL 2h. La web se sirve desde el edge de Cloudflare, eliminando cold start de Render.
3. **`_redirects` creado** (para futura migración a Cloudflare Pages): mapea rutas estáticas directo y APIs proxy a `soma-853c.onrender.com`.

## Sesión: 27 Jun 2026 ✅

### Bitácora del día
1. **Cloudflare Worker keep-warm desplegado**: `soma-keep-warm` con cron `*/5 * * * *` (cada 5 min) que pinguea `soma-853c.onrender.com` para evitar que Render se duerma por inactividad. URL: `https://soma-keep-warm.habitarq85.workers.dev`.
2. **Token Cloudflare creado**: `SOMA Workers Deploy` con permisos `Workers Scripts -> Edit` + `User Details -> Read`. Almacenado localmente para deploy via Wrangler.
3. **Estructura creada**: `workers/keep-warm/wrangler.toml` + `src/index.js`.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 26 Jun 2026 ✅

### Bitácora del día
1. **Estación 4 corregida contra PROCESO DE DISEÑO 2.0**: reestructuración completa de 15 cards en `algoritmo_soma.html`:
   - Eliminado: 4.3 "Documento de Intenciones" y 4.15 "Documento de Concepto" (no existen en 2.0)
   - Separado en 2 pasos c/u: Volumetrización+Zonificación → 4.3+4.4, y Ubicación+Accesos → 4.5+4.6
   - Agregados sub-items: 4.8.1-6 (Espacialidad), 4.9.1-8 (Evaluación I), 4.11.1-6 (Configuración), 4.14.1 (Evaluación II)
   - Renombrado: 4.1, 4.2, 4.7, 4.15 según nomenclatura de 2.0
2. **CSS para sub-items**: clases `.stag.sh/sa/sm` con colores de procesador (naranja/azul/morado) para tags en sub-items.
3. **Limpiados rangos numéricos redundantes** en textos OPERA de cards 4.8, 4.9, 4.11, 4.14 para evitar que "4.8.1" apareciera dos veces (en texto y en listado).

### Próxima sesión
- Afinar detalles visuales de Estación 4
- Vincular estaciones 5+ (Modelado, Visualización, Anteproyecto) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación

## Sesión: 24 Jun 2026 ✅

### Bitácora del día
1. **Estación 1 simplificada**: Solo tarjeta 1.1 Contacto (eliminada 1.2 Programa y datos reales inyectados).
2. **Mensaje placeholder**: Cambiado "Sin proyectos activos en Momento 2" → "Sin proyectos registrados."
3. **Lección**: No mezclar cambios visuales con cambios de infraestructura (server.py / fetch). Mantener server.py intacto para evitar romper auth.

## Sesión: 22 Jun 2026 (p.m.) ✅

### Bitácora del día
1. **Barra de progreso global eliminada**: removido marcador de avance por estación (HTML+CSS+JS). Se conserva solo Estación 10 como Control.
2. **Barra de avance en tarjeta de proyecto**: cada proyecto en el selector ahora muestra una barra que se llena de izquierda a derecha (0–100%) con el progreso real del algoritmo. Se actualiza al cargar/guardar progreso vía `calcularProgresoGlobal()` + `actualizarProgresoTarjeta()`.

## Sesión: 22 Jun 2026 (noche) ✅

### Bitácora del día
1. **Diagrama SOMA integrado en Algoritmo (3.4)**: 
   - Botón "ABRIR DIAGRAMA DE RELACIONES" en la tarjeta 3.4 de Station 3 (Análisis).
   - Sección colapsable debajo del step-grid con vis-network (force-directed graph).
   - Carga datos reales desde `/api/diagrama/grafo/<proyecto_id>` (espacios + relaciones).
   - Filtro por zona (Social/Operativa/Descanso/Soporte/Transición).
   - Posiciones guardadas en localStorage, botón Reset, export PNG.
   - Leyenda cromática por zona.
2. **Cambio de proyecto re-renderiza estación activa**: al seleccionar otra tarjeta, la estación visible se actualiza con los datos del nuevo proyecto (incluyendo diagrama si está abierto).

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 23 Jun 2026 ✅

### Bitácora del día
1. **Corrección doble-codificación JSON en ubicación**: `programa.js` y `server.py` ahora usan columnas directas (`calle_numero`, `colonia`, `ciudad`, `estado_ubic`) en vez de `ubicacion` JSON, eliminando el bug de datos que se perdían al reabrir el modal.
2. **PDFs de expediente y cierre con respuestas A/B descriptivas**: mapeo completo de los 10 pasos de inmersión (step1…step10) con sus opciones (p.ej. `Pregunta 1: B. Cerrada`) tanto en el expediente modal, PDF de expediente y PDF de cierre.
3. **Protección de Momento 2**: el modal PROGRAMA se vuelve de solo lectura en fases `contratado`, `primera_entrega`, `entrega_final` (botones de agregar/eliminar espacios y guardar ocultos).
4. **Botón ELIMINAR en Momento 1**: todas las tarjetas de Candidatos ahora muestran botón ELIMINAR para borrar leads sin inmersión completa o erróneos (p.ej. "Casa del sol").
5. **Refresh robusto**: timeouts de 10s en cada `fetch` y 15s en `App.refresh()` + guard de modal solo en auto-refresh (30s), nunca en manual.
6. **Datos de ubicación como columnas simples**: migración automática en `init_db()` crea `calle_numero`, `colonia`, `ciudad`, `estado_ubic` en `captura_web`; PDFs y expediente leen directo.
7. **Auth básica en Render**: protección HTTP Basic Auth en `/dashboard`, `/algoritmo`, APIs y PDFs. Credenciales por defecto `admin` / `Yucata85` (configurables vía `DASHBOARD_USER` / `DASHBOARD_PASS` en Render). Página pública (`/`, `/web/*`, `/css/*`, `/recursos_graficos/*`, `/backend/*`) sin protección.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web

## Sesión: 22 Jun 2026 (madrugada) ✅

### Bitácora del día
1. **Expediente simplificado (v1)**: removidos cobros del modal expediente. Orden exacto v1: datos de inmersión → análisis multidimensional → respuestas A/B línea por línea → programa arquitectónico → PDF de expediente.
2. **Respuestas A/B en español**: formato "Pregunta 1: a Fachada abierta", "Pregunta 2: b Privacidad cerrada", etc. con labels descriptivos desde BD.
3. **Ruta PDF expediente**: `/lead/<id>/expediente-pdf` genera HTML imprimible del expediente completo (datos, análisis, respuestas, programa).
4. **DB limpia**: eliminados proyectos 7 (María Torres), 9 (Juan Pérez), 11 (Casa Alina). Único proyecto demo `SOMA-20260622-DEMO` con inmersión completa.
5. **Fix métricas Bloque 01**: `cargarMetrics()` llamado directamente antes de `App.refresh()` en `pagarCobroDirecto` y `avanzar` para evitar que el guard de modal activo bloquee la actualización de KPIs.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación
- Lead magnet — decidir ubicación en página web
- Revisar deploy en Render (soma.onrender.com responde 404 no-server)

### Comandos
```bash
# Servidor
systemctl --user stop soma-flask.service
systemd-run --user --unit=soma-flask --setenv=DATABASE_URL=postgresql://soma_user:soma_pass@localhost:5432/soma_db /home/juan/Documentos/PROYECTO\ SOMA/backend/venv/bin/python /home/juan/Documentos/PROYECTO\ SOMA/backend/server.py

# Logs
journalctl --user -u soma-flask.service -f

# Dashboard
http://localhost:8080/dashboard

# Algoritmo
http://localhost:8080/algoritmo

# PostgreSQL
PGPASSWORD=soma_pass psql -h localhost -U soma_user -d soma_db

# Métricas
curl -s "http://127.0.0.1:8080/metrics/bloque01?year=2026&month=6" | python3 -m json.tool

# Expediente PDF
curl -s "http://127.0.0.1:8080/lead/12/expediente-pdf"
```

### Archivos clave
```
web/
├── dashboard.html          # Dashboard 2.0
├── css/
│   ├── dashboard.css       # Estilos oscuros (dark editorial)
│   └── algoritmo.css       # Estilos del Algoritmo SOMA
├── js/
│   ├── api.js              # API calls
│   ├── ui.js               # UI utilities
│   ├── leads.js            # Leads, pipeline, expediente, pagos
│   ├── egresos.js          # Gastos de operación
│   ├── fondos.js           # Fondos de provisión
│   ├── programa.js         # Programa arquitectónico + cotización
│   ├── app.js              # App shell, refresh loop, metrics
│   └── algoritmo.js        # Algoritmo SOMA (tarjetas, diagrama, programa)
├── algoritmo_soma.html     # Algoritmo con tarjetas de proyecto
├── guia_visita.html        # Guía de visita (checklist sitio + ambientales + 6 tópicos)
└── guia_entrevista.html    # (obsoleto, reemplazado por guia_visita)

backend/server.py           # Flask (rutas: leads, cobros, metrics, expediente-pdf, programa/html)
antecedentes/dashboard_v1/  # Dashboard original (referencia)
```

## Flujo de trabajo — Contenido Instagram

### Proceso para crear posts
1. El usuario pide contenido para Instagram (tema, cantidad)
2. Crear cards HTML (800×800px) con identidad visual SOMA:
   - Fondo oscuro `#0a0a0a`, acento terracota `#d45e2c`
   - Tipografía: Georgia (serif) + Courier New (monospace)
   - Imágenes de fondo desde `recursos_graficos/Carrusel_por_proyecto/`
   - Pie con `info@soma-arquitectura.com · soma-arquitectura.com`
3. Guardar en `recursos_graficos/material_instagram/post_XX_tema.html`
4. Generar PNG con Puppeteer (herramienta instalada permanente):
   ```bash
   cd "/home/juan/Documentos/PROYECTO SOMA/recursos_graficos/material_instagram" && npm run generate
   ```
5. Las imágenes quedan en `recursos_graficos/material_instagram/publicaciones/`
6. Entregar captions listos para copiar/pegar

### Para carruseles (varias slides)
- Nombrar: `post_01a_tema.html` (slide 1), `post_01b_tema.html` (slide 2)
- Incluir indicador "1/2", "2/2" y "Desliza →"

### Captions
- Incluir siempre: texto del post + llamada a la acción (pregunta en comentarios)
- Hashtags: #ArquitecturaMérida #ConstruirEnMérida #PrimeraCasa #SOMATallerVirtual + específicos
```
