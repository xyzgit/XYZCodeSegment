### 测试包上传说明

1.  生成安装包（Android、iOS）
- 在ftp服务器上新建版本目录，比如：8.2.8，并在此目录中创建子目录packages
- 将第一步生成的安装包上传到子目录packages中
- 修改download.html中的相关配置:
  - 修改title为版本号，如8.2.8
  - 注释掉iOS、Android数组中没有的安装包配置，如全有，省略此操作
- 运行modify-plist.py脚本，修改plist文件对应的ipa配置信息。只有Anroid包可忽略此操作
- 上传html文件到当前版本目录（8.2.8），上传plist文件到第二步创建的子目录packages
