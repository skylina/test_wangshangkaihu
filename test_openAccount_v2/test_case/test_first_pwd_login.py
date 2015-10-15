#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月8日
Function:
@author: lina
To me :Believe yourself!
'''
import sys
from selenium import webdriver
import unittest
import time
from os import path
from test_case.public.readFile import read_jsonFile
sys.path.append("\public")
from public import readFile
from public import login_page

filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
json_data = read_jsonFile(filepath) 
file_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\edit_first_pwd.json")
pwd_data = read_jsonFile(file_path) 

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.dr.get(pwd_data['login_url'])
        self.login_=login_page.LoginPage(self.dr)
       
    def test_first_login(self):
        self.assertTrue("您已通过验证" ,self.login_.get_text_msg())
        time.sleep(15)
        
        username = pwd_data['username']
        password = pwd_data['first_pwd']
        code = json_data['code']
        self.login_.login(username,password,code) 
        print self.dr.current_url
        self.assertTrue("/first_edit_pwd" ,self.dr.current_url)
        repassword = json_data['edit_password']
        # 修改密码
        self.login_.edit_pwd(password,repassword)
        self.assertTrue("/gnnt/open", self.dr.current_url)
        
    def tearDown(self):
        self.dr.quit() 
if  __name__=="__main__":
    unittest.main()          