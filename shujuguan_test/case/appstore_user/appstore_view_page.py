#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from BaseCase.BaseCase import BaseCase
from common  import help_selenium as help
from selenium.webdriver.common.by import By
import unittest
class AppstoreViewPage(BaseCase):

    def appstoreView(self):
        helpUtils = help.Help(self.driver)
        element=helpUtils.find_element((By.ID,"appstore"))
        print('type(element),',type(element))
        # print('type(element()),', type(element()))
        self.assertEqual(element.text,"应用市场")

    def test_appstore_view(self):
        self.appstoreView()
    def test_try2(self):
        print ('test case 2 try trying!!!!!')
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    #app=AppstoreViewPage()
    #app.test_appstore_view()
    unittest.main()






