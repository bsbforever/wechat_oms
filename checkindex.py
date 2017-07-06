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

if __name__=="__main__":
    mailcontent=[] 
    ipaddress='10.60.14.70'
    username='sys'
    password='sys_password'
    port='1527'
    tnsname='NP1'
    #首先获取v$sql_plan中的索引名称保存至变量data
    try:
        oracle = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception as e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
        print (content)
    else:
        oracle_cursor = oracle.cursor()
        data=getindex(oracle_cursor)
        oracle_cursor.close()
        oracle.close()
        #接下来连接本地MySQL数据库
        mysql = pymysql.connect("localhost","root","Oracle@123","oracle" )
        mysql_cursor = mysql.cursor()
        #遍历每个索引
        for index in data:
            #首先检查该索引是否存在于数据库中
            checkifexist='select count(*) from oracle_indexmonitor where index_name=\''+index+'\' and ipaddress=\''+ipaddress+'\' and tnsname=\''+tnsname+'\''
            mysql_cursor.execute(checkifexist)
            count = mysql_cursor.fetchone()
            #如结果等于0说明该索引未记录，则插入到MySQL数据库中
            if int(count[0])==0:
                try:
                    insertsql='insert into oracle_indexmonitor(index_name,ipaddress,tnsname) values(\''+index+'\',\''+ipaddress+'\',\''+tnsname+'\')'
                    mysql_cursor.execute(insertsql)
                    mysql.commit()
                except:
                    mysql.rollback()

        mysql_cursor.close()
        mysql.close()

