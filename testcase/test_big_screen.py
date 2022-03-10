'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:45:15
LastEditTime: 2022-03-10 14:37:51
'''

from pageobject.login_page import LoginPage
from pageobject.big_screen_page import BigScreenPage
from base.base_util import BaseUtil
import pytest
import allure


class TestBigScreen(BaseUtil):

    #@pytest.mark.skip()
    @allure.title('大屏测试')
    def test_bigscreen(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        #进入大屏
        bs = BigScreenPage(self.driver)
        bs.big_screen()
        
