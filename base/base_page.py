'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:32
LastEditTime: 2022-03-02 15:41:34
'''
# -*- coding:utf-8 -*-


from time import sleep
from selenium.webdriver.support.select import Select

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://10.0.10.131/'
        self.driver.get(self.url)
        self.driver.maximize_window()
        
    #打开指定的url
    def open_url(self,url):
        self.driver.get(url)

    #定位元素的关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    #设置值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #单击的关键字
    def click(self,loc):
        self.locator_element(loc).click()

    def wait(self,time):
        sleep(time)

    #进入框架的关键字
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    #出框架的关键字
    def quit_frame(self):
        self.driver.switch_to.default_content()

    #封装选中下拉框关键字
    def choice_select(self,loc,value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    #获取文本的值
    def get_value(self,loc):
        return self.locator_element(loc).text