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
class BaseCase(unittest.TestCase):
    # def __init__(self):
    #     # self.driver=driver
    #     #修改为读取配置文件
    #     loginUrl="https://shujuguan.shujuguan.cn/login"
    #     self.driver.get(loginUrl)
    #登陆
    def setUp(self):
        self.driver=help.browser()
        loginUrl = "https://shujuguan.shujuguan.cn/login"
        self.driver.get(loginUrl)
        testLogin=test_login_page(self.driver)
        testLogin.test_login()





if __name__=="__main__":
    b=BaseCase("dt")
    print("test")





