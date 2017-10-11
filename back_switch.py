__author__ = '42274'
#encoding=utf-8
import telnetlib
import time
import datetime
import os
def switch(hostname,username,password1,password2,cmd1,cmd2):
    tn = telnetlib.Telnet(hostname,timeout=10)
    #tn.set_debuglevel(2)
    tn.read_until("Username: ")
    tn.write(username + "\n")
    tn.read_until("Password: ")
    tn.write(password1 + "\n")
    tn.read_until(">")
    tn.write('en'+ "\n")
    tn.read_until("Password: ")
    tn.write(password2 + "\n")
    tn.read_until("#")
    tn.write("terminal length 0"+"\n")
    tn.write(cmd1 + "\n")
    tn.write(cmd2 + "\n")
    #tn.read_until("#")
    tn.write("exit\n")
    result=tn.read_all()
    #print tn.read_all()
    return result
if __name__ == '__main__':
   # hostname = "10.65.5.1"
    username = 'file'
    password1='password1'
    password2='password2'
    cmd1='show run'
    cmd2='show version'
    file = open("g:\swbackup\ipaddress.txt")
    ipaddress=file.readlines()
    for hostname  in ipaddress:
        hostname=hostname.strip()
        now = datetime.datetime.now()
        dirname=hostname
        #dirname="%.2i%.2i%.2i" % (now.year,now.month,now.day)
        filename_prefix='SWB_'+hostname
        filename = "%s_%.2i%.2i%.2i%.2i%.2i%.2i" % (filename_prefix,now.year,now.month,now.day,now.hour,now.minute,now.second)+'.txt'
        #filename = "%s_%.2i%.2i%.2i" % (filename_prefix,now.hour,now.minute,now.second)+'.txt'
        result=switch(hostname,username,password1,password2,cmd1,cmd2)
        base='g:\\swbackup\\'
        path=base+dirname+'\\'
        ifExists=os.path.exists(path)
        if not ifExists:
            os.makedirs(path)
        else:
            pass
        backfile=path+filename
        fp=open(backfile,"w")
        fp.write(result)
        fp.close()
