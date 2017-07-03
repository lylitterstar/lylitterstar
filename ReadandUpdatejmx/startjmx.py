#　-*- coding: utf-8 -*-
from ReadandUpdatejmx import readJmxScript as jmx,updateCSV as csv
import subprocess
import os
import time
import readResponseTime as resTime
import readJmxScript as rjmx
class StartJmx():
    def __init__(self):
        try:
            #csv file update
            sessionID=input("Enter String type  PHPSessionID:")
            csvFilepath=input("Enter String type  csvFilepath:")

            csv.readandUpdateCSV(csvFilepath,sessionID)
            #jmx file update
            num_threads=input("Enter String type  num_threads:")
            ramp_time=input("Enter String type  ramp_time:")
            duration=input("Enter String type  duration:")
            jmx.updateJmx(num_threads,ramp_time,duration)
        except Exception as e:
            print("exception info is:",e)

def kill_jmeter(self):
    pass
# exec shell
def cmd_run(cmd):
    subprocess.call(cmd, shell=True)

def startJmx():
    try:
        f=open("./verifysum/configData/env.txt",'r')
        lines=f.readlines();
        env={}
        for line in lines:
            line=line.strip("\n")
            s=line.split(",")
            env[s[0]]=s[1]
    finally:
        f.close()
    try:

        absCsvFilepath=env.get("absCsvFilepath")
        absJmxScriptPath=env.get("absJmxScriptPath")
        jmeterPath=env.get("jmeterPath")
        #csv file update
        sessionID=input("Enter String type  PHPSessionID:")
        #csvFilepath=input("Enter String type  csvFilepath:")
        #now is solid csv
        csvFilepath="verify.csv"
        csvFilepath='shijue.csv'
        csvFilepath=absCsvFilepath+str(csvFilepath)
        csv.readandUpdateCSV(csvFilepath,sessionID)
        #jmx file update
        jmxScriptPath=input("Enter jmx  script file like 'a.jmx':")
        num_threads=input("Enter String type  num_threads:")
        num_threads=str(num_threads)
        ramp_time=input("Enter String type  ramp_time:")
        ramp_time=str(ramp_time)
        duration=input("Enter String type  duration:")
        duration=str(duration)
        #out name add time flag
        time1 = time.time()
        time2= time.localtime(time1)
        strTime=time.strftime("%Y-%m-%d-%H-%M-%S", time2)
        outPutName=jmxScriptPath+"_"+num_threads+"_"+strTime+".jtl"
        jmxScriptPath=absJmxScriptPath+str(jmxScriptPath)
        jmx.updateJmx(jmxScriptPath,num_threads,ramp_time,duration)
        elementName = 'HTTPSamplerProxy'
        atrrName = 'testname'
    except Exception as e:
        print("exception info is:",e)


    #jmx file path :jmxScriptPath
    # temp don`t use this way
    #cmd=jmeterPath+" -n -t "+jmxScriptPath+" -l "+"./sjgsum/jmxReport/listener.jtl"+" -e -o  ./sjgsum/jmxReport/report"
    cmd = jmeterPath + " -n -t " + jmxScriptPath + " -l " + "./verifysum/jmxReport/"+outPutName
    print('cmd:'+cmd)
    cmd_run(cmd)
    resTimePath="./verifysum/jmxReport/"+outPutName
    allWords = resTime.tryReadTime(resTimePath)
    #read lable
    label=rjmx.findNodesbyValue(jmxScriptPath,elementName,atrrName)
    #get response time
    # outTime=resTime.mulTypeTime(resTimePath, label)
    # print('90% requests time is', outTime)
    outTime = resTime.mulTypeTime(resTimePath, label)
    outTime2 = resTime.countTime(resTime.tryReadTime(resTimePath))
    print('90% requests time is', outTime, outTime2)


if __name__=="__main__":
    print('now start:')
    #start method
    # startJmx()
    jmxScriptPath='./verifysum/verify_home_page.jmx'
    # # resTimePath="/home/dushanshan/桌面/tesd7.jtl"
    resTimePath='./verifysum/home1.jtl'
    resTimePath='./verifysum/jmxReport/verify_home_page.jmx_20_2017-06-21-13-54-14.jtl'
    elementName = 'HTTPSamplerProxy'
    atrrName = 'testname'
    label = rjmx.findNodesbyValue(jmxScriptPath, elementName, atrrName)
    print('length',len(label))
    print('type',type(label))
    #suggest this method
    outTime = resTime.mulTypeTime(resTimePath, label)
    outTime2=resTime.countTime(resTime.tryReadTime(resTimePath))
    print('90% requests time is', outTime,outTime2)














