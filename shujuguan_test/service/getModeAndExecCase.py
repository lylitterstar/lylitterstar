#coding:utf-8
__author__='dushanshan'
import sys
import json
sys.path.append("..")
from common import operateYaml
from common.operateElement import OperateElement
from testMode.modeCase import GetCase,GetCaseInfo
class ModeAndExecCase():
    def __init__(self,test_module="",**kwargs):
        print(kwargs.keys())
        self.test_module=test_module
        # self.GetCaseInfo=kwargs["GetCaseInfo"]
        # self.GetCase=kwargs["GetCase"]
        self.driver=kwargs["driver"]
        self.GetCaseInfo=GetCaseInfo()
        self.GetCase=GetCase()
    def getModeList(self,file):
        bs=[]
        listData=operateYaml.getYaml(file)
        for i in range(len(listData)):
            if i==0:
                # 用例id
                self.GetCaseInfo.test_id =listData[i].get("test_id", "false")
                # 用例介绍
                self.GetCaseInfo.test_intr = listData[i].get("test_intr", "false")
            self.GetCase.element_info = listData[i].get("element_info", "false")
            self.GetCase.url = listData[i].get("url", "false")
            # 操作类型
            self.GetCase.operate_type = listData[i].get("operate_type", "false")
            self.GetCase.index = listData[i].get("index", "false")
            self.GetCase.text = listData[i].get("text", "false")  # 输入的text
            # 验证类型
            self.GetCase.find_type = listData[i].get("find_type", "false")
            bs.append(json.loads(json.dumps(self.GetCase.to_primitive())))
        return bs
    def execCase(self,file):
        #获取数据模型
        dataMode=self.getModeList(file)
        if dataMode[0].get("url")!="false":
            self.driver.get(dataMode[0].get("url", "false"))

        # 操作元素对象
        operateElement = OperateElement(self.driver)
        result = None
        for k in dataMode:
            if k["operate_type"] != "false":
                result = operateElement.operate_element(k)
                if result == False:
                    break
        return result


if __name__=="__main__":
    getCase=GetCase()
    getCaseInfo=GetCaseInfo()
    mc=ModeAndExecCase(GetCaseInfo=GetCaseInfo(),GetCase=GetCase())
    f="/home/dushanshan/git/lilytao5_python/python/shujuguan_test/case/yaml/login/login.yaml"
    data=mc.getModeList(f)
    print("return data :\n"+str(data))
