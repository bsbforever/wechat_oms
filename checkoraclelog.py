#!/usr/bin/python
#coding=utf8
import paramiko

def oraclelog(ssh,path):
        alert_log=[]
        command='grep  -E \'ORA-|Checkpoint|Error\' '+path
        stdin,stdout,stderr=ssh.exec_command(command)
        err=stderr.readlines()
        if len(err) != 0:
            print (err)
            return False
        else:
            stdout_content=stdout.readlines()
        if len(stdout_content)!=0:
            result='\n'.join(stdout_content)
            result= 'Oralce log on '+hostname+ ' have errors\n'+'The log path is '+path+'\n'+result
            alert_log.append(result)
            return alert_log
        else:
            return 'noerror'

if __name__ == '__main__':
    hostname='10.60.14.60'
    username='root'
    password='password'
    try:
        #使用SSHClient方法定义ssh变量
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接目标服务器
        ssh.connect(hostname=hostname,port=22,username=username,password=password)
        path='/oracle/NP1/saptrace/background/alert_NP1.log'
        alert_log=oraclelog(ssh,path)
        ssh.close()
        if alert_log:
            if alert_log !='noerror':
                for i in alert_log:
                    print (i)
            else:
                print ('There is no ORA- error on '+hostname)
    except Exception as e:
        print (hostname+' '+str(e))



