#coding:utf-8
__author__='dushanshan'
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
a=os.path.dirname(__file__)
print('a,',a)
import sys
sys.path.append("../..")
from common  import help_selenium as help
from page.test_login_page import test_login_page
from common.operateFile import OperateFile
class BaseCase(unittest.TestCase):
    global op
    #登陆
    def setUp(self):
        # op=OperateFile()
        # op.initExcel()
        self.driver=help.browser()
        # 读取配置文件-----以后设置成
        file = "login/login.yaml"
        rr=os.getcwd()
        testLogin=test_login_page(self.driver,file)
        testLogin.test_login()
    def test_ll(self):
        print "test is running!"

    def tearDown(self):
        self.driver.quit()





if __name__=="__main__":
    print("test")
    print(os.getcwd())
    print(os.path.join(os.path.dirname(os.getcwd()),"yaml/login/login.yaml"))
    unittest.main()






