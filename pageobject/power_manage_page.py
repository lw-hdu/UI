'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-09 15:46:13
'''
# -*- coding:utf-8 -*-

import time
from selenium.webdriver.common.by import By
import sys
sys.path.append('D:\\liuwen10\\Desktop\\ui_autotest\\base')
from base_page import BasePage
from selenium import webdriver

class PowerManagePage(BasePage):

    #页面元素
    power_manager_loc = (By.XPATH,'//li[@class="el-menu-item"]')
    select_loc = (By.XPATH,'//input[@placeholder="请输入电站名称"]')
    button_loc = (By.XPATH,'//span[text()=" 查询 "]')

    reset_loc = (By.XPATH,'//span[text()=" 重置 "]')
    status_loc = (By.XPATH,'//input[@placeholder="状态"]')
    alarm_loc = (By.XPATH,'/html/body/div[2]/div/div/ul/li[3]')

    #查询电站名称定位
    station_name = (By.XPATH,'//div[@class="station-stationName-group"]/h3')
    #查询电站状态定位
    station_status = (By.XPATH,'//div[@class="power_status_content"]/span')

    
    #页面动作
    def input_power(self):
        #根据输入的电站名称查询
        self.click(self.power_manager_loc)
        time.sleep(1)
        self.send_keys(self.select_loc,"空港")
        time.sleep(1)
        self.click(self.button_loc)
        time.sleep(3)
        
    def select_power(self):
        #清空查询条件
        self.click(self.reset_loc)
        time.sleep(1)
        #通过下拉框选择状态查询
        self.click(self.status_loc)
        time.sleep(2)
        self.click(self.alarm_loc)
        time.sleep(1)
        self.click(self.button_loc)
        time.sleep(2)

    #断言
    def get_input_station_text(self):
        return self.get_value(self.station_name)

    def get_select_station_text(self):
        return self.get_value(self.station_status)
