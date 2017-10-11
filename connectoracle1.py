#!/usr/bin/python
#coding=utf8
import cx_Oracle
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
        #由于上面获取的是一个列表(多行)，这里使用for循环来遍历
        #注意i也是一个列表
        print ('表空间名称 总大小(M) 已使用(M) 剩余空间(M) 使用率')
        for i in data:
            print (i[0])



