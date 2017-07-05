#!/usr/bin/python
#coding=utf8
import cx_Oracle
from sendmail_phone import *

def getindex(cursor):
    fp=open('/home/oracle/script/getindex.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    result=[]
    row=s.fetchall()
    for i in row:
        result.append(i[0]+'.'+i[1])
    return result
    #return row

if __name__=="__main__":
    mailcontent=[] 
    ipaddress='10.65.1.120'
    username='sys'
    password='sys_password'
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
        data=getindex(cursor)
        cursor.close()
        db.close()
        for i in data:
            print (i) 

