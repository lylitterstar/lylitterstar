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
from common import operateYaml
class BaseCase(unittest.TestCase):
    #登陆
    def setUp(self):
        self.driver=help.browser()
        #读取配置文件
        rr=os.getcwd()
        print("test==",rr)
        data_login_element=operateYaml.getYaml("login/login.yaml")
        loginUrl=data_login_element[0]["url"]
        self.driver.get(loginUrl)
        testLogin=test_login_page(self.driver,data_login_element)
        testLogin.test_login()

    def tearDown(self):
        self.driver.quit()





if __name__=="__main__":
    print("test")
    print(os.getcwd())
    print(os.path.join(os.path.dirname(os.getcwd()),"yaml/login/login.yaml"))





