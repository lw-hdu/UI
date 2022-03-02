'''
Descripttion: 
Author: Liuwen
Date: 2022-02-28 16:39:06
LastEditTime: 2022-03-01 10:39:45
'''
from selenium import webdriver

class BaseUtil:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        print('-------start-------')
    
    def teardown_class(self):
        print('-------end-------')
        self.driver.quit()