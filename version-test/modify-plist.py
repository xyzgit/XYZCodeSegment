# -*- coding: utf-8 -*-
import fileinput, re, os

def modify_file(file_name, pattern, repl):
    fp = open(file_name, 'r')
    lines = fp.readlines()
    fp.close()

    fp = open(file_name, 'w')
    for line in lines:
        s = re.sub(pattern, repl, line)
        fp.writelines(s)
    fp.close()

#从当前目录得到唯一的html文件名称
html_file = os.popen('echo *.html').read().replace('\n', '')

# 从html文件中，筛选出安装包的目录名称
dir_name = ''
title = ''
for line in fileinput.input(html_file):
    if 'title:' in line:
        str_array = line.split('"')
        title = str_array[1]

    if 'dirName:' in line:
        str_array = line.split('"')
        dir_name = str_array[1]

pattern = r"lakala/[^/]+/[^/]+/"
repl = "lakala/" + title + '/' + dir_name + "/"

files = ['ce_shi.plist', 'ce_shi_wai_wang.plist', 'beiji.plist', 'shengchan.plist']
for file in files:
    modify_file(file, pattern,repl)

print('modify complete')
