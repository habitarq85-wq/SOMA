#!/usr/bin/env bash
set -e
echo "=== Iniciando SOMA local ==="

# Activar entorno virtual
source backend/venv/bin/activate 2>/dev/null || true

# Iniciar WhatsApp service
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
if command -v node &>/dev/null; then
    echo "Iniciando servicio WhatsApp (Baileys)..."
    cd backend/whatsapp_service
    node server.js &
    WA_PID=$!
    cd "$OLDPWD"
    echo "WhatsApp PID: $WA_PID"
else
    echo "⚠️  Node.js no instalado"
fi

sleep 2

# Iniciar Flask
echo "Iniciando servidor Flask..."
python3 backend/server.py
