'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:35:56
LastEditTime: 2022-03-03 10:05:28
'''
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class BigScreenPage(BasePage):

    page_screen_loc = (By.XPATH,'//li[@class="el-menu-item"]/span[text()="数据大屏"]')

    def big_screen(self):

        #进入大屏
        self.click(BigScreenPage.page_screen_loc)
        time.sleep(2)