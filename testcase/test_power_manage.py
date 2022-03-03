'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-03 09:34:17
'''
# -*- coding:utf-8 -*-

# import sys
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
# from base.base_util import BaseUtil
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\pageobject')
import time
from pageobject.login_page import LoginPage
from pageobject.power_manage_page import PowerManagePage
from selenium import webdriver
from base.base_util import BaseUtil

class TestPowerManage(BaseUtil):

    def test_select_power(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        time.sleep(3)

        pm = PowerManagePage(self.driver)
        pm.select_power()