# coding: UTF-8
import os,sys

#判断是否有命令行传入参数
if len(sys.argv) < 2:
	dirPath = os.path.dirname(os.path.abspath(__file__))
else:
	dirPath = os.path.abspath(sys.argv[1])
	
if len(sys.argv) == 3:
	distPath = os.path.abspath(sys.argv[2])
else:
	distPath = "fileList.txt"

basedeep = dirPath.count('\\')	#记录当前查找的目录深度

print basedeep
print dirPath

outputFile = open(distPath,'w')	#打开文件用于打印目录结构

#统计文件个数
fileCount = 0

#用walk函数遍历文件夹
for root,dirs,files in os.walk(dirPath):

	#计算当前目录的深度
	deep = os.path.abspath(root).count('\\') - basedeep

	#输出当前所遍历的文件夹名称，' '*dieLevel表示缩进
	outputFile.writelines(' ' * deep * 2
		+ '/' + os.path.basename(root)+'\n')

	#对文件夹下的每一个文件名称进行输出
	for file in files:
		#写文件
		outputFile.writelines(' ' * (deep+1) * 2 + file +'\n')

		fileCount += 1
		
#关闭文件
outputFile.close()

print fileCount
