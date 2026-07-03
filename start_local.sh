#!/usr/bin/env bash
set -e
echo "=== Iniciando SOMA local ==="

# Activar entorno virtual
source backend/venv/bin/activate 2>/dev/null || true

# Cargar variables de entorno (exporta todo el .env)
set -a
[ -f ".env" ] && source .env
set +a

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
