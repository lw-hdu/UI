'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:35:56
LastEditTime: 2022-03-09 14:27:52
'''
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
import logging

class BigScreenPage(BasePage):

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()

    page_screen_loc = (By.XPATH,'//li[@class="el-menu-item"]/span[text()="数据大屏"]')

    def big_screen(self):

        #进入大屏
        self.click(self.page_screen_loc)
        self.log.info(f'大屏定位的元素为{self.page_screen_loc}')
        time.sleep(2)