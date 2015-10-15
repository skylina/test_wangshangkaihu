#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年9月10日
Function:
@author: lina
To me :Believe yourself!
'''
from test_case.public.base_page import BasePage
from test_case.public.active_page import ActiveEmailPage
import time
import re
from test_case.public import active_page
class Edit_Email(BasePage):
    #使用正则获取邮箱中的超链接
    def get_re(self):
        active_url = '<a .*?href="(.*?)".*?>'
        return active_url
    #拼接url 修改    
    def content_append(self,content_text,activeurl,edit):
        content_text.append(activeurl)
        content_text.append(edit)
    #把修改和URL存放到列表中
    def get_content_from_editEmail(self,grep):
        active_url=self.get_re()
        content_text=[]
        change = "".join(re.findall(active_url, grep)[0])
        activeurl = "".join(re.findall(active_url, grep)[1])
        print "xiugai:%s"%change
        self.content_append(content_text, change,activeurl)
        print content_text
        return content_text
    def open_emailBox(self):
        return self.by_xpath("//*[@id='folder_1']")
    #获取到邮箱html中  修改和URL的超链接
    def loginEmail_with_edit_email(self,emailUsername,emailPwd):
        dr = self.driver
        
        ac=active_page.ActiveEmailPage(dr)
        #登录邮箱
        ac.login_email(emailUsername, emailPwd)  
        self.open_emailBox().click()
        dr.switch_to_frame("mainFrame")
        #打开邮件
        ac.open_acount_email().click()
        #切图
        ac.save_img("open_email")
        
        grep = ac.mailContent().get_attribute("innerHTML")
        content = self.get_content_from_editEmail(grep)
        #print "content_text%s"%content_text
        return content
    #点击获取到文本中的修改或激活
    def get_active_with_word(self,emailUsername,emailPwd):
        dr=self.driver
        context_text=self.loginEmail_with_edit_email(emailUsername, emailPwd)
        active_url=context_text[0]
        print active_url
        dr.get(active_url) 
        time.sleep(10)
    #点击邮件中的 修改或激活的URL
    def get_active_with_url(self,emailUsername,emailPwd):
        dr=self.driver
        context_text=self.loginEmail_with_edit_email(emailUsername, emailPwd)
        print context_text
        active_url=context_text[1]
        print active_url
        dr.get(active_url) 
        time.sleep(10)  
    #修改邮箱 使用邮箱验证
    def edit_email_(self,code):
        #修改邮箱
        self.by_link_text("修改邮箱").click()
        #//div[@id='wrapper']/div[4]/div[1]/input
        self.by_xpath("//input[@value='使用原邮箱验证']").click()
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMailStep2Button").click()
    #修改邮箱 使用手机验证
    def edit_email_user_mobile(self,code):
        #修改邮箱
        self.by_link_text("修改邮箱").click()
        #//div[@id='wrapper']/div[4]/div[1]/input
        self.by_xpath("//input[@value='使用手机验证']").click()
        self.by_id("checkcodeButton").click()
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMailStep2Button").click()    
        
        
        
        
    #修改手机使用邮件验证
    def edit_phone_with_email(self,code):
        #修改邮箱
        self.by_link_text("修改手机").click()
        #//div[@id='wrapper']/div[4]/div[1]/input
        self.by_xpath("//input[@value='使用邮箱验证']").click()
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMailStep2Button").click()
    #修改手机 使用手机验证
    def edit_phone_with_mobile(self,code):
        #修改邮箱
        self.by_link_text("修改手机").click()
        #//div[@id='wrapper']/div[4]/div[1]/input
        self.by_xpath("//input[@value='使用原手机验证']").click()
        self.by_id("checkcodeButton").click()
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMailStep2Button").click()   
    
    def get_msg(self):
        return self.by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[3]/p").text
    #输入新邮箱
    def write_new_email(self,email,code):
        self.by_id("email").send_keys(email)
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMailStep3Button").click()
    #输入新手机号 
    def write_new_phone(self,mobileno,code):
        self.by_id("mobileno").send_keys(mobileno)
        self.by_id("js_genCode").click()
        self.by_id("checkcode").send_keys(code)
        self.by_id("changeMobileStep3Button").click()