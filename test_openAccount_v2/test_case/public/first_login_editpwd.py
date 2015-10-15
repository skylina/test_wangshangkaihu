#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年7月22日
Function:
@author: lina
To me :Believe yourself!
'''
from os import sys,path
import  time
from selenium import webdriver
import unittest

# 第一次用户名和密码是从注册邮箱里面读取到的，这里没有完善完
def edit_pwd(self,oldpassword,password): 
    dr = self.driver
    dr.find_element_by_id("oldpassword").clear()  
    dr.find_element_by_id("oldpassword").send_keys(oldpassword)   
    dr.find_element_by_id("password").clear()     
    dr.find_element_by_id("password").send_keys(password)      
    dr.find_element_by_id("repassword").clear()     
    dr.find_element_by_id("repassword").send_keys(password)   
    dr.find_element_by_id("submit-button").click()  
    dr.find_element_by_id("yesButton").click()