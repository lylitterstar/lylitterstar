#　-*- coding: utf-8 -*-

def countTime(allWords):
    
    # print('allWords before:')
    # print(allWords)
    result=map(int,allWords)
    allWords2=[int(i) for i in allWords]
    # allWords2=list(map(int,allWords))
    # print('allWords after:')
    allWords2.sort()
    # print(allWords2)
    print('last Response time value:')
    print(allWords2[-1])
    length=len(allWords2)
    # <-----90%---Response time--->
    print("90% Response time is :")
    valueof=round(length*0.9)
    print(allWords2[long(valueof-1)])
    time=allWords2[long(valueof-1)]
    return time
    




def readTime(filepath):
    #f=open('/opt/apache-jmeter-3.1/jmx_test/jmxReport/query_Aggregate_Report.jtl')
    f=open(filepath)

    allWords=[]
    allWords2=[]
    threadNum=20
    line=f.readline()
    while  line:
        list=line.split(',')
        if list[1]!=None:
            allWords.append(list[1])
            line=f.readline()
            # print(line)
    f.close()

    return allWords




if __name__=="__main__":
    filepath='/opt/apache-jmeter-3.1/jmx_test/jmxReport/query_Aggregate_Report.jtl'
    allWords=readTime(filepath)
    time =countTime(allWords)
    print(time)
