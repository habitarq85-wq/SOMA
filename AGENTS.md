# Contexto de Sesión — Algoritmo SOMA

## Última sesión: 15 Jun 2026

### Tema: Reparación de notificación WhatsApp en cotizador

### Problema
El cotizador de `Pagina Web 6.html` dejó de enviar WhatsApp a Juan al registrarse un nuevo lead. La causa fue que **Twilio Sandbox expiró** (error 63015 — destinatario no ha hecho opt-in).

### Solución implementada
Se reemplazó Twilio por **Baileys v7** (`@whiskeysockets/baileys`), una implementación pura de Node.js del protocolo WhatsApp Web que:
- No necesita Chromium/Puppeteer (mucho más ligero)
- Conexión directa vía WebSocket
- Sesión persistente (QR solo la primera vez)
- Sin costos recurrentes

### Archivos creados/modificados
| Archivo | Cambio |
|---------|--------|
| `backend/whatsapp_service/server.js` | **(Nuevo)** Servicio HTTP con Baileys v7. Endpoints: `GET /status`, `POST /send` |
| `backend/whatsapp_service/package.json` | **(Nuevo)** Dependencias Node.js |
| `backend/whatsapp_service/.gitignore` | **(Nuevo)** Excluye session-data y node_modules |
| `backend/server.py` | **(Modificado)** `enviar_whatsapp()` ahora prueba Baileys primero, fallback a Twilio |
| `start.sh` | **(Nuevo)** Script para Render que levanta ambos servicios |
| `start_local.sh` | **(Nuevo)** Script para desarrollo local |
| `.env` | **(Modificado)** Se agregó `WA_SERVICE_HOST` |
| `render.yaml` | **(Modificado)** Build ahora instala Node.js + npm; start usa `start.sh` |
| `Procfile` | **(Modificado)** Apunta a `start.sh` |

### Cómo usar (primera vez)
1. Ejecutar `./start_local.sh`
2. Escanear el QR con WhatsApp (válido por única vez)
3. A partir de ahí, el servicio envía notificaciones automáticas a `+5219993619433`
4. Si se cierra sesión, eliminar `backend/whatsapp_service/session-data/` y repetir

### Pendientes originales (aún vigentes)
1. **Extender grafo a secciones 5–9** en `web/algoritmo_soma.html`
2. **Compuertas condicionales por paquete**

### Archivos relevantes
- `web/algoritmo_soma.html` — archivo principal, producción
- `web/grafo_conceptual.html` — prototipo standalone del grafo (380 líneas)
- `backend/whatsapp_service/server.js` — servicio WhatsApp activo

### Comandos útiles
- Validar balance div: `python3 -c "c=open('...').read();print(c.count('<div'),c.count('</div>'))"`
