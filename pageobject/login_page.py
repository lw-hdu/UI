'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-01 10:39:48
'''
# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By
# import sys
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
from base.base_page import BasePage
import time
# import base.base_util 


class LoginPage(BasePage):   
    #页面的元素
    #输入用户名
    username_loc = (By.XPATH,'//input[@placeholder="请输入用户名"]')
    #输入密码
    password_loc = (By.XPATH,'//input[@placeholder="请输入密码"]')
    #登录按钮
    submit_loc = ((By.XPATH,'//span[text()=" 登  录 "]'))
    # tuichu_loc = (By.LINK_TEXT,'退出')

    #页面的动作
    def login(self,username="admin",password="1qaz!QAZ"):
        self.send_keys(self.username_loc,username)
        self.send_keys(self.password_loc,password)
        self.click(self.submit_loc)
        time.sleep(2)
        

    #断言
    # def get_except_result(self):
    #     self.goto_frame("header-frame")
    #     return self.get_value(LoginPage.tuichu_loc)


