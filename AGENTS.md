# Contexto de Sesión — Algoritmo SOMA

## Última sesión: 16 Jun 2026 (Parte 2) ✅

### Tema: Flujo Momento 1 a Momento 2, Reestructuración del Dashboard, Fix DB Postgres

### Qué se hizo en esta sesión
1. **Reestructuración del Dashboard:**
   - División en 3 bloques principales: **CANDIDATOS — MOMENTO 1** (Leads), **CLIENTES — MOMENTO 2** (Contratados), y **BLOQUE 02: TALLER SOMA** (Vista detallada operativa).
   - Actualización de las tarjetas de leads para incluir botones consistentes: `[ EXPEDIENTE ] [ PROGRAMA ] [ CONTRATAR ]`.
2. **Flujo de Contratación (Momento 1 -> Momento 2):**
   - El botón **CONTRATAR** ahora sirve únicamente para confirmar el pase a Momento 2 (cambia el pipeline a `contratado`).
   - Se agregó validación: no permite contratar si los "Datos del Proyecto" no están completos.
3. **Datos del Proyecto y Autoguardado en PROGRAMA:**
   - Se movieron los campos de configuración (Nombre Cliente, Proyecto, Tipo, Nivel, Ubicación) a la cabecera del modal **PROGRAMA**.
   - Se implementó **autoguardado inteligente**: cambiar de pestaña hacia "Cotización" guarda automáticamente los datos y recalcula los honorarios/obra usando el Nivel seleccionado sin recargar.
4. **Fix Crítico Base de Datos (PostgreSQL):**
   - Se corrigió un bug en `db.py` al migrar de SQLite a Postgres: se agregó dinámicamente `RETURNING id` a las consultas `INSERT` para que `get_lastrowid()` funcione correctamente. Esto resolvió el problema de creación de espacios en el Programa Arquitectónico.

### Cambios adicionales
- Limpieza de datos de prueba, manteniendo ejemplos fieles a lo generado por la Inmersión Web (Cotizador).
- Adición de las columnas de ubicación y nombre_cliente en `captura_web`.

### Archivos modificados
| Archivo | Cambio |
|---------|--------|
| `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/Dashboard.html` | **(Modificado)** Reestructura Momento 1 y 2, nuevos modals y validaciones, autoguardado de cotización. |
| `backend/server.py` | **(Modificado)** Nuevo endpoint `PATCH /lead/<id>/datos-proyecto`. Ajuste en ruta `contratar`. |
| `backend/db.py` | **(Modificado)** Fix `RETURNING id` en función `adapt_sql` para PostgreSQL. |

### Pendientes (PRÓXIMA SESIÓN)
1. **Continuar trabajando con el Dashboard**.
2. **Crear los campos de la base de datos "integral"** (expandir las tablas y modelo de datos general del proyecto).
3. (Opcional) Compuertas condicionales por paquete (Básico/Integral/Ejecutivo) en Algoritmo SOMA.

### Archivos relevantes
- `web/algoritmo_soma.html`
- `backend/server.py` y `backend/db.py`
- `metodologia/Bloque 1 - Gestion del Entorno (ADM)/dashboard/Dashboard.html`

### Comandos útiles
- Servir local: `cd /home/juan/Documentos/PROYECTO\ SOMA/backend && source venv/bin/activate && DATABASE_URL=postgresql://soma_user:soma_pass@localhost:5432/soma_db python server.py`
- Dashboard: `http://localhost:8080/dashboard`
