#!/bin/bash

BACKUP_DIR="/backup"
DB_NAME="notesdb"
DB_USER="noteuser"
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_$(date +%Y-%m-%d_%H-%M-%S).sql"

mysqldump -u "$DB_USER" -p'NotePass123!' "$DB_NAME" > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully:"
    echo "$BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi
