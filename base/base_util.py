'''
Descripttion: 
Author: Liuwen
Date: 2022-02-28 16:39:06
LastEditTime: 2022-03-17 10:38:23
'''
from selenium import webdriver

class BaseUtil:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(10)
        self.driver.get("http://10.0.10.131/")
        self.driver.maximize_window()
        # self.driver = webdriver.Chrome()
        print('-------浏览器启动-------')
    
    def teardown(self):
        print('-------浏览器关闭-------')
        self.driver.quit()