#!/usr/bin/python
#coding=utf8

#导入cx_Oracle模块
import cx_Oracle

#创建到Oracle数据库的连接并赋给变量
db=cx_Oracle.connect('dcb2b/dcb2b@10.65.1.119:1521/dcprod')

#创建游标并赋给变量cursor
cursor=db.cursor()

#执行Oracle SQL语句
cursor.execute('select sysdate from dual')

#获取执行结果并赋给变量data
#这里fetchone表示获取一行，fetchall为获取所有行
#fetchone返回的是一个字符串
#fetchall返回的是一个列表,哪怕结果只有一行
data=cursor.fetchone()





#打印结果

print ('Database time: %s ' %data)

#关闭数据库连接

cursor.close()
db.close()



