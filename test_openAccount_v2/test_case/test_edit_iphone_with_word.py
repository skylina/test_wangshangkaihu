#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月9日
Function:测试修改手机使用原邮箱进行验证，在原邮箱中打开验证邮件点击修改，
输入新手机号
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
        self.editE.edit_phone_with_email(json_data["code"])
        msg=self.editE.get_msg()
        self.assertTrue("我们已发送了一封验证链接到您的", msg)
        self.dr.get(json_data["QQurl"])
        emailUsername = json_data['email']
        emailPwd = json_data['emailpwd']
        ac=active_page.ActiveEmailPage(self.dr)
        self.editE.get_active_with_word(emailUsername, emailPwd)
        time.sleep(5)
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"])
        #self.assertTrue("您已通过验证", self.dr.find_element_by_xpath("/html/body/div[3]/div[1]").text) 
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