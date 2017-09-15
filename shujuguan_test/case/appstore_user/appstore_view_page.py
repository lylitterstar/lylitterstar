#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from BaseCase.BaseCase import BaseCase
from common  import help_selenium as help
from common import operateYaml
from common.operateElement import OperateElement
class AppstoreViewPage(BaseCase):

    def appstoreView(self):
        operateElement=OperateElement(self.driver)
        helpUtils = help.Help(self.driver)
        #业务处理部分
        data_appstore_view = operateYaml.getYaml("appstore/appstoreView.yaml")
        result=None
        for k in data_appstore_view:
            if k.get("operate_type") != None:
                result=operateElement.operate_element(k)
                if result==False:
                    self.assertFalse(result)
                    break

        print("test_app_view:"+str(data_appstore_view))
        self.assertIsNone(result)
        # self.assertEqual(data_appstore_view[0].get("test_intr"),"应用市场")

    def test_appstore_view(self):
        self.appstoreView()

    # def test_try2(self):
    #     print ('test case 2 try trying!!!!!')
    #放置在基类中，后续要是没有问题，可以删掉该代码
    # def tearDown(self):
    #     self.driver.quit()

if __name__=="__main__":
    unittest.main()






