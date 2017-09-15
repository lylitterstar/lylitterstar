#　-*- coding: utf-8 -*-
import countTime
import getPId
#import jmxRead
import readXml as rx
import threading
import time

def Main():
    
    #start jmeter
    #cmd='/opt/apache-jmeter-3.1/bin/jmeter.sh'
    cmd='/opt/apache-jmeter-3.1/bin/jmeter.sh -n -t /opt/apache-jmeter-3.1/jmx_test/test_workcharts_query.jmx -l /opt/apache-jmeter-3.1/jmx_test/jmxReport/Aggregate_Report.jtl'
    timeindex=100
    print('start jmeter')
    getPId.cmd_run(cmd)
    print('end jmeter')

    #get now time
    print('now time')
    now=time.ctime()
    new10min=now+timeindex
    newtime=time.ctime(new10min)
    #sleep 10min
    print('into sleep')
    at=int(timeindex)
    time.sleep(at)
    
    #read jmeter output
    filepath='/opt/apache-jmeter-3.1/jmx_test/jmxReport/query_Aggregate_Report.jtl'
    allWords=countTime.readTime(filepath)
    timeResponse =countTime.countTime(allWords)
    print('timeResponse:')
    print(timeResponse)

    #is >5000
    while(timeResponse<5000):
        threadNum=threadNum+50
        textThreadNum=str(threadNum)
        textThreadStartTime=10
        #modify jmeter thread Num
        tree=rx.read_xml("/opt/apache-jmeter-3.1/jmx_test/test_workcharts_query.jmx")
        root=tree.getroot()
        text_nodes=rx.get_node_by_keyvalue(rx.find_nodes(tree,"hashTree/hashTree/ThreadGroup/stringProp"),{"name":"ThreadGroup.num_threads"})
        rx.change_node_text(text_nodes, textThreadNum)
        #modify thread init start Time
        text_nodes_time=rx.get_node_by_keyvalue(rx.find_nodes(tree,"hashTree/hashTree/ThreadGroup/stringProp"),{"name":"ThreadGroup.ramp_time"})
        rx.change_node_text(text_nodes_time, str(textThreadStartTime))
        p=getPId.getPid2('ApacheJMeter')
        getPId.kill(int(p[0]))
        #restart jmeter
        cmd1='/opt/apache-jmeter-3.1/bin/jmeter.sh'
        getPId.cmd_run(cmd1)
        #kill jmeter
        p=getPId.getPid2('ApacheJMeter')
        getPId.kill(int(p[0]))



class StartThread(threading.Thread):
    def __init__(self,name,internal,pidName):
        threading.Thread.__init__(self)
        self.name=name
        self.internal=internal
        self.pidName=pidName
        
    def run(self):
        while 1:
            #start jmeter
            print('start jmeter')
            cmd1='/opt/apache-jmeter-3.1/bin/jmeter.sh'
            getPId.cmd_run(cmd1)
            status=1
            #sleep(200)
            time.sleep(self.internal)
            if int(status)<1:
                #kill jmeter 'ApacheJMeter'
                p=getPId.getPid2(self.pidName)
                getPId.kill(int(p[0]))
                break




                            
                            
                            
                            
                            
                
        
        
        
        
    
        
        
if __name__=='__main__':
    print('----start----')
    #Main()
    
    cmd='/opt/apache-jmeter-3.1/bin/jmeter.sh -n -t /opt/apache-jmeter-3.1/jmx_test/test_workcharts_query.jmx -l /opt/apache-jmeter-3.1/jmx_test/jmxReport/Aggregate_Report.jtl'
    t1=threading.Thread(target=getPId.cmd_run,args=(cmd,))
    t2=threading.Thread(target=threadTest,args=(t1,))
        
        
        
        

        
        
        
    

    

    
