'''
Descripttion: 用于实现登录页面对象的文件
              包含核心元素定位、核心业务流程
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-09 14:03:35
'''
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import time
import logging


class LoginPage(BasePage):   

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    #页面的元素（用元祖管理元素）
    #输入用户名
    username_loc = (By.XPATH,'//input[@placeholder="请输入用户名"]')
    #输入密码
    password_loc = (By.XPATH,'//input[@placeholder="请输入密码"]')
    #登录按钮
    submit_loc = (By.XPATH,'//span[text()=" 登  录 "]')
    # 登录成功后右上角“退出登录”定位
    loc = (By.XPATH,'//img[@class="user-avatar"]')
    loc2 = (By.XPATH,'//li[text()=" 退出登录 "]')

    #页面的动作
    def login(self,username="admin",password="1qaz!QAZ"):
        self.send_keys(self.username_loc,username)
        self.send_keys(self.password_loc,password)
        self.click(self.submit_loc)
        self.log.info('---登录成功---')
        time.sleep(2)

    #断言
    def get_expect_result(self):
        return self.locator_mouse_element(self.loc,self.loc2)
        
# driver = webdriver.Chrome()
# lp = LoginPage(driver)
# lp.login()
# lp.get_expect_result()


