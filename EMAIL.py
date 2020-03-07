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

def fsend(data):
        today = date.today()
        date_today = today.strftime("%m%d")
    
        message = MIMEMultipart()
        message['From'] = "563811563@qq.com"
        #message['To'] = "1621680732@qq.com"
        message['To'] = "563811563@qq.com"
        subject = "Python SMTP 邮件"+date_today
        message['Subject'] = Header(subject,'utf-8')
        message.attach(MIMEText(data))
        with open (data,'rb') as f:
            letter = MIMEBase('zip','zip',filename=data)
            letter.add_header('Content-Disposition','attachment',filename=('gb2312', '', data))
            letter.add_header('Content-ID','<0>')
            letter.add_header('X-Attachment-Id','0')
            letter.set_payload(f.read())
            encoders.encode_base64(letter)
            message.attach(letter)
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
            smtpobj.send_message(message)
            print("邮件发送成功")
        except smtplib.SMTPException:
            print('Error:发送失败！')