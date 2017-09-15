#coding:utf-8
__author__="dushanshan"
import yaml
import os
def getYaml(yamlPath):

    #方法一：获取当前目录
    # homeYaml = os.path.join(os.getcwd(), "case/yaml", yamlPath)
    # 方法二：获取当前目录
    homeYaml=os.path.join(os.path.dirname(os.path.dirname(__file__)),"case/yaml", yamlPath)
    try:
        with open(homeYaml) as f:
            data=yaml.load(f)
            print data
            return data
        #FileNotFoundError:在python3中才可使用
    except IOError:
        print(u'文件找不到')


if __name__=="__main__":
    fpath=os.path.join(os.path.dirname(os.getcwd()),"case/yaml/login/login.yaml")
    data=getYaml(fpath)
    url=data[0]["url"]

    print("data,",type(data),",url="+url)



