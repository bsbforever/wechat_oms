#!/usr/bin/python
#coding=utf8
import paramiko
def getunixspace(ssh):
        result=[]
        stdin,stdout,stderr=ssh.exec_command('bdf |awk \' NR>1 {if ($1==$NF){printf $1}else{print $0}}\'')
        err=stderr.readlines()
        if len(err) != 0:
            print (err)
            return False
        else:
            stdout_content=stdout.readlines()
        result= stdout_content
        try:
            if  len(result) !=0:
                return result
            else:
                print ('There is something wrong when execute unix bdf command')
        except  Exception as e :
            print (e)


def getunixcpu(ssh):
        result=[]
        stdin,stdout,stderr=ssh.exec_command('sar 1 3 |awk \'END {print 100-$NF }\'')
        err=stderr.readlines()
        if len(err) != 0:
            print (err)
            return False
        else:
            stdout_content=stdout.readlines()
        result= stdout_content
        try:
            if  len(result) !=0:
                return round(float(result[0].strip()),2)
            else:
                print ('There is something wrong when execute unix sar command')
        except Exception as e:
            print (e)
def getunixmem(ssh):
        result=[]
        stdin,stdout,stderr=ssh.exec_command('swapinfo -tam | awk \'END { print $5}\'')
        err=stderr.readlines()
        if len(err) != 0:
            print (err)
            return False
        else:
            stdout_content=stdout.readlines()
        result= stdout_content
        try:
            if  len(result) !=0:
                return round(float(result[0].strip()[0:-1]),2)
            else:
                print ('There is something wrong when execute unix swapinfo command')
        except Exception as e:
            print (e)
if __name__ == '__main__':
    hostname='10.60.14.51'
    username='root'
    #password='nstx147)'
    password='password'
    try:
        #使用SSHClient方法定义ssh变量
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接目标服务器
        ssh.connect(hostname=hostname,port=22,username=username,password=password)
        #调用getlinuxcpu函数获得服务器CPU使用率
        result=getunixcpu(ssh)
        ssh.close()
        if result:
           print (result)
    except Exception as e:
        print (hostname+' '+str(e))



