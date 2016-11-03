# -*- coding: utf8 -*-


import os, datetime

# postgreSQL的当前用户
pg_user = 'administrator'
# 当前用户(administrator)的postgres登录密码
pg_pwd = 'admin'
# 需要备份的数据库列表
db_names = ['chc','test']
# 备份文件夹
backup_path = 'D:\\pgbackup\\'
# data_dir in odoo.conf and then specified for filestore.
data_dir = 'D:\\ERP\\data\\filestore\\'
odoo_dir = 'D:\\ERP\\'
# log文档的全路径
log_path = backup_path + 'backup.log'
# postgres安装的执行文件路径，最好加入系统path当中
# pg_path = 'C:\\Program Files\\PostgreSQL\\9.6\\bin\\'


# 创建日志函数
def writeLogs(filename, contents):
    f = file(filename,'a+')
    f.write(contents)
    f.close()
    return True

# 数据库备份函数
def pgdbBackup(user, pwd, db_list, file_path, file_prefix):
    # 把当前postgreSQL用户的密码写入环境变量
    # os.putenv('PGPASSWORD', pwd)
    os.environ['PGPASSWORD'] = pwd
    dropdb_cmd = "dropdb -U {} -w --if-exists {}".format(db_name)
    createdb_cmd = "createdb -U {} -w -O {} --if-exists {}".format(db_name)
    restore_cmd =
    for datebase in db_list:
        backup_name = file_prefix + '_' + datebase + '.backup'
        backup_cmd = "pg_dump -U {} -w -f {}{} {}".format(user, file_path, backup_name, datebase)
        if os.system(backup_cmd):
            writeLogs(log_path, "Backup database failed!\n")
        else:
            writeLogs(log_path, "Backup *{}* completed.\n".format(datebase))
    return True

# 文件夹备份函数
def fileBackup(directory, file_path, file_prefix):
    backup_name = file_prefix + '_filestore.zip'
    # make sure you install 7-zip in windows and add it into system path.
    zip_cmd = "7z a {}{} -r {}".format(file_path, backup_name, directory)
    if os.system(zip_cmd):
        writeLogs(log_path, "Backup filestore failed!\n")
        return False
    else:
        writeLogs(log_path, "Backup #filestore# completed.\n")
        return True


def main():
    '''
    speciafied for central hub company.
    system information: windows server 2008.
    datetime:2016-11-02
    target software: odoo 10 enterprise
    '''
    writeLogs(log_path, "-"*79 + "\nOperation time: {}\n".format(today_str))
    pgdbBackup(pg_user, pg_pwd, db_names, backup_path, today_file)
    fileBackup(data_dir, backup_path, today_file)
    deleteBackup(backup_path, 10)

if __name__ == "__main__":
    main()