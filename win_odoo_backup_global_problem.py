# -*- coding: utf8 -*-


import os, datetime


# 创建日志函数
def writeLogs(filename, contents):
    f = file(filename,'a+')
    f.write(contents)
    f.close()
    return True

# 数据库备份函数
def pgdbBackup(pwd, db_list, file_path, file_prefix):
    # 把当前postgreSQL用户的密码写入环境变量
    # os.putenv('PGPASSWORD','admin')
    os.environ['PGPASSWORD'] = pwd
    for datebase in db_list:
        backup_name = file_prefix + '_' + datebase + '.backup'
        backup_cmd = "pg_dump -f {}{} {}".format(file_path, backup_name, datebase)
        if not os.system(backup_cmd):
            message += "Backup for *{}* is success.\n".format(datebase)
        else:
            message += "Backup database failed!!!\n"
    return True

# 文件夹备份函数
def fileBackup(directory, file_path, file_prefix):
    backup_name = file_prefix + '_filestore.zip'
    # make sure you install 7-zip in windows and add it into system path.
    zip_cmd = "7z a {}{} -r {}".format(file_path, backup_name, directory)
    if not os.system(zip_cmd):
        message += "Backup for #filestore# is success.\n"
        return True
    else:
        message += "Backup filestore failed!!!\n"
        return False

# 旧备份文件删除函数
def backupDelete(file_path, term=7):
    prefix = (datetime.datetime.now() - datetime.timedelta(days = term)).strftime("%Y-%m-%d")
    _files = os.listdir(file_path)
    for _file in _files:
        if _file[:len(prefix)] == prefix:
            file_path = os.path.join(file_path, _file)
            try:
                os.remove(file_path)
                message += "Delete success for file: {}\n".format(_file)
            except:
                message += "Delete failed for file: {}\n".format(_file)
    return True

def main():
    '''
    speciafied for central-hub company.
    system information: windows server 2008.
    datetime:2016-11-02
    target software: odoo 10 enterprise
    '''

    # 当前用户(administrator)的postgres登录密码
    pg_pwd = 'admin'
    # 需要备份的数据库列表
    db_names = ['chc','test']
    # 备份文件夹
    backup_path = 'D:\\pgbackup\\'
    # data_dir in odoo.conf and then specified for filestore.
    data_dir = 'D:\\ERP\\data\\filestore\\'
    # log文档的全路径
    log_path = backup_path + 'backup.log'
    message = ''
    # postgres的安装后的执行文件路径，最后加入系统path当中
    # pg_path = r'C:\Program Files\PostgreSQL\9.6\bin\'

    # time related variables
    _now = datetime.datetime.now()
    # 2016-11-02-11-28-21, 用类似这样的格式作为文件前缀
    today_file = _now.strftime("%Y-%m-%d-%H-%M-%S")
    # 2016-11-02 14:47:31, 用类似这样的时间格式作为log信息记录
    today_str = _now.strftime("%Y-%m-%d %H:%M:%S")

    message += "Operation time: {}\n".format(today_str)

    pgdbBackup(pg_pwd, db_names, backup_path, today_file)
    fileBackup(data_dir, backup_path, today_file)
    backupDelete(backup_path, 10)
    writeLogs(log_path, message)

if __name__ == "__main__":
    main()