#!/usr/bin/python
#coding=utf8
import cx_Oracle
def oraclesql():
    ipaddress='10.65.1.120'
    username='sys'
    password='ase_sys_n'
    port='1521'
    tnsname='dctest'
    try:
        db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception as e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
        print (content)
    else:
        cursor = db.cursor()
        data=oraclesql(cursor)
        cursor.close()
        db.close()

    cursor.execute('select max(count(*))  from v$open_cursor group by sid')
    data=cursor.fetchone()
    return data


if __name__=="__main__":
    
    result=oraclesql()
    print (result)


