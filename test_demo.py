'''
Descripttion: 
Author: Liuwen
Date: 2022-01-19 09:14:11
LastEditTime: 2022-01-19 09:14:11
'''
import time

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(chrome_options=option)

driver.get("http://10.0.10.131/")
driver.add_cookie('cook')