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
import createIDCard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from base_page import BasePage
import readFile
from test_case.public import login_page
from colorama.win32 import handles
import time
import re


class Pub(BasePage):
    # 个人信息
    def userinfo_btn(self):
        self.by_link_text(u"个人信息").click()
    # 网上开户
    def open_account_btn(self):
        self.by_link_text(u"实盘开户").click()   
    # 上传证件资料
    def update_infomation(self):
        self.by_link_text(u"证件资料").click()
    # 修改客户姓名
    def update_username(self, nickname):
        self.by_id("name").clear()
        self.by_id("name").send_keys(nickname)  # 修改用户名
    # 设置性别
    def set_sex(self):
        # //form/div[5]/div/div[2]/input
        # self.by_xpath("//form/div/div[5]/div/div[2]/input").click()
        self.by_xpathes("//input[@type='radio']").pop().click()
    # 设置性别_
    def set_sex_male(self):
        # /html/body/div[3]/div/div[2]/div[2]/form/div[5]/div/div[2]/input
        # self.by_xpath("//form/div[5]/div/div[2]/input").click()
        self.by_xpathes("//input[@type='radio']").pop(1).click()
    # 身份证号    

    def get_cardID(self, cardID_path):
        cardID = createIDCard.fun()
        self.save_trade_Info(cardID_path, cardID)
        return cardID

    def set_cardID(self):
        self.by_id("cardno").clear()
        cardID = createIDCard.fun()
        self.by_id("cardno").send_keys(cardID) 
          
    def save_trade_Info(self, file_path, content_text):
        file = open(file_path, "w")
        self.wirte_content(content_text, file)
        file.close()    
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
    def set_address(self, address):
        self.by_id("address").clear()
        self.by_id("address").send_keys(address)

    def get_address_phoneNo(self, address, phone, post_id):
        self.set_address(address)      
        self.click_radio()
        self.set_phone(phone)
        self.set_postcode(post_id)
    
    def get_address(self, address, phone, post_id):
        self.get_address_phoneNo(address, phone, post_id)
        self.by_id("edituserbutton").click()
        self.by_id("closeBtn").click()
    # 地址和手机号
    def get_addressAndPhoneNo(self, address, phone, post_id):
        self.get_address_phoneNo(address, phone, post_id)
        self.sub_btu()
    # 勾选完善资料填写固定电话
    def click_radio_with_phone(self, phoneno):
        self.click_radio()
        self.set_phone(phoneno)
        self.set_postcode("") 
        self.sub_btu()
    # 勾选完善资料填写邮编
    def click_radio_with_postcode(self, postcode):
        self.click_radio()
        self.set_phone("")
        self.set_postcode(postcode) 
        self.sub_btu()  
    # 勾选完善资料设置固定电话和邮编
    def set_phone_postcode(self, phone, post_id):         
        self.click_radio()
        self.set_phone(phone)
        self.set_postcode(post_id)
        self.sub_btu()
    # 勾选完善资料
    def click_radio(self):
        self.by_id("js_forhide").click()
    # 设置固定电话    
    def set_phone(self, phoneno):
        self.by_id("phone").clear()
        self.by_id("phone").send_keys(phoneno)
        
    # 设置邮编
    def set_postcode(self, postcode):
        self.by_id("postcode").clear()
        self.by_id("postcode").send_keys(postcode)  
    # 实盘开户填写个人信息下一步按钮
    def sub_btu(self):
        self.by_id("subButton").click()    
    # 下一步按钮
    def next_btn(self):
        self.by_id("nextButton").click()
    def go_to_help_url(self):
        # /html/body/div[3]/div/div[2]/form/div/div[4]/a
        self.by_link_text("如何使用手机拍照并上传图片？").click()
    # 获取会员名称
    def get_member_name(self):
        return self.by_xpath("//ul[@class='vip_title']/li[1]/span").text

    # 获取会员ID
    def get_member_id(self):
        return self.by_xpath("//ul[@class='vip_title']/li[2]/span").text   
    # 获取会员展示
    def click_member_info_btn(self):
        return self.by_link_text("会员展示")  
    # 获取变更按钮
    def change_btn(self):
        return self.by_id("changeOpen")
    
    # 变更会员 清空推荐人
    def click_member_without_referrer(self, member):
        self.click_member_info_btn().click()  # 点击会员展示
        print "3", self.driver.current_url
        self.change_btn().click()
        self.change_member_name(member)
        self.by_id("recommender").clear()
        self.by_id("memberChangeSubmit").click()  # 确认修改按钮
    # 个人信息->会员变更
    def userinfo_click_memberinfo(self, member, referrer):
        self.driver.switch_to_default_content()
        time.sleep(3)
        self.by_link_text("首页").click()
        self.by_link_text("个人信息").click()
        self.by_link_text("会员单位").click()
        print "3", self.driver.current_url
        self.change_btn().click()
        self.change_membername_and_referen(member, referrer)
        self.by_id("memberChangeSubmit").click()  # 确认修改按钮
    # 导航-》会员展示
    def click_memberinfo(self, member, referrer):
        self.click_member_info_btn().click()  # 点击会员展示
        print "3", self.driver.current_url
        self.change_btn().click()
        self.change_membername_and_referen(member, referrer)
        self.by_id("memberChangeSubmit").click()  # 确认修改按钮
    
    def change_memberNo(self, member, referrer):
        self.driver.switch_to_default_content()
        time.sleep(3)
        self.click_memberinfo(member, referrer)    
    # 实盘开户个人信息填写完毕
    def change_memberNo_after_input_userinfo(self, nickname, province, city, region, address, phoneno, postId, member, referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        time.sleep(5)
        # 变更会员
        self.change_memberNo(member, referrer)
        # 返回实盘开户
        # self.open_account_btn()
    # 实盘开户填写会员单位信息之后 修改
    def change_memberNo_after_input_memberinfo(self, nickname, province, city, region, address, phoneno, postId, member, referrer, new_member, new_referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 变更会员
        self.change_memberNo(new_member, new_referrer)
        # 返回实盘开户
        # self.open_account_btn()
    # 实盘开户协议签署之后未点击下一步
    def change_memberNo_after_input_protocol(self, nickname, province, city, region, address, phoneno, postId, member, referrer, new_member, new_referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement_without_next()
        # 变更会员
        self.change_memberNo(new_member, new_referrer)
        # 返回实盘开户
        # self.open_account_btn()
        
    # 实盘开户协议签署点击下一步
    def change_memberNo_after_input_protocol_with_next(self, nickname, province, city, region, address, phoneno, postId, member, referrer, new_member, new_referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        # self.aggrement_without_next()
        # 变更会员
        self.change_memberNo(new_member, new_referrer)
        # 返回实盘开户
        # self.open_account_btn()

    def get_content1(self):
        text = self.by_id("content1").get_attribute("innerHTML")
        return text
    def get_content2(self):
        text = self.by_id("content2").get_attribute("innerHTML")
        return text
    def userinfo_agrrement(self):
        # self.driver.switch_to_default_content()
        time.sleep(3)
        self.by_link_text("首页").click()
        self.by_link_text("个人信息").click()
        self.by_link_text("协议管理").click()
        assert u"大宗商品交易协议" in self.by_link_text(u"大宗商品交易协议").text
        self.by_xpath("//form/div[2]/div/div/h2/span").click()
        self.get_content1()
        time.sleep(3)
        # //form/div[3]/div/div/h2/span
        self.by_xpath("//form/div[4]/div/div/h2/span").click()
        text = self.get_content2()
    # 实盘开户协议签署点击下一步 然后到个人信息 协议管理 需要纸质合同
    def download_contract(self, nickname, province, city, region, address, phoneno, postId, member, referrer):
        self.userinfo_change_memberNo_after_input_protocol_with_next(self, nickname, province, city, region, address, phoneno, postId, member, referrer)
        self.by_id("applyButton").click()
        self.by_id("applyButton").click()
        self.by_xpath("//div[@id='imgBox']/div[1]/table/tbody/tr/td[2]/a/img").click()
        
    
    
    # 实盘开户协议签署点击下一步 然后到个人信息 协议管理 
    def userinfo_change_memberNo_after_input_protocol_with_next(self, nickname, province, city, region, address, phoneno, postId, member, referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        self.userinfo_agrrement()
        # 返回实盘开户
        # self.open_account_btn()
    # 实盘开户协议签署点击下一步 变更会员 然后到个人信息 协议管理 
    def userinfo_change_memberNo_after_input_protocol(self, nickname, province, city, region, address, phoneno, postId, member, referrer, new_member, new_referrer):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        # 变更会员
        self.click_memberinfo(new_member, new_referrer)
        time.sleep(3)
        # 继续签协议
        self.by_link_text(u"实盘开户").click()
        self.select_memberNo(member, referrer)
        time.sleep(3)
        self.aggrement()
        self.userinfo_agrrement()
        
        # self.aggrement_without_next()
        
        
        # 返回实盘开户
        # self.open_account_btn()
    # 实盘开户上传照片 未点击下一步
    def change_memberNo_after_upload_photo_without_next(self, nickname, province, city, region, address,
                                                        phoneno, postId, member, referrer, new_member,
                                                        new_referrer, frontImg, upcartImg, upselfImg):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        # 上传照片未点击下一步
        self.upload_photo(frontImg, upcartImg, upselfImg)
        
        # 变更会员
        self.change_memberNo(new_member, new_referrer)
        # self.userinfo_click_memberinfo(new_member, new_referrer)
        # 返回实盘开户
        # self.open_account_btn()
    # 实盘开户上传照片 未点击下一步
    def userinfo_change_memberNo_after_upload_photo_without_next(self, nickname, province, city, region, address,
                                                        phoneno, postId, member, referrer, new_member,
                                                        new_referrer, frontImg, upcartImg, upselfImg):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        # 上传照片未点击下一步
        self.upload_photo(frontImg, upcartImg, upselfImg)
        
       
        # self.change_memberNo(new_member, new_referrer)#会员展示
        self.userinfo_click_memberinfo(new_member, new_referrer)  # 会员单位中的变更
        # 返回实盘开户
        # self.open_account_btn()    
    # 实盘开户上传照片 点击下一步
    def change_memberNo_after_upload_photo_with_next(self, nickname, province, city, region, address,
                                                     phoneno, postId, member, referrer, frontImg, upcartImg, upselfImg):
        self.open_account_btn()
        # 填写个人信息
        self.input_userinfo(nickname, province, city, region, address, phoneno, postId)
        # 填写会员信息
        self.select_memberNo(member, referrer)
        # 协议
        self.aggrement()
        # 上传照片
        self.upload_info(frontImg, upcartImg, upselfImg)
        # 变更会员按钮变灰
        self.disable_change_memberNo()
        # 返回实盘开户
        # self.open_account_btn()
    # 获取变更按钮灰色属性
    def disable_change_memberNo(self):
        # self.by_xpath("//input[@id='changeOpen' and @disable='disable']")
        text = self.change_btn().get_attribute("disable")
        return text
    # 下载确认书
    def down_querenshu(self):
        self.open_account_btn()
        self.by_link_text("点击下载《确认书》").click()
        time.sleep(5)
    # 打开手机拍照上传帮助页面
    def photo_uplao_help_page(self):
        self.open_account_btn()
        '''
        url=self.driver.current_url
        self.go_to_help_url()#跳转到上传照片帮助页面
        time.sleep(2)
        self.driver.get(url) #返回上传页面
        time.sleep(5)
        
        '''
        # 第二种方式
        # 切换窗口 关闭所跳转的窗口   
        now_handle = self.driver.current_window_handle  # 获取当前窗口句柄
        print u"当前1%s" % self.driver.current_url
        print now_handle  # 输出当前获取的窗口句柄
        # 点击查看手机拍照上传跳转页面
        self.go_to_help_url()
        time.sleep(5)
        all_handles = self.driver.window_handles  # 获取所有窗口句柄
        for handle in all_handles:
            if handle != now_handle:
                print handle  # 输出待选择的窗口句柄
                self.driver.switch_to_window(handle)
                print u"上传照片%s" % self.driver.current_url
                time.sleep(5)
                self.driver.close()  # 关闭当前窗口
        time.sleep(3)
        print now_handle  # 输出主窗口句柄
        self.driver.switch_to_window(now_handle)  # 返回主窗口
    # 上传身份证图片        
    # 定位上传照片
    def upload_photo(self, frontImg, upcartImg, upselfImg):
        # self.down_querenshu()
        time.sleep(5)
        self.by_id("upcartfront").click()
        self.driver.switch_to_frame(0)
        self.by_id("file").send_keys(frontImg)
        self.by_css("button.btn.button").click()
        self.by_id("upcartrear").click()
        self.driver.switch_to_frame(0)
        self.by_id("file").send_keys(upcartImg)
        self.by_css("button.btn.button").click()
        self.by_id("upselfphoto").click()
        self.driver.switch_to_frame(0)
        self.by_id("file").send_keys(upselfImg)

    def upload_info(self, frontImg, upcartImg, upselfImg):
        self.upload_photo(frontImg, upcartImg, upselfImg)
        self.by_css("button.btn.button").click()
    
    # 定位设置交易密码    
    def update_tradePwd(self, oldpassword, password):
        self.by_id("tpwd").clear()
        self.by_id("tpwd").send_keys(oldpassword)
        self.by_id("tpwdrepeat").clear()
        self.by_id("tpwdrepeat").send_keys(password)
        self.by_id("initPwdSubmit").click()  
    def get_mailContent(self):
        return self.by_id("imgBox")  
    # 设置密码  并获取到实盘开户账户 写入到文件   
    def set_trade_pwd(self, oldpassword, password, file_path):
        # self.open_account_btn()
        self.update_tradePwd(oldpassword, password) 
        # self.driver.switch_to_frame(0)
        grep = self.get_mailContent().get_attribute("innerHTML")
        print grep
        content_text = self.get_content(grep)
        # 把用户名，初始密码写入文件
        self.save_emailInfo(file_path, content_text)
    
        
    # 通过正则获取实盘信息
    def get_re(self):
        url = '<a .*?href="(.*?)".*?>'
        shipan_user = u'您的实盘账号为：(\d+)'
        return url, shipan_user
    # 实盘信息存到list中
    def get_content(self, grep):
        url, shipan_user = self.get_re()
        content_text = []  # 存放从邮箱读取的信息
        bank_sign_url = "".join(re.findall(url, grep)[0])  #
        downlaod_app_url = "".join(re.findall(url, grep)[1])
        shipan_userid = "".join(re.findall(shipan_user, grep))
        self.content_append(content_text, shipan_userid, bank_sign_url, downlaod_app_url)
        print content_text
        return content_text
    # 拼接
    def content_append(self, content_text, shipanuserid, url, downlaod_app_url):
        content_text.append(shipanuserid)
        content_text.append(url)
        content_text.append(downlaod_app_url)
        
    # 写实盘信息
    def wirte_content(self, content_text, file):
        file.write('{"shipan_userid":"%s"' % content_text[0])  # username
        file.write(',\n"bank_sign_url":"%s"' % content_text[1])  # username
        file.write(',\n"download_app_url":"%s"}' % content_text[2])  # app_download
    # 保存文件
    def save_tradeInfo(self, file_path, content_text):
        file = open(file_path, "w")
        self.wirte_content(content_text, file)
        file.close()    
        

    # 协议签署

    def select_agreement_by_js(self):
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
    # 填写协议，点击下一步
    def aggrement(self):
        self.select_agreement_by_js()
        self.by_css("span.btn.syb_btn").click()  # 同意
    # 填写协议，未点击下一步
    def aggrement_without_next(self):
        self.select_agreement_by_js()
    # 选择会员单位推荐人        

    # 修改会员单位名称
    def change_member_name(self, member):
        self.by_id("meList").clear()
        self.by_id("meList").send_keys(member)
        self.by_id("meList").send_keys(Keys.ENTER)

    # 修改会员单位推荐人
    def change_member_id(self, referrer):
        self.by_id("recommender").clear()
        self.by_id("recommender").send_keys(referrer)
        self.by_id("recommender").send_keys(Keys.ENTER)
    # 定位 会员单位和推荐人
    def change_membername_and_referen(self, member, referrer):
        self.change_member_name(member)
        sleep(3)
    # self.by_css("li.ac_even").click()
    # 定位会员简介(需求变更 暂没用到）
    # self.by_xpath("//div[@id='member_remark2_div']/div/table/tbody/tr/td[2]/a/img").click()
        self.change_member_id(referrer)
    # 填写会员单位和推荐人
    def select_memberNo(self, member, referrer):

        self.change_membername_and_referen(member, referrer)
        self.by_id("member_div_botton").click()
        # self.assertEqual(u"实盘账号生成后，将无法再进行会员单位变更", self.close_alert_and_get_its_text())
        
        assert u"实盘账号生成后，将无法再进行会员单位变更" in self.close_alert_and_get_its_text()
    # 个人信息
    def account_info(self, nickname, province, city, region, address, phone, postId, text_m, pic1, pic2, pic3):
       
        # dr.find_element_by_link_text("个人信息").click()
        # self.userinfo_btn()
        # 填写用户信息
        self.input_userinfo(nickname, province, city, region, address, phone, postId)
        
        '''
        #修改密码
        self.by_link_text(u"密码修改").click()
        
        #此处的密码可以从配置文件里面读取
        
        first_login_editpwd.edit_pwd(self,json_data['edit_password'], json_data['re_edit_password'])
        
        sleep(10)
        
        '''
        # 上传证件资料
       
        self.by_link_text(text_m).click()
        self.upload_info(pic1, pic2, pic3)
        
    # 大宗商品
    def dazongproduct(self):
        # return self.by_xpath("input[@type='checkbox']").click()
        return self.by_xpathes("//input[@type='checkbox']").pop(0).click()
            
    # 投资藏品
    def touzhicangpin(self):
        # return self.by_xpath("//form/div[3]/div/label[2]/input").click()
        return self.by_xpathes("//input[@type='checkbox']").pop().click()
    '''
    def input_userinfo(self, nickname, province, city, region, address, phone, postId):
        self.dazongproduct()
        #self.touzhicangpin()
        
        # 修改客户姓名
        self.update_username(nickname)
        
        # 修改性别 定位与个人信息的定位不同所以不能公用
        self.set_sex()
        # 身份证
        self.set_cardID()
        # 省市区
        self.input_address(province, city, region)
        # 通讯地址
        self.get_addressAndPhoneNo(address, phone, postId)
    '''
    # 抽取选择女性信息
    def select_female_info(self, nickname, province, city, region, address):
    # 大宗商品
        self.dazongproduct()
    # 修改客户姓名
        self.update_username(nickname)
    # 修改性别女
        self.set_sex()
    # 身份证
        self.set_cardID()
    # 省市区
        self.input_address(province, city, region)
    # 通讯地址
        self.set_address(address)
    # 填写用户信息性别选择女并且勾选完善资料填写资料
    def input_userinfo(self, nickname, province, city, region, address, phoneno, postId):
        self.select_female_info(nickname, province, city, region, address)
        # 通讯地址
        self.set_phone_postcode(phoneno, postId)
        
    
    # 选择女性并且勾选完善资料只填写phone
    def input_userinfo_with_input_Phone(self, nickname, province, city, region, address, phone):
        self.select_female_info(nickname, province, city, region, address)
        # 填写固定电话
        self.click_radio_with_phone(phone)

    # 抽取选择男性的公共代码
    def select_male_info(self, nickname, province, city, region, address):
        # 大宗商品
        self.dazongproduct()
    # 修改客户姓名
        self.update_username(nickname)
    # 身份证
        self.set_cardID()
    # 省市区
        self.input_address(province, city, region)
    # 通讯地址
        self.set_address(address)
    # 填写用户信息性别默认男不选择勾选完善资料
    def input_userinfo_with_select_male(self, nickname, province, city, region, address):
        self.select_male_info(nickname, province, city, region, address)
    # 填写用户信息性别默认男选择勾选完善资料填写邮编
    def input_userinfo_with_male_with_input_postid(self, nickname, province, city, region, address, postid):
        self.select_male_info(nickname, province, city, region, address)
        self.click_radio_with_postcode(postid)
    # 填写用户信息性别默认男选择勾选完善资料不填手机和邮箱
    def input_userinfo_with_male_with_click_radio(self, nickname, province, city, region, address):
        self.select_male_info(nickname, province, city, region, address)
        # 勾选
        self.click_radio()

    # 开户流程

    def set_member_aggrement_photo(self, memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
        # 会员单位和推荐人
        self.select_memberNo(memberno, referrer)
        # 协议签署
        self.aggrement()
        
        # 照片上传
        self.upload_info(pic1, pic2, pic3)
        self.next_btn()
        self.set_trade_pwd(edit_password, edit_password, filepath)
        '''
        # 设置交易密码
        self.update_tradePwd(edit_password, edit_password)
        sleep(20)
        self.by_css("span.btn").click()
        self.by_css("a > img").click()
        '''
    def open_account_m(self, nickname, province, city, region, address, phone, postId,
                       memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
          
        self.open_account_btn()
        
        self.input_userinfo(nickname, province, city, region, address, phone, postId)
        
        self.set_member_aggrement_photo(memberno, referrer, pic1, pic2, pic3, edit_password, filepath)
    # 女性勾选完善资料填写手机号
    def open_account_with_phone(self, nickname, province, city, region, address, phone, postId,
                       memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
          
        self.open_account_btn()
        self.input_userinfo_with_input_Phone(nickname, province, city, region, address, phone)
        
        self.set_member_aggrement_photo(memberno, referrer, pic1, pic2, pic3, edit_password, filepath)
    # 男性不勾选完善资料
    def open_account_with_male(self, nickname, province, city, region, address,
                       memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
          
        self.open_account_btn()
        self.input_userinfo_with_select_male(nickname, province, city, region, address)
        
        self.set_member_aggrement_photo(memberno, referrer, pic1, pic2, pic3, edit_password, filepath)
    # 男性勾选完善资料不填写手机和邮编
    def open_account_with_click_gouxuanbtn(self, nickname, province, city, region, address,
                       memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
          
        self.open_account_btn()
        self.input_userinfo_with_male_with_click_radio(nickname, province, city, region, address)
        
        self.set_member_aggrement_photo(memberno, referrer, pic1, pic2, pic3, edit_password, filepath)
    # 男性 填写邮编
    def open_account_with_male_inputpostid(self, nickname, province, city, region, address, postId,
                       memberno, referrer, pic1, pic2, pic3, edit_password, filepath):
          
        self.open_account_btn()
        self.input_userinfo_with_male_with_input_postid(nickname, province, city, region, address, postId)
        self.set_member_aggrement_photo(memberno, referrer, pic1, pic2, pic3, edit_password, filepath)        
        '''
        dr.find_element_by_css_selector("a > strong").click()
        dr.find_element_by_css_selector("li.HXBANK.quick").click()
        dr.find_element_by_id("nextButton").click()
        dr.find_element_by_id("nextButton").click()
        '''
