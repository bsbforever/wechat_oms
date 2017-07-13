#!/usr/bin/python
#coding=utf8
import paramiko
def getlinuxcpu(ssh):
    result=[] 
    #这里我们使用sar命令来获取CPU的使用率
    #exec_command可有三个变量可使用
    #stdin代表标准输入
    #stdout为标准输出，即命令输出的结果
    #stderr为错误输出，即执行该命令的错误信息
    stdin,stdout,stderr=ssh.exec_command('sar 2 3 |awk \'END {print 100-$NF}\'')
    #我们首先判断有无错误，如果没有则读出命令结果
    err=stderr.readlines() 
    if len(err) != 0:
        return err
    else:
        stdout_content=stdout.readlines()
    result= stdout_content
    #读出输出的结果后判断是否正确，有时由于超时等原因可能不会返回正确的数值
    try:
        if  len(result) !=0:
            return round(float(result[0].strip()),2)
        else:
            print ('There is something wrong when execute sar command')
    except Exception as e:
        print (e)



def getlinuxmem(ssh):
        result=[]
        stdin,stdout,stderr=ssh.exec_command('free -m |awk \' NR==2 {print (($3 - $6 - $7)/$2)*100}\'')
        err=stderr.readlines()
        if len(err) != 0:
            return err
        else:
            stdout_content=stdout.readlines()
        result= stdout_content
        try:
            if  len(result) !=0:
                return round(float(result[0].strip()),2)
            else:
                print ('There is something wrong when execute free command')
        except Exception as e:
            print (e)

def getlinuxspace(ssh):
        result=[]
        stdin,stdout,stderr=ssh.exec_command('df -h |awk \' NR>1 {if ($1==$NF){printf $1}else{print $0}}\'')
        err=stderr.readlines()
        if len(err) != 0:
            print (err)
        else:
            stdout_content=stdout.readlines()
        result= stdout_content
        try:
            if  len(result) !=0:
                return result
            else:
                print ('There is something wrong when execute df command')
        except Exception as e:
            print (e)


if __name__ == '__main__':
    hostname='10.65.202.201'
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
        result=getlinuxspace(ssh)
        ssh.close()
        for i in result:
            j=i.split()
            print ('The disk usage of '+j[5]+' on '+hostname+' is '+j[4][0:-1]+'% Used')
    except Exception as e:
        print (hostname+' '+str(e))



