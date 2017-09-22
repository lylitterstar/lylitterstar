#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
from common  import help_selenium as help
from service import getModeAndExecCase as getModeandExec
from common.variable import GetVariable as common
class test_login_page():

    def __init__(self,driver,file):
        self.driver=driver
        self.file=file
        self.test_module="test_login"
        # self.mc = getModeandExec.ModeAndExecCase("test_login",GetCaseInfo=GetCaseInfo(), GetCase=GetCase(),driver=self.driver)
        self.mc = getModeandExec.ModeAndExecCase(self.test_module, driver=self.driver,reportPath=common.RESULT_PATH)

    def login(self):
        # self.mc.execCase(self.file)
        self.mc.execCaseAndLog(self.file,test_name="test_login_module")

    def dprint(self):
        print("this is trying the two case !!!!!")

    def test_login(self):
        self.login()
        # self.dprint()





if __name__=="__main__":
    driver = help.browser()
    file = "login/login.yaml"
    testLoginPage=test_login_page(driver=driver,file=file)
    testLoginPage.test_login()
    driver.quit()




