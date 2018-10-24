#!/usr/local/env python
# -*- coding utf-8 -*-

import smtplib
import string

HOST = "smtp.qq.com"
SUBJECT = "test email from Python"
TO = "flyxewlh@163.com"
FROM = "466874819@qq.com"
text = "Python rules them all"
BODY = string.join(("From:%s" % FROM,"To: %s" % TO,"Subject: %s" % SUBJECT,"",text),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls("466874819@qq.com","")
server.sendmail(FROM,[TO],BODY)
server.quit()

