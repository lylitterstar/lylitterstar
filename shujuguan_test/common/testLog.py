#coding:utf-8
__author__='dushanshan'

import os
import time
import logging
import traceback
import threading
class Log:
    def __init__(self):
        global logger,resultPath,logPath
        resultPath="/home/dushanshan/git/webResult"
        logPath=os.path.join(resultPath,(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())))
        if os.path.exists(logPath)==False:
            os.makedirs(logPath)
        self.checkNo=0
        self.logger=logging.getLogger("SJG test result ")
        self.logger.setLevel(logging.INFO)
        #create handler,write log
        fh=logging.FileHandler(os.path.join(logPath,'out.log'))
        #Define the output format of formatter handle
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    def getMyLogger(self):
        return self.logger
    def buildStartLine(self,caseNo):
        startLine="------    "+caseNo+"    "+"START"+"    "+"------  "
        self.logger.info(startLine)
    def buildEndLine(self,caseNo):
        endLine="------    "+caseNo+"    "+"END"+"    "+"------  "
        self.logger.info(endLine)
        self.checkNo=0
    def writerResult(self,result):
        reportPath=os.path.join(logPath,"report.txt")
        flogging=open(reportPath,"a")
        try:
            flogging.write(result+"\n")
        except IOError,e:
            traceback.print_exc()
        finally:
            flogging.close()
    def resultOK(self,caseNo):
        self.writerResult(caseNo+"OK")

    def resultNG(self,caseNo,reason):
        self.writerResult(caseNo+":NG--"+reason)

    def checkPointOK(self,driver,caseName,checkPoint):
        """
        write the case's checkPoint(OK)
        :param driver:
        :param caseName:
        :param checkPoint:
        :return:
        """
        self.checkNo+=1
        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+checkPoint+": OK")
        #take shot
        self.screenshotOK(driver, caseName)
    def checkPointOK(self,driver,caseName,checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": NG")
        # take shot
        self.screenshotNG(driver, caseName)

    def screenshotOK(self,driver,caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_OK.png"
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))


    def screenshotNG(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_NG.png"
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))
class myLog:
    """
    this class is used to get log
    """
    log=None
    mutex=threading.Lock()
    def __init__(self):
        pass
    @staticmethod
    def getLog():
        if myLog.log==None:
            myLog.mutex.acquire()
            myLog.log=Log()
            myLog.mutex.release()
        return myLog.log

if __name__=="__main__":
    logTest=myLog.getLog()
    logger=logTest.getMyLogger()
    logger.debug("ttttt")
    logTest.buildStartLine("test")