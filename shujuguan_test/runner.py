#coding=utf-8
__author__='dushanshan'

import unittest
import os
import HTMLTestRunner
import time
#用例路径
case_path=os.path.join(os.getcwd(),"case")
#报告存放路径
report_path=os.path.join(os.getcwd(),"report")
#生成TestSuite
def allCase():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='appstore*.py',top_level_dir=None)
    print('discover=',discover)
    return discover
#run
def runTextAllCase():
    runner = unittest.TextTestRunner()
    runner.run(allCase())
def runHTMLAllCase():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    reportPath=os.path.join(report_path,"HTMLtemplate_"+now+".html")
    print(reportPath)
    fp=open(reportPath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='自动化测试报告：',
                                           description='用例执行情况：')
    fp.close()
    runner.run(allCase())

if __name__=="__main__":
    # runTextAllCase()
    runHTMLAllCase()

