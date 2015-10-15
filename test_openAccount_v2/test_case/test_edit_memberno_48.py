#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月21日
Function:会员变更  点击个人信息 会员单位  填写完个人信息、协议签署点击下一步之后进行更换会员
个人信息协议管理
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
        sleep(3)
        nickname=json_data["nickname"]
        province=json_data['province']
        city=json_data['city']
        region=json_data['region']
        address=json_data['address']
        phoneno=json_data['phone']
        postId=json_data['post_id']
        member=json_data['memberno']
        referrer=json_data['referrer']
        new_member=json_data['memberno_B']
        new_referrer=json_data['referrer_S']
        self.pub_.userinfo_change_memberNo_after_input_protocol(nickname, province, city, region, 
                                                       address, phoneno, postId,member, 
                                                       referrer,new_member, new_referrer)
        
        msg1 = self.pub_.get_content1()
        self.assertTrue(u"江苏大泰贵金属有限公司", msg1)
        msg2 = self.pub_.get_content2()
        self.assertTrue(u"甲方：江苏大泰贵金属有限公司", msg2)
        self.assertTrue(u"乙方（交易商）：%s"%nickname, msg2)
        self.assertTrue(u"证件号：259755195912136105(身份证)", msg2)
        
    def test_account_info(self):
        self.with_account_info()
    
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()          
