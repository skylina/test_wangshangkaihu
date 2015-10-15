#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年7月21日
Function:
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
        self.pub_=pub_shipan_accountinfo.Pub(self.dr)
    def with_account_info(self):
        login_page.LoginPage(self.dr).login(json_data["email"], json_data["edit_password"], json_data["code"])
        sleep(3)
        #个人信息
        # dr.find_element_by_link_text("个人信息").click()
        self.pub_.userinfo_btn()
        text_ = u"协议签署"
        self.pub_.account_info(json_data["nickname"],json_data['province'],json_data['city'],json_data['region'],
                               json_data['address'],json_data['phone'],json_data['post_id'],text_,json_data['pic1'],
                               json_data['pic2'],json_data['pic3'])
        #self.pub_.account_info(json_data["nickname"],  json_data['city'],json_data['region'],json_data['address'], json_data['address'], json_data['phone'], json_data['post_id'], text_m, json_data['pic1'], json_data['pic2'], json_data['pic3'],json_data['edit_password'])
        '''
        #修改客户姓名
        self.pub_.update_username(json_data["nickname"])
        # 性别
        self.pub_.set_sex()
        #身份证号
        self.pub_.get_cardID()
        #省市区
        self.pub_.input_address()
        #填写通信地址
        self.pub_.get_address(json_data['address'], json_data['phone'], json_data['post_id'])
        #修改密码  可有可无
        
        #dr.find_element_by_link_text(u"密码修改").click()
        
        #此处的密码可以从配置文件里面读取
        
        #first_login_editpwd.edit_pwd(self,json_data['edit_password'], json_data['re_edit_password'])
        
        #sleep(10)
        
        
        #上传证件资料
        self.pub_.by_link_text(u"证件资料")
        self.pub_.upload_info(json_data['pic1'], json_data['pic2'], json_data['pic3'])
        '''
    def test_account_info(self):
        self.with_account_info()
    
    def tearDown(self):
        self.dr.quit()
if __name__ == "__main__":
    unittest.main()          
