#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月19日
Function:
@author: lina
To me :Believe yourself!
'''
import json, linecache
# 读取json配置文件 
def read_jsonFile(filepath):
    # print "jsonfile:%s"%filepath
    lines = linecache.getlines(filepath)
    # print "lines:-----------%s"%lines 
    datas = "".join(lines)
    # print "datas:***********%s"%datas
    data = json.loads(datas)
    # print data
    return data
