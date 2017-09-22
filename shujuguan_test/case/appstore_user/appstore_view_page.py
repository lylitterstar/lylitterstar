#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from BaseCase.BaseCase import BaseCase
from service.getModeAndExecCase import ModeAndExecCase
from common.variable import GetVariable as common
import unittest
class AppstoreViewPage(BaseCase):


    def appstoreView(self,**kwargs):
        #业务处理部分,file,test_name
        mc = ModeAndExecCase("test_app_store_view",driver=self.driver,reportPath=common.RESULT_PATH)
        # result=mc.execCase(file)
        result=mc.execCaseAndLog(file=kwargs["file"],test_name=kwargs["test_name"])
        # self.assertIsNone(result)

    def test_appstore_view(self):
        file = "appstore/appstoreView.yaml";
        test_name="test_appstore_module_v1"
        self.appstoreView(file=file,test_name=test_name)

    def test_try2(self):
        file = "appstore/appstoreView.yaml";
        test_name = "test_appstore_module_v2"
        self.appstoreView(file=file,test_name=test_name)
        print ('test case 2 try trying!!!!!')

if __name__=="__main__":
   unittest.main()







