import os
import sys
import win32com.client

#import Crypto

passwd=[]
passwd_dir = "D:\\"
dic = open(passwd_dir+"newfile.txt","r")
data=dic.readline()
while data:
    passwd.append(data)
    data=dic.readline().strip('\n')
dic.close()
wps1=win32com.client.Dispatch('Kwps.application')
#print(type(wps1))
wps1.Visible=0
wps1.DisplayAlerts = 0
for i in passwd:
    #print(i)
    try:
        b = wps1.Documents.Open('D:\\a.docx','r',PasswordDocument="01234567")
           
    except :
        print(i)
    print("succcccceesss:"+i)
    