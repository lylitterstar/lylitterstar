
#　-*- coding: utf-8 -*-

import os
import sys
import signal


def kill(pid):

    try:
        a=os.kill(pid, signal.SIGKILL)
        # a = os.kill(pid, signal.9) 
       # print ('已杀死pid为%s的进程,　返回值是:%d' % (pid, a))
        print ('已杀死pid为%s的进程,　' % (pid))
    except OSError as e:
        print ('没有如此进程!!!')


if __name__=='__main__':
    
    kill(14515)


        
