'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:45:15
LastEditTime: 2022-03-03 09:37:36
'''
from selenium import webdriver
from pageobject.login_page import LoginPage
from pageobject.big_screen_page import BigScreenPage
from base.base_util import BaseUtil


class TestBigScreen(BaseUtil):
    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     print('-------start big screen-------')
    
    # def teardown_class(self):
    #     print('-------end big screen-------')
    #     self.driver.quit()

        
    def test_bigscreen(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        #进入大屏
        bs = BigScreenPage(self.driver)
        bs.big_screen()
        
