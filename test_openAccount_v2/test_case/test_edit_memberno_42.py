#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月21日
Function： 对注册时的会员A进行变更为B或者修改推荐人，变更之后填进行开户操作
@author: lina
To me :Believe yourself!
'''
from os import sys, path
from selenium import webdriver
from time import sleep
import unittest
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
        self.pub_ = pub_shipan_accountinfo.Pub(self.dr)

    def with_account_info(self):
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"])    
        self.pub_.click_member_without_referrer(json_data['memberno_B'])
        sleep(3)
        nickname=json_data["nickname"]
        province=json_data['province']
        city=json_data['city']
        region=json_data['region']
        address=json_data['address']
        phoneno=json_data['phone']
        postId=json_data['post_id']
        member=json_data['memberno_C']
        referrer=json_data['referrer_T']
        self.pub_.change_memberNo_after_input_userinfo(nickname, province, city, 
                                                       region, address, phoneno,
                                                        postId,member, referrer)
        
        mem_name = self.pub_.get_member_name()
        mem_id = self.pub_.get_member_id()
        self.assertTrue("江苏瑞福源贵金属有限公司", mem_name)
        self.assertTrue("106", mem_id)
        
    def test_account_info(self):
        self.with_account_info()
    
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()          
