# -*- coding: utf-8 -*-
__author__ = 'dushanshan'
# 查找元素的方式
class GetVariable(object):
    NAME = "name"
    ID = "id"
    XPATH = "xpath"
    INDEX = "index"
    find_element_by_id = "by_id"
    find_elements_by_id = "by_ids"
    find_element_by_name = "by_name"
    find_elements_by_name = "by_names"
    find_element_by_link_text ="by_link_text"
    find_elements_by_link_text = "by_link_texts"
    find_element_by_xpath = "by_xpath"
    find_elements_by_xpath = "by_xpaths"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    SELENIUM = "selenium"
    IE = "ie"
    FOXFIRE = "foxfire"
    CHROME = "chrome"

    CLICK = "click"
    DRIVER = ""
    TAP = "tap"

    SEND_KEYS = "send_keys"
    FIND_STR = "find_str"
    WAIT_TIME = 50

    #selenium
    SEND_CODE = "send_code" # 输入验证码

    #本地存储记录所有的case情况的路径
    REPORT_INFO_PATH = "d:/info.txt"
    REPORT_INIT = "d:/init.txt"
    REPORT_COLLECT_PATH = "d:/collect.txt"
    CRASH_LOG_PATH = "d:/crash.txt" # 存放crash的json文件名
    # case sucesss num
    test_success=0
    test_failed=0
    test_sum=0

    DetailData = {"init": [], "info": []}
    TotalResult = {"init": [], "info": []}
    RESULT_PATH="/home/dushanshan/git/lilytao5_python/python/shujuguan_test/testReport.xlsx"
    REPORT_FILE="testReport.xlsx"
