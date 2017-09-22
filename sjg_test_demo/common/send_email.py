#coding:utf-8
__author__='dushanshan'
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import traceback
import os
# 发送邮件，发送最新测试报告html
def email_send(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 关闭文件
    f.close()
    # 发送邮箱服务器
    smtpserver = 'smtp.sina.com.cn'
    # 发送邮箱用户名/密码
    user='ssdu1023@sina.com'
    password="du170143"
    # 发送邮箱
    sender = 'ssdu1023@sina.com'
    # 发送邮件主题
    subject = 'Python SMTP 邮件测试'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
    receivers = ['ssdu1023@sina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEMultipart('mixed')
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    message.attach(msg_html)


    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    # message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    # message['From'] = Header("菜鸟教程", 'utf-8')
    message['From'] ='ssdu1023@sina.com'
    message['To'] = ";".join(receivers)
    message['Subject'] = Header(subject, 'utf-8')

    try:

        smtpObj=smtplib.SMTP()
        smtpObj.connect(smtpserver,25)
        smtpObj.login(user,password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
        smtpObj.quit()
    except smtplib.SMTPException,e:
        print "Error: 无法发送邮件"
        traceback.print_exc()
if __name__=="__main__":
    f=os.path.join( os.path.dirname(os.getcwd()),"report","HTMLtemplate_2017_09_12 15_36_59.html")
    email_send(f)