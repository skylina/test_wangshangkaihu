#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月21日
Function:
@author: lina
To me :Believe yourself!
'''
from os import sys, path
import json, linecache
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, re
import httplib2
from operator import contains
sys.path.append("\public")
from public import active_page
from public import pub
from public import readFile

filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
#print filepath
json_data = readFile.read_jsonFile(filepath)
# 第一次用户名和密码是从注册邮箱里面读取到的
class TestActiveEmail(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.dr.get(json_data["QQurl"])
        
    def test_activeEmail(self):
        emailUsername = json_data['email']
        emailPwd = json_data['emailpwd']
        code = json_data['imgCheckCode']
        edit_password = json_data['edit_password']
        #初始密码从edit_firstpwd中获取
        file_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\edit_first_pwd.json")
        ac=active_page.ActiveEmailPage(self.dr)
        ac.loginEmail(emailUsername, emailPwd, code, edit_password, file_path)
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()  
