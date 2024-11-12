#!/bin/bash

source_dir="/mnt/e/Devops/Devops/Linux/projects"
backup_dir="/mnt/e/Devops/Devops/Linux/backups"
timestamp=$(date +%Y%m%d%H%M%S)
backup_file="${backup_dir}/backup_$timestamp.tar.gz"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

tar -czvf "$backup_file" "$source_dir"
echo "Backup completed: $backup_file"
