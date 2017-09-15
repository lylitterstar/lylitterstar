import subprocess
class RunCmd(object):
  def cmd_run(self, cmd):
    self.cmd = cmd
    subprocess.call(self.cmd, shell=True)
#Sample usage


if __name__=='__main__':
    a = RunCmd()
    #a.cmd_run('ps -ef|grep tomcat')
    a.cmd_run('/opt/apache-jmeter-3.1/bin/jmeter.sh')
    print(a)

