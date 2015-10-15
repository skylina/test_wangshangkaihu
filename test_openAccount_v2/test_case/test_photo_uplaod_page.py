#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月15日
Function:打开 如何使用手机拍照并上传照片
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
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(30)
        self.base_url = "http://10.0.250.209/"
        self.dr.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_download_querenshu(self):
       
        self.dr.get(json_data["url"])  
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"]) 
        sleep(3)
        pub_shipan_accountinfo.Pub(self.dr).photo_uplao_help_page()
        msg = self.dr.current_url
        self.assertTrue("/gnnt/upload?rpage=upload", msg)
    def tearDown(self):
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()