#!/usr/bin/python
#coding=utf8
import cx_Oracle
import pymysql
from sendmail_phone import *

def getindex(oracle_cursor):
    fp=open('/home/oracle/script/getindex.sql','r')
    fp1=fp.read()
    s=oracle_cursor.execute(fp1)
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
    password='ase_sys_n'
    port='1521'
    tnsname='dctest'
    #这里我们利用Python的异常处理来捕获异常，具体用法请参考文章开始提到的教程
    try:
        #这里我们使用sysdba权限连接oracle数据库(和上期连接普通用户的不同)
        oracle = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception as e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
        print (content)
    else:
        oracle_cursor = oracle.cursor()
        data=getindex(oracle_cursor)
        oracle_cursor.close()
        oracle.close()

     
        mysql = pymysql.connect("localhost","root","Oracle@123","oracle" )
        mysql_cursor = mysql.cursor()
        for index in data:
            checkifexist='select count(*) from oracle_indexmonitor where index_name=\''+index+'\''
            mysql_cursor.execute(checkifexist)
            count = mysql_cursor.fetchone()
            if int(count[0])==0:
                try:
                    insertsql='insert into oracle_indexmonitor(index_name,ipaddress,tnsname) values(\''+index+'\',\''+ipaddress+'\',\''+tnsname+'\')'
                    mysql_cursor.execute(insertsql)
                    mysql.commit()
                except:
                    mysql.rollback()

        mysql_cursor.close()
        mysql.close()

