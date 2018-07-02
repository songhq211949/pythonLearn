'''
Created on 2018年6月19日

@author: Administrator
'''
from ftplib import FTP
import os
ftp=FTP()
ftp.set_debuglevel(2)
ftp.connect("192.168.39.248",21)
ftp.login("testftp","testftp")
print(ftp.getwelcome())
ftp.cwd("checkfilepath")
ftp.dir()
bufsize=1024
filename="E://ftp/30331004111082420180528.txt"
file_handler = open(filename,'wb').write  
#以写模式在本地打开文件   
ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)  
#接收服务器上文件并写入本地文件   
ftp.set_debuglevel(0)   
ftp.quit()   
print("ftp down ok") 