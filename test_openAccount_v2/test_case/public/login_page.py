#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月19日
Function:login_page
@author: lina
To me :Believe yourself!
'''
from base_page import BasePage
from dashboard_page import DashBoardPage
import time

class LoginPage(BasePage):

    def username(self):
        return self.by_id('username')

    def password(self):
        return self.by_id('password')
    
    def repassword(self):
        return self.by_id('repassword')
    
    def oldpwd(self):
        return self.by_id("oldpassword")
    
    def code(self):
        return self.by_id("code")
    #登录按钮
    def login_btn(self):
        return self.by_id('submit-login-button')
    #确认修改按钮
    def edit_pwd_btn(self):
        return self.by_id('submit-button')
    #密码修改成功
    def confim_edit_btn(self):
        return self.by_id('yesButton')
    
    
    
    def error_message(self):
        txt = self.by_id('errorMessage').text
        msg = txt.strip()
        print msg
        return msg
    def login_and_clear_username(self):
        
        self.username().clear()
        
        self.password().clear()
        
        self.code().clear() 
          
    def edit_pwd_clear(self):
        
        self.oldpwd().clear()
        
        self.password().clear()
        
        self.repassword().clear()
    #获取邮箱验证成功

    def get_email_success_msg(self):
        return self.by_xpath("/html/body/div[3]/div[1]")

    def get_text_msg(self):
        text_msg=self.get_email_success_msg().text
        return text_msg
    
    def get_msg(self):
        return self.by_id("tip").text
    # 第一次用户名和密码是从注册邮箱里面读取到的，这里没有完善完
    def edit_pwd(self,oldpassword,password): 
       
        self.edit_pwd_clear()
        self.oldpwd().send_keys(oldpassword)#原始密码       
        
        self.password().send_keys(password)#输入新密码     
         
        self.repassword().send_keys(password)#再次输入新密码 
        
        self.edit_pwd_btn().click() 
        
        msg=self.get_msg()
        if u"密码修改成功" in msg:
            print msg
        self.confim_edit_btn().click() 
    # 登录
    def login(self, username, password, code):
        
        self.login_and_clear_username() 
        
        self.username().send_keys(username) 
        
        self.password().send_keys(password)
         
        self.code().send_keys(code)  
        
        self.login_btn().submit()
        
        return DashBoardPage(self.driver)
    