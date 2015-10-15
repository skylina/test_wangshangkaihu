#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年8月19日
Function:base_page
@author: lina
To me :Believe yourself!
'''
from os import sys,path
import time
class BasePage(object):
    url = None
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.accept_next_alert = True

    def url(self):
        return self.url

    def navigate(self):
        self.driver.get(self.url)
        
    def title(self):
        return self.driver.get_title()

    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)
    
    def by_class_name(self, the_name):
        return self.driver.find_element_by_class_name(the_name)
    
    def js(self,js_text):
        return self.driver.execute_script(js_text)

    def by_xpath(self,the_xpath):
        return self.driver.find_element_by_xpath(the_xpath)
    
    def by_xpathes(self,the_xpath):
        return self.driver.find_elements_by_xpath(the_xpath)

    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)
    
    def by_link_text(self,text):
        return self.driver.find_element_by_link_text(text)
    
    def fill_form_by_css(self, form_css,value):
        elem = self.driver.find_element_by_css_selector(form_css)
        elem.send_keys(value)

    def input_form_by_id(self,form_element_id,value):
        return self.driver.find_element_by_id('#%s' % form_element_id,value)
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            print alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    def save_img(self,img_path):
        now = time.strftime("%Y_%m_%d-%H_%M_%S")
        #print now
        pic_path = 'result\\image\\%s%s_.png'%(img_path,now)
        filepath = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), pic_path)
        print filepath
        self.driver.save_screenshot(filepath)
        time.sleep(10)
        #print self.dr.current_url