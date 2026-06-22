# Contexto de Sesión — Algoritmo SOMA

## Sesión: 22 Jun 2026 ✅

### Bitácora del día
1. **Station 2 → Inmersión Web real**: `renderImmersionReal()` — muestra las 10 respuestas A/B de `respuestas_json` con labels (Fachada, Privacidad, Flexibilidad, etc.). Se inyecta dinámicamente en 2.2 Material Variable.
2. **Station 3 → Análisis Procesado real**: `renderAnalisisReal()` — despliega el `analisis_procesado` (reporte multidimensional con Psicología Ambiental, Lenguaje de Patrones, Space Syntax, Conducta Ambiental, POE) en secciones formateadas.
3. **Station 1 → Cobros reales**: `renderContactoReal()` — ahora muestra los pagos del proyecto con montos y estado (✅ Pagado / ⏳ Pendiente) desde la tabla `cobros`.
4. **Llamadas integradas** en `showSection()` para que cada estación cargue datos reales al activarse.

### Próxima sesión
- Vincular estaciones 4+ (Conceptualización, Modelado, Visualización) con datos de la BD
- Considerar crear tabla `algoritmo_contenido` para almacenar outputs de cada estación

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

## Sesión: 19 Jun 2026 (tarde/noche) ✅

### Bitácora del día
1. **KPIs por período contable**: `/metrics/bloque01` filtra por `?year=` y `?month=`. Clientes Activos excluye `terminado`. `Ingresos del Período` sobre `Monto Acumulado`. `Gasto de Operación` desde egresos.
2. **Botones de pago directo**: ANTICIPO (F1), PAGO 1RA (F2), PAGO FINAL (F3) — marcan cobro como pagado sin confirm. Botones de avance advierten si falta pago.
3. **Dashboard 2.0**: Reescribito en `web/` con módulos separados (api.js, ui.js, leads.js, egresos.js, fondos.js, programa.js, app.js). Sin `alert()`, datos escapados, botones con loading state, concurrencia controlada. CSS limpio en `web/css/dashboard.css`.
4. **Fondos de provisión (B03)**: Tablas `fondos` + `movimientos_fondo`. API: CRUD + apartar/retirar. UI en dashboard.
5. **Limpieza de BD**: Eliminadas 7 tablas vacías. Eliminadas columnas `presupuesto` y `habitantes` de `captura_web`. `init_db` actualizado.
6. **Dashboard v1 archivado**: Movido a `antecedentes/dashboard_v1/`.
7. **Algoritmo SOMA**: Dropdown reemplazado por tarjetas visuales colapsables. Muestra solo Momento 2. Clic expande/colapsa. Banner eliminado. Botón PROGRAMA abre dashboard.

### Próxima sesión
- Continuar desarrollo del Algoritmo SOMA
- Vincular estaciones del algoritmo con datos reales de la BD

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
```

### Archivos clave
```
web/
├── dashboard.html          # Dashboard 2.0
├── css/dashboard.css       # Estilos
├── js/                     # Módulos JS
│   ├── api.js, ui.js, leads.js, egresos.js, fondos.js, programa.js, app.js
└── algoritmo_soma.html     # Algoritmo con tarjetas de proyecto
backend/server.py           # Flask (rutas actualizadas)
antecedentes/dashboard_v1/  # Dashboard original
```
