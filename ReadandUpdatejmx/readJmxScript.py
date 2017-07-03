#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : wklken@yeah.net
# date: 2012-05-25
# version: 0.1

import xml.dom.minidom
import sys
from xml.etree.ElementTree import ElementTree,Element

def read_xml(in_path):
  '''读取并解析xml文件
    in_path: xml路径
    return: ElementTree'''
  tree = ElementTree()
  tree.parse(in_path)
  return tree

def write_xml(tree, out_path):
  '''将xml文件写出
    tree: xml树
    out_path: 写出路径'''
  tree.write(out_path, encoding="utf-8",xml_declaration=True)

def if_match(node, kv_map):
  '''判断某个节点是否包含所有传入参数属性
    node: 节点
    kv_map: 属性及属性值组成的map'''
  for key in kv_map:
    if node.get(key) != kv_map.get(key):
      return False
  return True

#---------------search -----
def find_nodes(tree, path):
  '''查找某个路径匹配的所有节点
    tree: xml树
    path: 节点路径'''
  print('find_nodes:')
  print(path)
  root=tree.getroot()
  print(root.findall(path))
  return root.findall(path)



def get_node_by_keyvalue(nodelist, kv_map):
  '''根据属性及属性值定位符合的节点，返回节点
    nodelist: 节点列表
    kv_map: 匹配属性及属性值map'''
  result_nodes = []
  print('get_node_by_keyvalue:')
  print(nodelist)
  for node in nodelist:
    if if_match(node, kv_map):
      result_nodes.append(node)
  return result_nodes

#---------------change -----
def change_node_properties(nodelist, kv_map, is_delete=False):
  '''修改/增加 /删除 节点的属性及属性值
    nodelist: 节点列表
    kv_map:属性及属性值map'''
  for node in nodelist:
    for key in kv_map:
      if is_delete:
        if key in node.attrib:
          del node.attrib[key]
      else:
        node.set(key, kv_map.get(key))
'''改变/增加/删除一个节点的文本
  nodelist:节点列表
  text : 更新后的文本'''
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    for node in nodelist:
        if is_add:
            node.text += text
            print(node.text)
        elif is_delete:
            node.text = ""
        else:
            print('before:')
            print(node.text)
            node.text = text

def add_child_node(nodelist, element):
  '''给一个节点添加子节点
    nodelist: 节点列表
    element: 子节点'''
  for node in nodelist:
    node.append(element)

def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
  '''同过属性及属性值定位一个节点，并删除之
    nodelist: 父节点列表
    tag:子节点标签
    kv_map: 属性及属性值列表'''
  for parent_node in nodelist:
    children = parent_node.getchildren()
    for child in children:
      if child.tag == tag and if_match(child, kv_map):
        parent_node.remove(child)


# get lable in order to count response time
def readLableIntoText(path,lableElementPath,labelTextPath):
    LableList=[]
    tree = read_xml(path)
    #find node elements
    nodes = find_nodes(tree, lableElementPath)
    #get lable by attri
    for node in nodes:
        print (node.get('testname'))
        tempLine=node.get('testname')+"\n"
        LableList.append(tempLine)
    print('len',len(LableList),'labelTextPath',labelTextPath)
    #write into lable.txt
    with open(labelTextPath,'w+') as f:
        f.writelines(LableList)
    return LableList
def readLableIntoList(path,lableElementPath):
    LableList=[]
    tree = read_xml(path)
    #find node elements
    nodes = find_nodes(tree, lableElementPath)
    #get lable by attri
    for node in nodes:
        print (node.get('testname'))
        tempLine=node.get('testname')
        LableList.append(tempLine)
    return LableList

def  updateAtribution(nodes,tagValue,text):
    node=get_node_by_keyvalue(nodes,{"name":tagValue})
    if(node):
        change_node_text(node,text)

#-----------update jmx--------
def updateJmx(jmxScriptPath,num_threads,ramp_time,duration):
  # read Jmx file
  #tempPath="./sjgsum/"
  print('jmxScriptPath='+jmxScriptPath)
  #linux path
  #tree=read_xml("/opt/apache-jmeter-3.1/jmx_test/workcharts_query.jmx")
  tree=read_xml(jmxScriptPath)
  root=tree.getroot()
  #2. 属性修改
  nodes=find_nodes(tree, "hashTree/hashTree/ThreadGroup/stringProp")
  #5. 修改节点文本
  try:
      updateAtribution(nodes,'ThreadGroup.num_threads',num_threads)
  except Exception as e:
      print("input error type args:",e)
  #modify threadTime
  try:
      updateAtribution(nodes,"ThreadGroup.ramp_time",ramp_time)
  except Exception as e:
      print("input error type args:",e)
  #modify durationTime
  try:
      updateAtribution(nodes,"ThreadGroup.duration",duration)
  except Exception as e:
      print("input error type args:",e)
  #6. 输出到结果文件
  write_xml(tree,jmxScriptPath)


#elementName='HTTPSamplerProxy' atrrName='testname'
def findNodesbyValue(jmxScriptPath,elementName,atrrName):
    dom = xml.dom.minidom.parse(jmxScriptPath)
    findNodes = dom.getElementsByTagName("HTTPSamplerProxy")
    dataLable = []
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for node in findNodes:
        lable = node.hasAttribute("testname")
        if lable:
            dataLable.append(node.getAttribute("testname"))
    print('lableList', dataLable)
    return dataLable


if __name__ == "__main__":
  #1. 读取xml文件
  # tree = read_xml("./test.xml")
  # #window path
  # wpath="D:\sjgsum\sjg_Test_Plan_summary_guide.jmx"
  # #linux path
  # lpath = './verifysum/verify_home_page.jmx'

  # #6. 输出到结果文件
  # # write_xml(tree, "./out.xml")
  # #write_xml(tree,"/opt/apache-jmeter-3.1/jmx_test/outtest.jtl")
  # write_xml(tree,lpath)
  path = './verifysum/verify_home_page.jmx'
  # path='./verifysum/verify_category_page.jmx'
  # lableElementPath = 'hashTree/hashTree/hashTree/HTTPSamplerProxy'
  # labelTextPath = './verifysum/configData/lable.txt'
  # readLable(path, lableElementPath, labelTextPath)
  jmxScriptPath=path
  elementName='s'
  atrrName='s'
  findNodesbyValue(jmxScriptPath,elementName,atrrName)






