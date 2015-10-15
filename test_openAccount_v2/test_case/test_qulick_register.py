#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月7日
Function:
@author: lina
To me :Believe yourself!
'''
import unittest
from os import path
from selenium import webdriver
from public import readFile
from public import register_page
filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
# print filepath
json_data = readFile.read_jsonFile(filepath)
# print json_data
class TestRegister(unittest.TestCase):
    
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.dr.get(json_data["quickRegister"])
        self.register_ = register_page.Register(self.dr)
    def test_register(self):
        # print json_data["email"],json_data["memberno"],json_data["mobileno"],json_data["imgCheckCode"],json_data["checkCode"],json_data["recommender"]
        self.register_.q_register(json_data["email"], json_data["memberno"], json_data["mobileno"], json_data["imgCheckCode"], json_data["checkCode"], json_data["recommender"], "register")   
        self.assertTrue("quickOpenacc/success" in self.dr.current_url)
        # /html/body/div[3]/div[1]  马上激活账号，完成注册
        self.assertTrue(u"马上激活账号，完成注册" in self.register_.get_msg())
        
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()            
    