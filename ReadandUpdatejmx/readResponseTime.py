# 　-*- coding: utf-8 -*-
from collections import defaultdict
from ReadandUpdatejmx import readJmxScript as rjmx
d=defaultdict(list)
label=[]
def countTime(allWords):
    # print('allWords before:')
    # print(allWords)
    if len(allWords)==0:
        return 0
    else:
        result = map(int, allWords)
        allWords2 = [int(i) for i in allWords]
        # allWords2=list(map(int,allWords))
        allWords2.sort()
        # print(allWords2)
        # print(allWords2[-1])
        length = len(allWords2)
        # <-----90%---Response time--->
        print("90% Response time is :")
        valueof = round(length * 0.9)
        print(allWords2[long(valueof - 1)])
        time = allWords2[long(valueof - 1)]
        return time



def readTime(filepath):
    # f=open('/opt/apache-jmeter-3.1/jmx_test/jmxReport/query_Aggregate_Report.jtl')
    f = open(filepath)
    allWords = []
    line = f.readline()
    line = f.readline()
    while line:
        list = line.split(',')
        if list[1] != None:
            allWords.append(list[1])
            line = f.readline()
            # print(line)
    f.close()
    return allWords

# easy method
def tryReadTime(filepath):
    allWords = []
    with open(filepath,'rb') as f:
        line = f.readline()
        for line in f:
            # print('line',line)
            list = line.split(',')
            if len(list)>2:
                if list[1] != None:
                    allWords.append(list[1])

    return allWords

# #method 1: read lable from lable txt
# def mulTypeTimeFromFile(filepath,labelpath):
#     #method 1: read lable from lable txt
#     allWords = []
#     #read config label
#     with open(labelpath,'rb') as f:
#         for line in f:
#             line=line.strip('\n')
#             # print('label',line)
#             label.append(line)
#     #init defaultdict
#     global  d
#     for i in range(len(label)):
#         d.setdefault(label[i],[])
#     print('init d:',d)
#     #read out jtl
#     with open(filepath, 'rb') as f:
#         line = f.readline()
#         print(type(line))
#         for line in f:
#             line=line.strip('\n')
#             list = line.split(',')
#             if len(list)>=2:
#                 if list[2] not in d.keys():
#                     for key in d.keys():
#                         if key.find('api/yuntuapp/fingerprint') != -1:
#                             d[key].append(int(list[1]))
#                             break
#                 else:
#                     d[list[2]].append(int(list[1]))
#
#
#     for key in d.keys():
#         print(key)
#         allWords.append(int(countTime(d[key])))
#     print('allWords',allWords)
#     finalTime=int(countTime(allWords))
#
#     print('finalTime',finalTime)
#     return finalTime

#method 2: from lable list[]
# detailed method
def mulTypeTime(filepath,label):
    allWords = []
    testTotal=[]
    for i in range(len(label)):
        d.setdefault(label[i],[])
    print('init d:',d)
    #read out jtl
    with open(filepath, 'rb') as f:
        line = f.readline()
        print(type(line))
        for line in f:
            line=line.strip('\n')
            list = line.split(',')
            if len(list)>2:
                testTotal.append(list[1])
                if list[2] not in d.keys():
                    for key in d.keys():
                        if key.find('api/yuntuapp/fingerprint') != -1:
                            d[key].append(int(list[1]))
                else:
                    d[list[2]].append(int(list[1]))

    for key in d.keys():
        print(key)
        allWords.append(int(countTime(d[key])))
    allWords.sort()
    print('allWords',allWords)
    # finalTime=int(countTime(allWords))
    # print('allWords length',len(allWords))
    finalTime=int(countTime(testTotal))
    # print('test total  length', len(testTotal))
    # print('test total time:', finalTime)
    # print('finalTime',finalTime)
    return finalTime


if __name__=="__main__":
    filepath="./verifysum/jmxReport/verify_home_page.jmx_50_2017-05-23-20-52-08.jtl"
    labelpath="./verifysum/configData/lable.txt"
    path='./verifysum/verify_home_page.jmx_50_2017-05-23-20-52-08.jtl'
    lableElementPath = 'hashTree/hashTree/hashTree/HTTPSamplerProxy'
    label=rjmx.readLableIntoList(path, lableElementPath)
    print('label',label)
    mulTypeTime(filepath,label)






