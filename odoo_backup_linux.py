#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, datetime

# postgreSQL的当前用户
PG_USER = 'root'
# 当前用户(administrator)的postgres登录密码
PG_PASSWORD = 'admin'
# 需要备份的数据库列表
DATABASES = ['kalisign']
# 备份文件夹
backup_dir = '/root/backup/'
# data_dir in odoo.conf and then specified for filestore.
data_dir = '/root/.local/share/Odoo'
# log文档的全路径
log_path = backup_dir + 'backup.log'


# time related variables
# 获取当前时间
_now = datetime.datetime.now()
# 2016-11-02-11-28-21, 用类似这样的格式作为文件前缀
today_file = _now.strftime("%Y%m%d")
print today_file
# 2016-11-02 14:47:31, 用类似这样的时间格式作为log信息记录
today_str = _now.strftime("%Y-%m-%d %H:%M:%S")
print today_str

# 创建日志函数
def writeLogs(filename, contents):
    log_file = file(filename,'a+')
    log_file.write(contents)
    log_file.close()

# 数据库备份函数
def postgress_database_backup(user, databases, file_path, file_prefix):
    for datebase in databases:
        backup_name = '{}.{}.backup.gz'.format(file_prefix, datebase)
        backup_cmd = "pg_dump {} | gzip > {}".format(datebase, file_path+backup_name)
        if os.system(backup_cmd):
            writeLogs(log_path, "Backup database failed!\n")
        else:
            writeLogs(log_path, "Backup *{}* completed.\n".format(datebase))
    return True

# 文件夹备份函数
def file_dir_backup(directory, file_path, file_prefix):
    backup_name = '{}.data.backup.gz'.format(file_prefix)
    cmp_cmd = "gzip {} > {}".format(file_path, backup_name)
    if os.system(zip_cmd):
        writeLogs(log_path, "Backup filestore failed!\n")
        return False
    else:
        writeLogs(log_path, "Backup #filestore# completed.\n")
        return True

# 旧备份文件删除函数
def deleteBackup(file_path, term=7):
    prefix = (datetime.datetime.now() - datetime.timedelta(days = term)).strftime("%Y-%m-%d")
    _files = os.listdir(file_path)
    for _file in _files:
        if _file[:len(prefix)] == prefix:
            target_path = os.path.join(file_path, _file)
            del_cmd = "del/f/s/q {}".format(target_path)
            if os.system(del_cmd):
                writeLogs(log_path, "Delete file failed: {}\n".format(_file))
            else:
                writeLogs(log_path, "Delete file completed: {}\n".format(_file))
            # try:
            #     os.remove(file_path)
            #     writeLogs(log_path, "Delete file completed: {}\n".format(_file))
            # except:
            #     writeLogs(log_path, "Delete file failed: {}\n".format(_file))
    return True

def main():
    '''
    speciafied for central hub company.
    system information: windows server 2008.
    datetime:2016-11-02
    target software: odoo 10 enterprise
    '''
    writeLogs(log_path, "-"*79 + "\nOperation time: {}\n".format(today_str))
    postgress_database_backup(PG_USER, DATABASES, backup_dir, today_file)
    # file_dir_backup(data_dir, backup_dir, today_file)
    # deleteBackup(backup_dir, 10)

if __name__ == "__main__":
    main()