#!/usr/bin/env bash
set -e

# Iniciar servicio WhatsApp (Baileys) en segundo plano
echo "=== Iniciando servicio WhatsApp (Baileys) ==="
WA_DIR="backend/whatsapp_service"
if command -v node &>/dev/null; then
    if [ ! -d "$WA_DIR/node_modules/@whiskeysockets/baileys" ]; then
        echo "Instalando dependencias Node.js..."
        cd "$WA_DIR" && npm install && cd "$OLDPWD"
    fi
    cd "$WA_DIR"
    node server.js &
    WA_PID=$!
    cd "$OLDPWD"
    echo "WhatsApp service PID: $WA_PID"
    sleep 3
else
    echo "⚠️  Node.js no disponible — WhatsApp desactivado"
fi

# Iniciar servidor Flask en primer plano
echo "=== Iniciando servidor Flask ==="
exec gunicorn backend.server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --worker-class=gthread --threads=4
