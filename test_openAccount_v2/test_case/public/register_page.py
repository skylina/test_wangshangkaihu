#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月20日
Function:
@author: lina
To me :Believe yourself!
'''
from os import sys, path
import time
from selenium import webdriver
import unittest
import json, linecache
import pub
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
from test_case.public.dashboard_page import DashBoardPage
class Register(BasePage):
    
    def email(self):
        return self.by_id("email")
    def member_unit(self):
        return self.by_id("meList")
    def auto_unit(self):
        return self.by_id("autoSelect")
    def member_list(self):
        return self.by_css("li.ac_even")
    def member_info(self):
        return self.by_xpath("//div[@id='member_remark_div']/div/table/tbody/tr/td[2]/a/img")
    
    
    def mobile_no(self):
        return self.by_id("mobileno")
    def show_genCode(self):
        return self.by_id("show_genCode")
    def img_checkCode(self):
        return self.by_id("imgCheckCode")
    def js_genCode(self):
        return self.by_id("js_genCode")
    def checkCode(self):
        return self.by_id("checkCode")
    def recommender(self):
        return self.by_id("recommender") 
    def quick_button(self):
        return self.by_id("quick_button")
    
    def confim_register_btn(self):
        return self.by_id("submit-register-button")
    def element_clear(self):
        self.email().clear()
        self.member_unit().clear()
        self.mobile_no().clear()
        #self.img_checkCode().clear()
        self.checkCode().clear()
        self.recommender().clear()
    def get_msg(self):
        #马上激活账号，完成注册
        return self.by_xpath("/html/body/div[3]/div[1]").text
        #print text_msg    
        
    def member_unit_v(self):
        return self.by_xpath("//*[@id='meList']")
    def click_register_btn(self):
        return self.by_class_name("registered")


    def select_moni_money(self):
        return self.by_xpath("//form/div[6]/div/span[1]/label[3]/input")
    #此方法为 从首页点击注册步骤
    def register(self, email, memberno, mobilno, imgCheckCode, checkCode, recommender,img_path):
        self.element_clear()
        #点击首页的注册按钮
        #self.by_link_text("注册")
        self.click_register_btn().click()
        self.email().send_keys(email)
        ##自动分配会员单位
        #self.auto_unit().click()
        
        #直接输入会员单位
        self.member_unit().send_keys(memberno)
        self.member_unit().send_keys(Keys.ENTER) 
        #self.member_list().click()
        # 定位会员简介
        #self.member_info().click()
    
        print  self.member_unit_v().text#打印会员单位 没有获取到
        self.pub_register_info(mobilno, imgCheckCode, checkCode, recommender, img_path)
        self.select_moni_money().click()
        self.confim_register_btn().click()
        self.save_img(img_path)
        
    def pub_register_info(self, mobilno, imgCheckCode, checkCode, recommender, img_path):
        # mobileno
        self.mobile_no().send_keys(mobilno)
        # 点击发送手机验证码
        self.show_genCode().click()
        time.sleep(3)
        #验证码
        self.img_checkCode().send_keys(imgCheckCode)
        # time.sleep(5)
        self.js_genCode().click() #免费发送验证码
        time.sleep(3)
        # 验证码
        self.checkCode().send_keys(checkCode)
        
        

    def q_register(self, email, memberno, mobilno, imgCheckCode, checkCode, recommender,img_path):
        self.element_clear()
        self.email().send_keys(email)
        #会员单位
        self.member_unit().send_keys(memberno)
        self.member_unit().send_keys(Keys.ENTER) 
        # self.member_list().click()
        # 定位会员简介
        # self.member_info().click()
        self.pub_register_info(mobilno, imgCheckCode, checkCode, recommender, img_path)
        # 推荐人
        time.sleep(3)
        self.recommender().send_keys(recommender)
        self.quick_button().click()
        self.save_img(img_path)
        # 验证register/quickOpenacc/success 
        #print self.driver.current_url
        #self.assertTrue("quickOpenacc/success" in self.driver.current_url)    
        
        
