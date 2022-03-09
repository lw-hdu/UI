'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:32
LastEditTime: 2022-03-09 14:08:25
'''
# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        # self.driver.implicitly_wait(30)
        
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

    #定位鼠标悬停后才显示的元素并返回文本信息
    def locator_mouse_element(self,loc,loc2):
        mouse = self.locator_element(loc)
        ActionChains(self.driver).move_to_element(mouse).perform()
        self.wait(2)
        return self.get_value(loc2)


# driver = webdriver.Chrome()
# bp = BasePage(driver)
# loc = (By.XPATH,'//img[@class="user-avatar"]')
# loc2 = (By.XPATH,'//li[text()=" 退出登录 "]')

# driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys('admin')
# driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('1qaz!QAZ')
# driver.find_element(By.XPATH,'//span[text()=" 登  录 "]').click()
# sleep(3)
# bp.locator_mouse_element(loc,loc2)
