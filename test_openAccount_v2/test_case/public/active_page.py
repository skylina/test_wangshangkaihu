#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月20日
Function:
@author: lina
To me :Believe yourself!
'''
import time
import re
import first_login_editpwd
from base_page import BasePage
import login_page
now = time.strftime("%Y_%m_%d-%H_%M_%S")
class ActiveEmailPage(BasePage):
    def emailusername(self):
        return self.by_id("inputuin")
    def email_pwd(self):
        return self.by_id("pp")
    def email_submit(self):
        return self.by_id("btlogin")
    def clear_email_pwd(self):
        self.emailusername().clear()
        self.email_pwd().clear()
        
    #登录邮箱
    def login_email(self,emailUsername, emailPwd):
        self.clear_email_pwd()
        self.emailusername().send_keys(emailUsername)
        self.email_pwd().send_keys(emailPwd)
        self.email_submit().submit()
   
        
    def content_append(self, content_text, activeurl, login_email, oldpwd, moniusername, monipwd):
        content_text.append(activeurl)
        content_text.append(login_email)
        content_text.append(oldpwd)
        content_text.append(moniusername)
        content_text.append(monipwd)
    #通过正则获取邮箱内容
  
    def get_re(self):
        active_url = '<a .*?href="(.*?)".*?>'
        # email = '邮箱:(.*?)，'
        email = 'mailto:(.*?)">'
        old_pwd = u'登录密码是:(\d+)'
        moni_user = u'您的模拟盘账号是：(\d+)'
        moni_pwd = u'密码是：(\d+)'
        return active_url, email, old_pwd, moni_user, moni_pwd
 
    
    def get_content(self,grep):
        active_url, email, old_pwd, moni_user, moni_pwd = self.get_re()
        content_text = [] #存放从邮箱读取的信息
        activeurl = "".join(re.findall(active_url, grep)[0])
        login_email = "".join(re.findall(email, grep))
        print login_email
        oldpwd = "".join(re.findall(old_pwd, grep))
        moniusername = "".join(re.findall(moni_user, grep))
        monipwd = "".join(re.findall(moni_pwd, grep))
        
        self.content_append(content_text, activeurl, login_email, oldpwd, moniusername, monipwd)
        return content_text
    #保存邮件信息

    def wirte_content(self, content_text, file):
        file.write('{"username":"%s"' % content_text[1]) #username
        file.write(',\n"first_pwd":"%s"' % content_text[2]) #pwd
        file.write(',\n"login_url":"%s"' % content_text[0]) #login_url
        file.write(',\n"shipan_username":"%s"' % content_text[3]) #shipan_username
        file.write(',\n"shipan_pwd":"%s"}' % content_text[4]) #shipan_pwd

    def save_trade_Info(self,file_path, content_text):
        file = open(file_path, "w")
        self.wirte_content(content_text, file)
        file.close()
    def open_emailBox(self):
        return self.by_xpath("//*[@id='folder_1']")
    def open_acount_email(self):
        return self.by_xpath("//form[3]/div[2]/table[1]/tbody/tr/td[3]/table/tbody/tr")
    
    def mailContent(self):
        return self.by_id("mailContentContainer")
    

    def first_login(self, code, edit_password, dr, url, username, password):
        dr.get(url)
        #激活之后的第一次登录
        login_ = login_page.LoginPage(dr)
        login_.login(username, password, code)
        self.save_img("first_login")
        #第一次登录修改初始密码
        first_login_editpwd.edit_pwd(self, password, edit_password)
        self.save_img("first_edit_pwd")
         
    
    def loginEmail(self,emailUsername,emailPwd,code,edit_password,file_path):
        dr = self.driver
        #登录邮箱
        self.login_email(emailUsername, emailPwd)  
        self.open_emailBox().click()
        dr.switch_to_frame("mainFrame")
        #打开邮件
        self.open_acount_email().click()
        #切图
        self.save_img("open_email")
        
        grep = self.mailContent().get_attribute("innerHTML")
        print grep
        content_text = self.get_content(grep)
        #把用户名，初始密码写入文件
        self.save_trade_Info(file_path, content_text)
        '''
        url = content_text[0]
        username = content_text[1]
        password = content_text[2]
        self.first_login(code, edit_password, dr, url, username, password)
        '''