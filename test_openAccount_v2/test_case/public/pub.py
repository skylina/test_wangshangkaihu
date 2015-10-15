#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年7月21日
Function:
@author: lina
To me :Believe yourself!
'''
from os import sys, path
from time import sleep
import linecache, json
import createIDCard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
class public_method(object):
    def __init__(self, driver):
        self.dr = driver
    # 登录
    def login(self, username, password, code):
        self.by_id("username").clear()  
        self.by_id("username").send_keys(username) 
        self.by_id("password").clear()
        self.by_id("password").send_keys(password)
        self.by_id("code").clear()  
        self.by_id("code").send_keys(code)  
        self.by_id("submit-login-button").submit()
        # self.assertTrue("register/index" in dr.current_url)
    # 读取json配置文件 
    def read_jsonFile(self, filepath):
        # print "jsonfile:%s"%filepath
        lines = linecache.getlines(filepath)
        # print "lines:-----------%s"%lines 
        datas = "".join(lines)
        # print "datas:***********%s"%datas
        data = json.loads(datas)
        # print data
        return data
    # 修改客户姓名
    def update_username(self, nickname):
        self.by_id("name").clear()
        self.by_id("name").send_keys(nickname)  # 修改用户名
    # 设置性别
    def set_sex(self, dr):
        # //form/div[4]/div/div[2]/input
        self.by_xpath("//form/div/div[4]/div/div[2]/input").click()
        
    # 设置性别_实盘
    def set_sex_shipan(self):
        self.by_xpath("//form/div[4]/div/div[2]/input").click()
    # 身份证号    
    def get_cardID(self):
        self.by_id("cardno").clear()
        self.by_id("cardno").send_keys(createIDCard.fun())    
    # 选择省市区    
    def input_addresss2(self):
        self.by_xpath("//option[@value='1946']").click()  # 省
        self.by_xpath("//option[@value='1947']").click()  # 市
        self.by_xpath("//option[@value='1951']").click()  # 区
        
    def input_address(self, province, city, region):
        Select(self.by_name("areaid_select")).select_by_visible_text(province)
        Select(self.by_xpath("(//select[@name='areaid_select'])[2]")).select_by_visible_text(city)
        Select(self.by_xpath("(//select[@name='areaid_select'])[3]")).select_by_visible_text(region)  
        
    # 填写地址 手机 邮编    
    def get_address_phoneNo(self, address, phone, post_id):
        self.by_id("address").clear()
        self.by_id("address").send_keys(address)
        self.by_id("js_forhide").click()
        self.by_id("phone").clear()
        self.by_id("phone").send_keys(phone)
        self.by_id("postcode").clear()
        self.by_id("postcode").send_keys(post_id)
    
    def get_address(self, address, phone, post_id):
        self.get_address_phoneNo(address, phone, post_id)
        self.by_id("edituserbutton").click()
        self.by_id("closeBtn").click()
    # 地址和手机号
    def get_addressAndPhoneNo(self, address, phone, post_id):
        self.get_address_phoneNo(address, phone, post_id)
        self.by_id("subButton").click()
    # 上传身份证图片    
    def upload_info(self, frontImg, upcartImg, upselfImg):
        self.by_id("upcartfront").click()
        self.dr.switch_to_frame(0)
        self.by_id("file").send_keys(frontImg)
        self.by_css("button.btn.button").click()
        self.by_id("upcartrear").click()
        self.dr.switch_to_frame(0)
        self.by_id("file").send_keys(upcartImg)
        self.by_css("button.btn.button").click()
        self.by_id("upselfphoto").click()
        self.dr.switch_to_frame(0)
        self.by_id("file").send_keys(upselfImg)
        self.by_css("button.btn.button").click()
    # 设置交易密码    
    def update_tradePwd(self, oldpassword, password):
        self.by_id("tpwd").clear()
        self.by_id("tpwd").send_keys(oldpassword)
        self.by_id("tpwdrepeat").clear()
        self.by_id("tpwdrepeat").send_keys(password)
        self.by_id("initPwdSubmit").click()    
    # 协议签署
    def aggrement(self):
        '''
        #第一种方法使用keys.down
        for i in range(25):
            by_id("content1").send_keys(Keys.DOWN)
        sleep(10)
        '''
        # 第二种使用js
        js_text = "document.getElementById('content1').scrollTop=10000"
        self.js(js_text)
        sleep(10)
        self.by_id("chk1").click()
        sleep(10)
        print "风险报告2"
        '''
        for i in range(100):
            by_id("content2").send_keys(Keys.DOWN)
        sleep(10)    
        '''
        js_text = "document.getElementById('content2').scrollTop=10000"
        self.js(js_text)
        sleep(10)
        self.by_id("chk2").click()
        self.by_css("span.btn.syb_btn").click()  # 同意
    # 选择会员单位推荐人        
    def select_memberNo(self, member, referrer):
        
        self.by_id("meList").clear()
        self.by_id("meList").send_keys(member)
        self.by_id("meList").send_keys(Keys.ENTER)
        sleep(5)
        #self.by_css("li.ac_even").click() 
        # 定位会员简介(需求变更 暂没用到）
        # self.by_xpath("//div[@id='member_remark2_div']/div/table/tbody/tr/td[2]/a/img").click()
        self.by_id("recommender").clear()
        self.by_id("recommender").send_keys(referrer)
        self.by_id("recommender").send_keys(Keys.ENTER)
        self.by_id("member_div_botton").click()
    
    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)
    
    def by_name(self, the_name):
        return self.dr.find_element_by_name(the_name)
    
    def js(self, js_text):
        return self.dr.execute_script(js_text)
    
    def by_xpath(self, the_xpath):
        
        return self.dr.find_element_by_xpath(the_xpath)
    
    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)
