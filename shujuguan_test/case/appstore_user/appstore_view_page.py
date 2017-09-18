#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from BaseCase.BaseCase import BaseCase
from common  import help_selenium as help
from common import operateYaml
from common.operateElement import OperateElement
from service.getModeAndExecCase import ModeAndExecCase
from testMode.modeCase import GetCase,GetCaseInfo
import unittest
class AppstoreViewPage(BaseCase):

    def appstoreView(self):
        #业务处理部分
        modeAndExec=ModeAndExecCase(driver=self.driver,GetCaseInfo=GetCaseInfo(),GetCase=GetCase())
        result=modeAndExec.execCase("appstore/appstoreView.yaml")
        self.assertIsNone(result)

    def test_appstore_view(self):
        self.appstoreView()

    # def test_try2(self):
    #     print ('test case 2 try trying!!!!!')

if __name__=="__main__":
   unittest.main()







