#!/usr/bin/env bash
set -e
echo "=== Iniciando SOMA local ==="

# Activar entorno virtual
source backend/venv/bin/activate 2>/dev/null || true

# Cargar variables de entorno (exporta todo el .env)
set -a
[ -f ".env" ] && source .env
set +a

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

# Iniciar Flask (usa el venv si existe)
echo "Iniciando servidor Flask..."
PYTHON=python3
[ -f "backend/venv/bin/python" ] && PYTHON="backend/venv/bin/python"
nohup $PYTHON backend/server.py > /tmp/soma_flask.log 2>&1 &
FLASK_PID=$!
echo ""
echo "============================================"
echo "  SOMA iniciado correctamente"
echo "  Dashboard: http://localhost:8080/dashboard"
echo "  PID Flask: $FLASK_PID"
echo "  Logs: tail -f /tmp/soma_flask.log"
echo "============================================"
echo ""
