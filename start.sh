#!/usr/bin/env bash
set -e

# Iniciar servicio WhatsApp (Baileys) en segundo plano
echo "=== Iniciando servicio WhatsApp (Baileys) ==="
WA_DIR="backend/whatsapp_service"

# Instalar Node.js via NVM si no está disponible
if ! command -v node &>/dev/null; then
    export NVM_DIR="$HOME/.nvm"
    if [ ! -d "$NVM_DIR" ]; then
        echo "Instalando NVM + Node.js..."
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash 2>/dev/null
    fi
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
    if command -v node &>/dev/null; then
        echo "Node.js listo: $(node --version)"
    else
        echo "⚠️  No se pudo instalar Node.js — WhatsApp desactivado"
    fi
fi

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
fi

# Iniciar servidor Flask en primer plano
echo "=== Iniciando servidor Flask ==="
exec gunicorn backend.server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --worker-class=gthread --threads=4
