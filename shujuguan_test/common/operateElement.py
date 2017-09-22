# -*- coding: utf-8 -*-
__author__ = 'dushanshan'
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from variable import GetVariable as common
import time

# 此脚本主要用于查找元素是否存在，操作页面元素
class OperateElement():
    def __init__(self, driver=""):
        self.driver = driver
    def findElement(self, mOperate):
        '''
        查找元素.mOperate是字典
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.driver))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("找不到数据")
            return False


    def operate_element(self,  mOperate):
        if self.findElement(mOperate):
            elements = {
                common.CLICK: lambda: operate_click(mOperate, self.driver),
                common.SEND_KEYS: lambda: send_keys(mOperate, self.driver),
                common.SEND_CODE: lambda : send_code()
            }
            return elements[mOperate.get("operate_type")]()
        return False

# 如果要输入验证码，暂停10秒钟，手动去输入
def send_code():
    time.sleep(10)
# 点击事件
def operate_click(mOperate,cts):
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_name or mOperate["find_type"] == common.find_element_by_xpath or mOperate["find_type"] == common.find_element_by_class_name:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == common.find_elements_by_id or mOperate["find_type"] == common.find_elements_by_name or mOperate["find_type"] == common.find_elements_by_class_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()
    # 记录运行过程中的一些系统日志，比如闪退会造成自动化测试停止


def send_keys(mOperate,cts):
    elements_by(mOperate, cts).send_keys(mOperate["text"])


# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {
        common.find_element_by_id : lambda :cts.find_element_by_id(mOperate["element_info"]),
        common.find_elements_by_id : lambda :cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda :cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda :cts.find_element_by_name(mOperate['name']),
        common.find_elements_by_name: lambda :cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda :cts.find_element_by_class_name(mOperate['element_info']),
        common.find_elements_by_class_name: lambda :cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()
