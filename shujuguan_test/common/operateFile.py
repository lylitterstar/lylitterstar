#coding=utf-8
__author__='dushanshan'
from xlwt import Workbook
import xlrd
from xlutils.copy import copy
import os
from common.variable import GetVariable as common
import collections
class OperateFile():
    def __init__(self,file_path):
        self.file_path=file_path
    def initExcel(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        file =Workbook(encoding='utf-8')
        # 指定打开的文件名
        table = file.add_sheet('test')
        # 写入表头
        title = ['test_result', 'test_reason', 'test_module', 'test_name', 'test_intr', 'test_id']
        title = ['test_id','test_intr','test_module','test_name','test_result','test_reason']
        for i,j  in enumerate(title):
            print(i,j)
            table.write(0,i,title[i])
        file.save(common.REPORT_FILE)
    def sortDict(self,dict):
        d=collections.OrderedDict()
        d['test_id']=dict['test_id']
        d['test_intr']=dict['test_intr']
        d['test_module']=dict['test_module']
        d['test_name']=dict['test_name']
        d['test_result']=dict['test_result']
        d['test_reason']=dict['test_reason']
        return d


    def writeExcel(self,reportdata):
        # 指定file以utf-8的格式打开,创建一个工作簿
        rb = xlrd.open_workbook(self.file_path, formatting_info=True)
        wsheet=rb.sheet_by_index(0)
        lnum=wsheet.nrows
        wb = copy(rb)
        table = wb.get_sheet(0)
        j=-1
        d=self.sortDict(reportdata[-1])
        for key in d:
            j+=1
            table.write(lnum,j,d[key])
        # for k,v in reportdata[-1].items():
        #     j+=1
        #     table.write(lnum, j, v)
        wb.save(common.REPORT_FILE)

if __name__=="__main__":
    data1=[]
    ow=OperateFile()
    ow.initExcel()
    ow.writeExcel(data1)





