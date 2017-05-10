#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import re


def file_operation():

    filename = sys.argv[1]
    try:
        f = open(filename, 'r')
        content = f.readlines()
        f.close()
    except IOError as e:
        raise e
        return

    # param should be like --itag=22 or be r/recover if present
    param = sys.argv[2] if len(sys.argv)>2 else ''
    # in case cmd as below:
    # python youtube_wrapper.py youtest.sh
    youget = "you-get '{}'\n"

    # in case cmd as below:
    # python youtube_wrapper.py youtest.sh r
    if param in ['recover', 'r']:
        url_only = re.compile("\'.*\'")
        content = [url_only.search(i).group(0).replace("'", "")+'\n' for i in content]
        with open(filename, 'w') as f:
            f.writelines(content)
        return
    # in case cmd as below:
    # python youtube_wrapper.py youtest.sh --itag=22
    elif re.search("--itag=\d+", param):
        youget = "you-get %s '{}'\n" % param
    # in case cmd as below:
    # python youtube_wrapper.py youtest.sh 22
    elif re.search("\d+", param):
        youget = "you-get --itag=%s '{}'\n" % param

    content = [youget.format(i.strip()) for i in content]
    with open(filename, 'w') as f:
        f.writelines(content)
    return


if __name__ == "__main__":
    file_operation()
