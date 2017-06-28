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
    #这里打开oracle_list文件并读取其中内容 
    file1=open(r"/home/oracle/script/oracle_list.txt")
    oracle_list=file1.readlines()
    file1.close()
    #循环读取每行的内容并使用split函数获取到相关数据库信息
    for i in oracle_list:
        info=i.split()
        ipaddress=info[0].strip()
        username=info[1].strip()
        password=info[2].strip()
        port=info[3].strip()
        tnsname=info[4].strip()
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception as e:
            content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
            mailcontent.append(content)
        else:
            cursor = db.cursor()
            data=oraclesql(cursor)
            cursor.close()
            db.close()
            for i in data:
                usage=int(i[4])
                if usage>=90:
                    tablespace=i[0]
                    mailcontent.append('Be Careful tablespace '+tablespace+' on '+tnsname+' is '+str(usage)+'% Used!')
        #这里我们判断mailcontent长度是否为0，不为0说明有超过90%的表空间，然后我们发送邮件
    if len(mailcontent) != 0:
        content='\n'.join(mailcontent)
        send_mail(to_list,' Tablespace usage warnning',content)
        

