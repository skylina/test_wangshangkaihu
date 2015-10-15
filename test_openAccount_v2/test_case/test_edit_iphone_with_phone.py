#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月9日
Function:测试修改手机使用手机号进行验证，输入新手机号
@author: lina
To me :Believe yourself!
'''
from os import sys, path
from selenium import webdriver
from time import sleep
import unittest
from test_case.public import edit_email, active_page
import time
sys.path.append("\public")
from public import pub_shipan_accountinfo
from public import readFile
from public import login_page

filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
json_data = readFile.read_jsonFile(filepath)
class TestAccountInfo(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        self.dr.get(json_data['url'])
        self.pub_=pub_shipan_accountinfo.Pub(self.dr)
        self.editE=edit_email.Edit_Email(self.dr)
    def with_account_info(self):
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"])
        sleep(3)
        #个人信息
        # dr.find_element_by_link_text("个人信息").click()
        self.pub_.userinfo_btn()
        #修改手机
        self.editE.edit_phone_with_mobile(json_data["checkCode"])
        
        time.sleep(10)
        
        self.editE.write_new_phone(json_data['new_mobileno'],json_data['checkCode'])
        msg=self.dr.find_element_by_xpath("//div[@id='wrapper']/div[3]/p/a/span").text
        self.assertTrue("您已成功修改了您的手机号码返回首页", msg)

    def test_account_info(self):
        self.with_account_info()
    
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()          