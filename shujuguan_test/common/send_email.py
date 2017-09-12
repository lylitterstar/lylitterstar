#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    smtpserver='mail.sina.com'
    # 发送邮箱用户名/密码
    user = 'ssdu1023@sina.com'
    password = 'du123456'
    # 发送邮箱
    sender = 'ssdu1023@sina.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
    receiver = ['ssdu1023@sina.com']
    # 发送邮件主题
    subject = '自动化测试报告'

    msg = MIMEMultipart('mixed')

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="HTMLtemplate_2017_09_12 15_36_59.html"'
    msg.attach(msg_html)



    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163设置授权码（即客户端的密码），否则会报535
    msg['From'] = 'XXXX@163.com'
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
