'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-09 15:44:10
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
import allure
import pytest

class TestPowerManage(BaseUtil):
    
    #@pytest.mark.skip()
    @allure.title('电站查询测试')
    def test_select_power(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        # time.sleep(3)
        
        pm = PowerManagePage(self.driver)
        #根据电站名称查询
        pm.input_power()
        #断言
        assert pm.get_input_station_text() == '空港'

        #根据电站状态查询
        pm.select_power()
        #断言
        assert pm.get_select_station_text() == '告警'
