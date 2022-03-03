'''
Descripttion: 
Author: Liuwen
Date: 2021-12-10 10:45:15
LastEditTime: 2022-03-03 11:02:10
'''

from pageobject.login_page import LoginPage
from pageobject.big_screen_page import BigScreenPage
from base.base_util import BaseUtil


class TestBigScreen(BaseUtil):

        
    def test_bigscreen(self):
        #登录
        lp = LoginPage(self.driver)
        lp.login()
        #进入大屏
        bs = BigScreenPage(self.driver)
        bs.big_screen()
        
