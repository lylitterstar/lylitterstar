# /bin/python
# coding=utf-8

import csv
import os

# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)

def writefile(file):
    with open(file,'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

def appendfile(file):
    with open(file,'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)



filename='test5.csv' #文件名称
fieldnames = ['name', 'age','dep'] #文件标题
data = {'name':'wangjie','age':'27','dep':'数据观事业部'} #文件内容


writefile(filename)
while True:
    size = os.path.getsize(filename)
    if (size < 1024**2): #单位bytes,1024**2为1M,1024**3为1G
        appendfile(filename)
    else:
        break

print formatSize(size)

if __name__=='__main__':

    writefile(filename)
    while True:
        size = os.path.getsize(filename)
        if (size < 1024 ** 2):  # 单位bytes,1024**2为1M,1024**3为1G
            appendfile(filename)
        else:
            break

    print formatSize(size)




