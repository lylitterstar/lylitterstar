#　-*- coding: utf-8 -*-
# f=open('/opt/apache-jmeter-3.1/jmx_test/output.jtl')
import readXml as rx
f=open('/opt/apache-jmeter-3.1/jmx_test/jmxReport/query_Aggregate_Report.jtl')

allWords=[]
allWords2=[]
threadNum=20
# line=f.readline()
line=f.readline()
while  line:
    list=line.split(',')
    if list[1]!=None:
        allWords.append(list[1])
    line=f.readline()
    # print(line)

f.close()

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
print(allWords2[valueof-1])
time=allWords2[valueof-1]
#test threadNum
while(time<5000):
    threadNum=threadNum+50
    text=str(threadNum)

    #modify threadNum
    tree=rx.read_xml("/opt/apache-jmeter-3.1/jmx_test/workcharts_query.jmx")
    root=tree.getroot()
    text_nodes=rx.get_node_by_keyvalue(rx.find_nodes(tree,"hashTree/hashTree/ThreadGroup/stringProp"),{"name":"ThreadGroup.num_threads"})
    rx.change_node_text(text_nodes, text)
    #modify threadTime
    text_nodes_time=rx.get_node_by_keyvalue(rx.find_nodes(tree,"hashTree/hashTree/ThreadGroup/stringProp"),{"name":"ThreadGroup.ramp_time"})
    rx.change_node_text(text_nodes_time, text)

    #6. 输出到结果文件
    # write_xml(tree, "./out.xml")
    rx.write_xml(tree,"/opt/apache-jmeter-3.1/jmx_test/outtest.jtl")


# def analysis_run_time():
