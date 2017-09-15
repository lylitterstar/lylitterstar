#coding:utf-8
__author__='dushanshan'
import sys
sys.path.append("..")
testpath2=sys.path
print ('testsys path=',testpath2)
from common import operateYaml
from common.operateElement import OperateElement

class ModeAndExecCase():
    def __init__(self,test_module="",GetCaseInfo="",GetCase=""):
        self.test_module=test_module
        self.GetCaseInfo=GetCaseInfo
        self.GetCase=GetCase
    def getModeList(self,file):
        listData=operateYaml.getYaml("appstore/appstoreView.yaml")
        for i in range(len(listData)):
            if i==0:
                # 用例id
                self.GetCaseInfo.test_id =listData[i].get("test_id", "false")
                # 用例介绍
                self.GetCaseInfo.test_intr = listData[i].get("test_intr", "false")
            self.GetCase.element_info = listData[i].get("element_info", "false")
            self.GetCase.open_url = listData[i].get("get_url", "false")
            # 操作类型
            self.GetCase.operate_type = listData[i].get("operate_type", "false")
            self.GetCase.index = listData[i].get("index", "false")
            self.GetCase.text = listData[i].get("text", "false")  # 输入的text
            # 验证类型
            self.GetWebCase.find_type = listData[i].get("find_type", "false")
        return listData
if __name__=="__main__":
    mc=ModeAndExecCase()
    f="/home/dushanshan/git/lilytao5_python/python/shujuguan_test/case/yaml/login/login.yaml"
    data=mc.getModeList(f)
    print("return data \n"+str(data))
