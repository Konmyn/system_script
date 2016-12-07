#!/bin/bash

# crontab -e
# crontab -l
# not work in crontab(aliyun, user:root)
python /root/system_script/db-tools.py -b 8069 -s admin123 backup -d kalisign -f /root/backup/$(date +%Y%m%d).kalisign.backup.zip
pg_dump kalisign | gzip > /root/backup/$(date +%Y-%m-%d).kalisign.backup.gz
tar czf /root/backup/$(date +%Y-%m-%d).data.tar.gz /root/.local/share/Odoo/filestore
rm -f /root/backup/$(date -d'-7 day' +%Y-%m-%d)*

# tobe read
tar czf /root/backup/$(date +%Y-%m-%d).data.tar.gz /root/.local/share/Odoo/filestore >> /root/test.log 2>&1

# working:
python /root/system_script/odoo_backup_linux.py
python /root/system_script/db-tools.py -b 8069 -s admin123 backup -d kalisign -f /root/backup/`date "+\%Y\%m\%d"`.kalisign.backup.zip
pg_dump kalisign | gzip > /root/backup/`date "+\%Y\%m\%d"`.kalisign.backup.gz
tar czf /root/backup/`date "+\%Y\%m\%d"`.data.tar.gz /root/.local/share/Odoo/filestore
rm -f /root/backup/`date "-d'-1 day' +\%Y\%m\%d"`*

# final
# m h  dom mon dow   command
MAILTO=""
0 5 * * * python /root/system_script/db-tools.py -b 8069 -s admin123 backup -d kalisign -f /root/backup/`date "+\%Y\%m\%d"`.kalisign.backup.zip
5 5 * * * pg_dump kalisign | gzip > /root/backup/`date +\%Y\%m\%d`.kalisign.backup.gz
5 5 * * * tar czf /root/backup/`date +\%Y\%m\%d`.data.tar.gz /root/.local/share/Odoo/filestore
9 5 * * * rm -f /root/backup/`date -d"-5 day" +\%Y\%m\%d`*