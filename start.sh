#!/usr/bin/env bash
set -e

# Iniciar servidor Flask en primer plano
echo "=== Iniciando servidor Flask ==="
exec gunicorn backend.server:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --worker-class=gthread --threads=4
