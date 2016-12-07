#!/bin/bash

# crontab -e
# crontab -l
# not work in crontab(aliyun, user:root)
pg_dump kalisign | gzip > /root/backup/$(date +%Y-%m-%d).kalisign.backup.gz
tar czf /root/backup/$(date +%Y-%m-%d).data.tar.gz /root/.local/share/Odoo/filestore
rm -f /root/backup/$(date -d'-7 day' +%Y-%m-%d)*