'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-02-28 16:41:38
'''
# -*- coding:utf-8 -*-

# import sys
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\base')
# from base.base_util import BaseUtil
# sys.path.append('D:\\liuwen10\\Desktop\\publicdemo\\pageobject')
from pageobject.power_manage_page import PowerManagePage
from selenium import webdriver
from base.base_util import BaseUtil

class TestPowerManage(BaseUtil):
    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     print('-------start power manage-------')
    
    # def teardown_class(self):
    #     print('-------end power manage-------')
    #     self.driver.quit()

    def test_select_power(self):

        pm = PowerManagePage(self.driver)
        pm.select_power()