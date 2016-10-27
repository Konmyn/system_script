#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

git_paths = ["/home/ethan/workspace/project/odoo/odoo",
             "/home/ethan/workspace/project/odoo/enterprise",
             "/home/ethan/workspace/project/odoo/kresta",
             "/home/ethan/workspace/project/odoo/kalisign",
             ]
# pay attention to the slash in the dir end.
log_path = "/home/ethan/workspace/project/script/"
log_name = "auto_git_pull.log"

os.system("date >> {}{}".format(log_path, log_name))
for git_path in git_paths:
    os.chdir(git_path)
    os.system("git pull >> {}{}".format(log_path, log_name))
