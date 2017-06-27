#!/usr/bin/python
#coding=utf-8
import smtplib
import os
import time
from email.mime.text import MIMEText
to_list=["<1391111111@139.com>"]
mail_host="10.65.1.134"  #设置服务器
mail_user="ezio_shi"    #用户名
mail_postfix="aseglobal.com"  #发件箱的后缀
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content)    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        #s.set_debuglevel(1)
        s.helo()
        #s.starttls()
        #s.login(mail_user,mail_pass)  #登陆服务器,一般公司内部无需认证
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception as  e:
        print (str(e))
        return False
if __name__ == '__main__':
    #多个收件人请用逗号隔开
    content='这里是发送的内容'
    sub='这里是邮件的标题'
    s=send_mail(to_list,sub,content)
    print (s)



