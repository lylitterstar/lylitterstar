#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from common  import help_selenium as help
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class test_login_page():
    # Get username textbox and input username
    def __init__(self,driver):
        self.driver=driver
        #读取配置文件
        self.username=(By.ID,'dushanshan@gbase.cn')
        self.password=(By.ID,"123456")

        self.username ='dushanshan@gbase.cn'
        self.password ="123456"
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
    def test_login(self):
        self.set_username()
        self.set_password()






