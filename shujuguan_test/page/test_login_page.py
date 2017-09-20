#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from common  import help_selenium as help
from service import getModeAndExecCase as getModeandExec
class test_login_page():

    def __init__(self,driver,file):
        self.driver=driver
        self.file=file
        # self.mc = getModeandExec.ModeAndExecCase("test_login",GetCaseInfo=GetCaseInfo(), GetCase=GetCase(),driver=self.driver)
        self.mc = getModeandExec.ModeAndExecCase("test_login", driver=self.driver)

    def login(self):
        self.mc.execCase(self.file)

    def test_login(self):
        self.login()



if __name__=="__main__":
    driver = help.browser()
    file = "login/login.yaml"
    testLoginPage=test_login_page(driver=driver,file=file)
    testLoginPage.test_login()
    driver.quit()




