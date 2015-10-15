#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年7月21日
Function:
@author: lina
To me :Believe yourself!
'''
import sys
from selenium import webdriver
import unittest
sys.path.append("\public")
from public import readFile
from public import login_page
json_data = readFile.read_jsonFile("..\\test_data\\register.json")
class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.dr.get(json_data['url'])
        self.login_=login_page.LoginPage(self.dr)
        
    def test_login(self):
        #print "1"
        self.login_.login(json_data["email"],json_data["edit_password"],json_data["code"])
        self.assertTrue("/register/index", self.dr.current_url)
    def test_login_with_incorrect_pwd(self):
        #print "2"     
        self.login_.login(json_data["email"],json_data["incorrect"],json_data["code"])
        self.login_.error_message()
        
    def test_login_with_clear_pwd(self):
        #print "3"
        self.login_.login(json_data["email"],json_data["empty_password"],json_data["code"]) 
        self.login_.error_message()  
        
    def test_login_with_clear_username(self):
        #print "4"
        self.login_.login(json_data["empty"],json_data["edit_password"],json_data["code"])
        self.login_.error_message()       
        
    def tearDown(self):
        self.dr.quit() 
if  __name__=="__main__":
    unittest.main()          