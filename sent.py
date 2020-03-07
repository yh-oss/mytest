import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase #附件
from email.mime.text import MIMEText
from email import encoders #转码
from datetime import date
from email.header import Header
import sys,socket
import getpass
import time

def getToday():
    today = date.today()
    date_today = today.strftime("%m%d")
    return date_today

def server(msg):
    #服务器
    mail_host = "smtp.qq.com"
    mail_user = "563811563@qq.com"
    mail_pass = "irwfnnyersyfbbfg"

    server = "563811563@qq.com"
    #receiver = ["1621680732@qq.com"]
    receiver = ["563811563@qq.com"]
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host,25)
        smtpobj.login(mail_user,mail_pass)
        smtpobj.send_message(msg)
        print("邮件发送成功")
    except smtplib.SMTPException:
        print('Error:发送失败！')


    

def send():
    #创建带附件实例
    for x in ('txt','doc','docx','png','rar'):
        message = MIMEMultipart()
        message['From'] = "563811563@qq.com"
        #message['To'] = "1621680732@qq.com"
        message['To'] = "563811563@qq.com"
        subject = "Python SMTP 邮件"+getToday()
        message['Subject'] = Header(subject,'utf-8')
        message.attach(MIMEText(host_computer()))
        with open ("D:\\大四下_"+x+".zip",'rb') as f:
            letter = MIMEBase('zip','zip',filename="大四下_"+x+".zip")
            letter.add_header('Content-Disposition','attachment',filename=('gb2312', '', "大四下_"+x+".zip"))
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
