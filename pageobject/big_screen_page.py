'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:35:56
LastEditTime: 2022-03-02 09:40:58
'''
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pageobject.login_page import LoginPage

class BigScreenPage(BasePage):

    page_screen_loc = (By.XPATH,'//li[@class="el-menu-item"]/span[text()="数据大屏"]')

    def big_screen(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        time.sleep(3)
        #进入大屏
        self.click(BigScreenPage.page_screen_loc)
        time.sleep(2)

