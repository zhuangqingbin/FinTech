# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-05-10 20:44

import smtplib
from email.mime.text import MIMEText

msg=MIMEText('Hello','plain','utf-8')
msg['From'] = '发送'
msg['To'] = '接受'
msg['Subject'] = 'fd'

server=smtplib.SMTP_SSL('smtp.qq.com', 465)
# server=smtplib.SMTP('smtp.qq.com',25)

server.login("360650538@qq.com",'velkooyixtgwbgbb')
server.sendmail('360650538@qq.com',['360650538@qq.com'],msg.as_string())
server.quit()

