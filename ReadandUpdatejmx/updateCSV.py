
#-*- encoding:UTF-8 -*-
def readandUpdateCSV(csvFilepath,sessionID):
    """

    :param csvFilepath:
    """
    try:
        f=open(csvFilepath,'r')
        line=f.readline();
        #get the last value
        s=line.split(',')
        s[-1]=sessionID
        #sessionID=s.pop();
        lineNew=",".join(s)
       # print("read conten:"+line,'sessionId='+s[-1])
        if(sessionID):
            open(csvFilepath,'w').writelines(lineNew)
    except Exception as e:
        print("error info:"+e)

    finally:
        f.close()
    print(f)


if __name__=="__main__":
    csvFilepath="D:\sjgsum\configData\sjg.txt"
    #csvFilepath= raw_input("please input sessionID")
    sessionID=input("Enter PHPSessionID:")
    readandUpdateCSV(csvFilepath,sessionID)

