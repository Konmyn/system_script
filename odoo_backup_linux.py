#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, datetime

# postgreSQL的当前用户
PG_USER = 'root'
# 需要备份的数据库列表
DATABASES = ['kalisign']
# 备份文件存放路径
backup_dir = '/root/backup/'
# data_dir in odoo.conf and then specified for filestore.
data_dir = '/root/.local/share/Odoo/filestore'
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

global logging = ''

def _logger(strings):
    global logging += strings

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
            _logger("Backup database failed!\n")
        else:
            _logger("Backup *{}* completed.\n".format(datebase))
    return True

# 文件夹备份函数
def file_dir_backup(directory, file_path, file_prefix):
    backup_name = '{}.data.tar.gz'.format(file_prefix)
    # tar czvf usr.tar.gz /home
    # tar xzvf usr.tar.gz
    cmp_cmd = "tar czvf {} {}".format(backup_name, file_path)

    if os.system(cmp_cmd):
        _logger("Backup odoo data files failed!\n")
        return False
    else:
        _logger("Backup #odoo data files# completed.\n")
        return True

# 旧备份文件删除函数
def delete_old_backup(file_path, term=7):
    prefix = (datetime.datetime.now() - datetime.timedelta(days = term)).strftime("%Y%m%d")
    print prefix
    _files = os.listdir(file_path)
    for _file in _files:
        if _file[:len(prefix)] == prefix:
            target_path = os.path.join(file_path, _file)
            rm_cmd = "rm -f {}".format(target_path)
            if os.system(rm_cmd):
                _logger("Delete file failed: {}\n".format(_file))
            else:
                _logger("Delete file completed: {}\n".format(_file))
    return True

def main():
    '''
    speciafied for kalisign company.
    system information: linux.
    datetime:2016-12-06
    target software: odoo 10 enterprise
    '''
    _logger("-"*79 + "\nOperation time: {}\n".format(today_str))
    postgress_database_backup(PG_USER, DATABASES, backup_dir, today_file)
    file_dir_backup(data_dir, data_dir, today_file)
    delete_old_backup(backup_dir)
    writeLogs(log_path, global logging)

if __name__ == "__main__":
    main()