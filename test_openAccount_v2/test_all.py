#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月7日
Function:
@author: lina
To me :Believe yourself!
'''
from os import sys,path

from selenium import webdriver
import unittest
from public import pub_shipan_accountinfo
import time
from test_case.public import login_page
sys.path.append("\public")

from public import readFile
from public import register_page
from public import active_page

filepath = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\register.json")
#print filepath
json_data = readFile.read_jsonFile(filepath)

class Test_all(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Firefox()
        self.base_url=json_data['quickRegister']
        self.dr.implicitly_wait(30)
        self.dr.get(self.base_url)
        self.login_=login_page.LoginPage(self.dr)
    def test_all(self):
        
        #注册
        register_=register_page.Register(self.dr)
        register_.register(json_data["email"],json_data["memberno"],json_data["mobileno"],
                           json_data["imgCheckCode"],json_data["checkCode"],json_data["recommender"],"register")   
        self.assertTrue("quickOpenacc/success" in self.dr.current_url)
        print "#注册成功"
        #激活邮件
        self.dr.get(json_data["QQurl"])
        emailUsername = json_data['email']
        emailPwd = json_data['emailpwd']
        code = json_data['imgCheckCode']
        edit_password = json_data['edit_password']
        #初始密码从edit_first_pwd中获取
        file_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "test_data\\edit_first_pwd.json")
        
        ac=active_page.ActiveEmailPage(self.dr)
        ac.loginEmail(emailUsername, emailPwd, code, edit_password, file_path)
        print "#激活邮件"
        #第一次登陆
        pwd_data=readFile.read_jsonFile(file_path)
        #self.assertTrue("您已通过验证" ,self.login_.get_text_msg())
        self.dr.get(pwd_data['login_url'])
        time.sleep(10)
        username = pwd_data['username']
        password = pwd_data['first_pwd']
        code = json_data['code']
        self.login_.login(username,password,code) 
        print username,password
        self.assertTrue("/first_edit_pwd" ,self.dr.current_url)
        repassword = json_data['edit_password']
        print repassword
        # 修改密码
        self.login_.edit_pwd(password,repassword)
        self.assertTrue("/gnnt/open", self.dr.current_url)
        #第二次登录  修改个人信息/实盘开户
        #self.dr.get(json_data['url'])
        #text_ = u"协议签署"
        #pub_shipan_accountinfo.Pub(self.dr).account_info(json_data["nickname"],json_data['province'],json_data['city'],json_data['region'],json_data['address'],json_data['phone'],json_data['post_id'],text_,json_data['pic1'],json_data['pic2'],json_data['pic3'])
        '''
        pub_shipan_accountinfo.Pub(self.dr).open_account_m(json_data["nickname"],json_data['province'],
                                                           json_data['city'],json_data['region'],json_data['address'],
                                                           json_data['phone'],json_data['post_id'],
                                                           json_data['memberno'], json_data['referrer'],
                                                           json_data['pic1'],json_data['pic2'],json_data['pic3'],edit_password)
        '''
       
    def tearDown(self):
        self.dr.quit()    
if __name__=='__main__':
    unittest.main()       