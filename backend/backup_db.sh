#!/bin/bash
# Backup automático de la base de datos SOMA
# Se ejecuta desde cron, copia proyectos_arquitectonicos.db con timestamp

BACKUP_DIR="/home/juan/Documentos/PROYECTO SOMA/backend/backups"
DB_PATH="/home/juan/Documentos/PROYECTO SOMA/web/EjemploBD/proyectos_arquitectonicos.db"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
mkdir -p "$BACKUP_DIR"
cp "$DB_PATH" "$BACKUP_DIR/proyectos_arquitectonicos_$TIMESTAMP.db"

# Limpiar backups más antiguos de 30 días
find "$BACKUP_DIR" -name "proyectos_arquitectonicos_*.db" -mtime +30 -delete

echo "[$(date)] Backup creado: proyectos_arquitectonicos_$TIMESTAMP.db" >> "$BACKUP_DIR/backup_log.txt"
