#coding:utf-8
__author__='dushanshan'
import sys
import json
sys.path.append("..")
from common import operateYaml
from common.operateElement import OperateElement
from testMode.modeCase import GetCase,GetCaseInfo
from common import testLog
from common.variable import GetVariable as common
from common.operateFile import OperateFile
class ModeAndExecCase():
    def __init__(self,test_module="",**kwargs):
        print(kwargs.keys())
        self.test_module=test_module
        # self.GetCaseInfo=kwargs["GetCaseInfo"]
        # self.GetCase=kwargs["GetCase"]
        self.driver=kwargs["driver"]
        self.GetCaseInfo=GetCaseInfo()
        self.GetCase=GetCase()
        self.test_module=test_module
        # self.data = {"init": [], "info": []}
        self.operateFile=OperateFile(kwargs["reportPath"])

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
        logTest=testLog.myLog().getLog()
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
    def execCaseAndLog(self,file,**kwargs):
        logTest = testLog.myLog().getLog()
        # 获取数据模型
        dataMode = self.getModeList(file)
        ch_check=dataMode[-1]
        if dataMode[0].get("url") != "false":
            self.driver.get(dataMode[0].get("url", "false"))
        # 操作元素对象
        operateElement = OperateElement(self.driver)
        for k in dataMode:
            if k["operate_type"] != "false":
                if operateElement.operate_element(k)==False:
                    logTest.checkPointNG(self.driver,kwargs["test_name"],kwargs["test_name"])
                    logTest.resultNG(kwargs["test_name"], "找不页面元素")
                    break
        if operateElement.findElement(ch_check):
            common.test_success += 1
            self.GetCaseInfo.test_result="成功"
            logTest.resultOK(kwargs["test_name"])
        else:
            logTest.checkPointNG(self.driver,kwargs["test_name"],kwargs["test_name"])
            common.test_failed+=1
            test_reason = "检查不到元素"
            self.GetCaseInfo.test_result="失败"
            self.GetCaseInfo.test_reason=test_reason

        self.GetCaseInfo.test_name=kwargs["test_name"]
        self.GetCaseInfo.test_module=self.test_module
        common.test_sum+=1
        common.DetailData["info"].append(json.loads(json.dumps(self.GetCaseInfo.to_primitive())))
        print('common_DetailData='+str(common.DetailData["info"]))
        # if kwargs["isLast"] == "1":
        #     # 最后case要写最下面的统计步骤
        #     self.result["info"].append(data["info"])
        """
        将生成数据，写入excel
        """
        if self.GetCaseInfo.test_name!="test_login_module":
            self.operateFile.writeExcel(common.DetailData["info"])




if __name__=="__main__":
    getCase=GetCase()
    getCaseInfo=GetCaseInfo()
    mc=ModeAndExecCase(GetCaseInfo=GetCaseInfo(),GetCase=GetCase())
    f="/home/dushanshan/git/lilytao5_python/python/shujuguan_test/case/yaml/login/login.yaml"
    data=mc.getModeList(f)
    print("return data :\n"+str(data))
