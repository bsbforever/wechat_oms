#!/usr/bin/python
#coding=utf8
import cx_Oracle
from sendmail_phone import *
def oraclesql(cursor):
    #这里我们使用python的open方法打开文件并读取文件内容作为SQL语句执行
    #可使用绝对路径或相对路径
    fp=open('/home/oracle/script/tablespace.sql','r')
    #fp=open('./tablespace.sql','r')
    fp1=fp.read()
    cursor.execute(fp1)
    data=cursor.fetchall()
    return data


if __name__=="__main__":
    mailcontent=[] 
    ipaddress='10.65.1.120'
    username='sys'
    password='ase_sys_n'
    port='1521'
    tnsname='dctest'
    #这里我们利用Python的异常处理来捕获异常，具体用法请参考文章开始提到的教程
    try:
        #这里我们使用sysdba权限连接oracle数据库(和上期连接普通用户的不同)
        db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception as e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
        print (content)
    else:
        cursor = db.cursor()
        data=oraclesql(cursor)
        cursor.close()
        db.close()
        #这里我们检查每个表空间使用率是否大于90%，如果是则将一条报警信息加入到mailcontent列表
        for i in data:
            usage=int(i[4])
            if usage>=90:
                tablespace=i[0]
                mailcontent.append('Be Careful tablespace '+tablespace+' is '+str(usage)+'% Used!')
        #这里我们判断mailcontent长度是否为0，不为0说明有超过90%的表空间，然后我们发送邮件
        if len(mailcontent) != 0:
            content='\n'.join(mailcontent)
            send_mail(to_list,' Tablespace usage warnning',content)
        

