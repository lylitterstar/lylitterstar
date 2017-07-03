#　-*- coding: utf-8 -*-
import commands
import sys
import logging
import os
import signal
import psutil
import subprocess
import time




def getPid(process):
    cmd = "ps -ef | grep '%s' " % process
    logging.info(cmd)
    info = commands.getoutput(cmd)
    infos = info.split()
    if len(infos) > 1:
        print(infos)
        return infos[1]
    else:
        return -1


def getPid2(process):
    cmd = "ps aux| grep '%s'|grep -v grep " % process
    logging.info(cmd)
    out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    infos = out.stdout.read().splitlines()
    pidlist = []
    if len(infos) >= 1:
        for i in infos:
            pid = i.split()[1]
            if pid not in pidlist:
                pidlist.append(pid)
        return pidlist
    else:
        print('process has yet not exsit')
        return -1



def kill(pid):
    try:
        print('into process:')
        print(pid)
        a=os.kill(pid, signal.SIGKILL)
        print(a)
        #a = os.kill(pid, 9) 
        print ('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))
      #  print ('已杀死pid为%s的进程,　' % (pid))
    except OSError as e:
        print ('没有如此进程!!!')

def kill2(pid,proc):
    out=os.system('kill'+pid)
    if out==0:
        print('success! kill '+pid+' '+proc)
    else:
        print('failed! kill '+pid+' '+proc)

def processinfo(processName):
	pids = psutil.pids()
	for pid in pids:
		p = psutil.Process(pid)
		if p.name() == processName:
			print(pid)
			return True    #如果找到该进程则打印它的PID，返回true
	return False		       #没有找到该进程，返回false




def cmd_run(cmd):
    subprocess.call(cmd, shell=True)


if __name__=="__main__":

    #start jmeter
    #cmd='/opt/apache-jmeter-3.1/bin/jmeter.sh'
    #windows location
    cmd="F:/apache-jmeter-3.1/bin/jmeter.bat"
    cmd_run(cmd)
    #p=getPid2('ApacheJMeter')

  
