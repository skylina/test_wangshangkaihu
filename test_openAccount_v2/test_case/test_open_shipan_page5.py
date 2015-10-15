#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月24日
Function:实盘开户性别选择男性，勾选完善资料，填写和邮编
@author: lina
To me :Believe yourself!
'''
from os import sys,path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
from public import pub_shipan_accountinfo, login_page
from test_case.public.readFile import read_jsonFile
sys.path.append("\public")
filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
#print filepath
json_data =read_jsonFile(filepath)
class TestOpenShipan(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.base_url = "http://10.0.250.209/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_open_shipan(self):
            
        self.dr.get(json_data["url"])  
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"]) 
        sleep(3)
        pub_shipan_accountinfo.Pub(self.dr).open_account_with_male_inputpostid(json_data["nickname"],json_data['province'],json_data['city'],
                                                           json_data['region'],json_data['address'],json_data["phone"],json_data['memberno'],json_data['referrer'],
                                                           json_data['pic1'],json_data['pic2'],json_data['pic3'],
                                                           json_data['edit_password'],json_data['edit_password'])
    
    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
