# -*- coding: utf-8 -*-
import os

for dirpath, dirnames, filenames in os.walk("app"):

    for name in filenames:

        filepath = os.path.join(dirpath,name)

        #过滤掉不需要的文件或者目录
        if(name in ['compile.sencha', 'make', 'README']):

            os.remove(filepath)

