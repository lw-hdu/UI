'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:45:15
LastEditTime: 2022-02-28 16:41:11
'''
from selenium import webdriver
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
        bs = BigScreenPage(self.driver)
        bs.big_screen()
        
