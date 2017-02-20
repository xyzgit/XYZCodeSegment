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

pattern = r"lakala/[^<]+<"

#Android替换内容
replformat = "lakala/feature_test_package/resources/{0}/{1}<"

first_arg = dir_name

#iOS替换内容
if 'packages' == dir_name:
    replformat = "lakala/{0}/packages/{1}<"
    first_arg = title

ipa_array = [
    '%e6%8b%89%e5%8d%a1%e6%8b%89_%e6%b5%8b%e8%af%95.ipa',
    '%e6%8b%89%e5%8d%a1%e6%8b%89_%e6%b5%8b%e8%af%95%e5%a4%96%e7%bd%91.ipa',
    '%e6%8b%89%e5%8d%a1%e6%8b%89_%e5%a4%87%e6%9c%ba.ipa',
    '%e6%8b%89%e5%8d%a1%e6%8b%89_%e7%94%9f%e4%ba%a7.ipa'
]

files = ['ce_shi.plist', 'ce_shi_wai_wang.plist', 'beiji.plist', 'shengchan.plist']
for index, filename in enumerate(files):
    ipa = ipa_array[index]
    repl = replformat.format(first_arg, ipa)
    modify_file(filename, pattern,repl)

print('modify complete')
