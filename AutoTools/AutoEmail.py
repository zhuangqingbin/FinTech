# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-05-08 10:19

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import MAIL_HOST ,MAIL_USER
from config import MAIL_TOKEN, SENDER, RECEVIERS
from config import SENDER_NAME, RECEVIER_NAME
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""

class EMAIL:
    def __init__(self, mail_host = MAIL_HOST, mail_user = MAIL_USER,
                 mail_token = MAIL_TOKEN, sender = SENDER,
                 receivers = RECEVIERS, sender_name = SENDER_NAME,
                 receiver_name = RECEVIER_NAME):
        self.__mail_host = mail_host
        self.__mail_user = mail_user
        self.__mail_token = mail_token
        self.sender = sender
        self.receivers = receivers
        self.sender_name = sender_name
        self.receiver_name = receiver_name

        self.connect()

    def connect(self):
        try:
            self.smtpObj = smtplib.SMTP()
            # 发件人邮箱中的SMTP服务器，端口是25
            self.smtpObj.connect(self.__mail_host, 25)  #
            self.smtpObj.login(self.__mail_user, self.__mail_token)
        except:
            self.smtpObj = None

    def send(self,message):
        pass


class LimitUp(EMAIL):

    def __init__(self, title = '每日涨停股快报'):
        super(LimitUp, self).__init__()
        # title邮件名
        self.title = title


    def send(self, message):
        message = MIMEText(message, 'html', 'utf-8')

        # 邮件名
        message['Subject'] = Header(self.title, 'utf-8')
        # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
        message['From'] = Header(self.sender_name, 'utf-8')
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['To'] = Header(self.receiver_name, 'utf-8')

        try:
            self.smtpObj.sendmail(self.sender, self.receivers,
                                  message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


def test(message):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "360650538@qq.com"  # 用户名
    mail_pass = 'velkooyixtgwbgbb'  # 授权码

    sender = '360650538@qq.com'
    receivers = ['360650538@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


    message = MIMEText(message, 'html', 'utf-8')


    message['From'] = Header("量化机器人", 'utf-8')  # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
    message['To'] = Header("终端用户", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    subject = '每日涨停股快报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 发件人邮箱中的SMTP服务器，端口是25
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")