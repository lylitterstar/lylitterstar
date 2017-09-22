#coding=utf-8
__author__="dushanshan"

from operateFile import OperateFile
class ReportResult():
    def __init__(self,file_path):
        self.file_path=file_path
        self.op= OperateFile(self.file_path)

    def getReport(self):
        self.op.initExcel()
        #补充，数据info的汇总
        print("report is compaished")




if __name__=="__main__":
    rp=ReportResult()
    rp.getReport()