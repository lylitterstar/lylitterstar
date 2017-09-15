#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from common  import help_selenium as help
from selenium.webdriver.common.keys import Keys
import time
from common import operateYaml
from common.operateElement import OperateElement

class test_login_page():
    # Get username textbox and input username
    def __init__(self,driver,data_login_element):
        self.driver=driver
        self.operateElement=OperateElement(self.driver)
        self.data_login_element=data_login_element
    #　可删掉，该方法
    def set_username(self):
        name=self.driver.find_element_by_id('username')
        name.clear()
        name.send_keys(self.username)

    # Get password textbox and input password, then hit return
    def set_password(self):
        pwd=self.driver.find_element_by_id('password')
        pwd.clear()
        pwd.send_keys(self.password+Keys.RETURN)
        time.sleep(10)

    def login(self):
        for k in self.data_login_element:
            if k.get("operate_type") != None:
                self.operateElement.operate_element(k)

    def test_login(self):
        self.login()



if __name__=="__main__":
    testLoginPage=test_login_page()




