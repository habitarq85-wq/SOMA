# Contexto de Sesión — Algoritmo SOMA

## Estado del Proyecto
- ✅ **DASHBOARD funcional**: Pipeline completo (3 momentos), expediente, PDFs, métricas, auth.
- ✅ **Base de datos arrancada para clientes**: PostgreSQL con migración automática, columnas de ubicación, leads demo, auth en Render.

## Sesión: 23 Jun 2026 ✅

### Bitácora del día
1. **Fix scroll modal**: `document.body.style.overflow = 'hidden'` ahora se restaura al cerrar modales (ui.js).
2. **Egresos filtrados por período**: Bloque 02 ahora usa el selector de mes/año como los KPI (egresos.js).
3. **Salarios en Bloque 02**: Nuevo sub-apartado con registro y tabla independiente (categoría "Salario").
4. **Fondos de Reemplazo**: Movido de Bloque 03 a Bloque 02, con aportación directa desde cada tarjeta.
5. **Algoritmo SOMA**: Muestra proyectos desde Momento 1, no solo Momento 2.
6. **Estación 1 simplificada**: Solo 2 tarjetas (1.1 Contacto, 1.2 Programa) + datos reales inyectados.

### Próxima sesión
- Revisar inconsistencias en el flujo de trabajo del Algoritmo SOMA

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
├── css/dashboard.css       # Estilos oscuros (dark editorial)
├── js/
│   ├── api.js              # API calls
│   ├── ui.js               # UI utilities
│   ├── leads.js            # Leads, pipeline, expediente, pagos
│   ├── egresos.js          # Gastos de operación
│   ├── fondos.js           # Fondos de provisión
│   ├── programa.js         # Programa arquitectónico + cotización
│   └── app.js              # App shell, refresh loop, metrics
└── algoritmo_soma.html     # Algoritmo con tarjetas de proyecto

backend/server.py           # Flask (rutas: leads, cobros, metrics, expediente-pdf)
antecedentes/dashboard_v1/  # Dashboard original (referencia)
```
