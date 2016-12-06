#!/bin/bash

# crontab -e
# crontab -l

pg_dump kalisign | gzip > /root/backup/$(date +%Y-%m-%d).kalisign.backup.gz
tar czf $(date +%Y-%m-%d).data.tar.gz /root/.local/share/Odoo/filestore
rm -f $(date -d'-7 day' +%Y-%m-%d)*