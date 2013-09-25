#coding: utf-8
import os
def walk_dir(dir,topdown=True):

	lines = 0

	#遍历目录,统计目录下所有文件行数
	for root,dirnames,filenames in os.walk(dir,topdown):
		for name in filenames:
			filepath = os.path.join(root,name)
			file = open(filepath)
			count = len(file.readlines())
			#print(name + ' lines: ' + str(count))
			file.close()
			lines += count
	print(lines)

dir = r'F:\distDir'
walk_dir(dir)
