#!/usr/local/env python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText

_user = "466874819@qq.com"
_pwd  = "hiyrmzwjhehqbjce"
_to   = "flyxewlh@163.com"

#msg = MIMEText('Test Python email测试','plain','utf-8')
msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')
msg["Subject"] = "Python test email"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print("Success!")
except smtplib.SMTPException,e: 
    print ("Falied,%s" %e)

