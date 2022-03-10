'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-10 14:37:55
'''
import pytest
from pageobject.login_page import LoginPage
from common.read_excel import ReadExcel
from base.base_util import BaseUtil
import logging
import allure

class TestLogin(BaseUtil):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    
    @allure.title('登录测试')
    #@pytest.mark.skip()
    @pytest.mark.parametrize("id,username,password",ReadExcel().get_xls())
    def test_login(self,id,username,password):
        """ 登录 """
        self.log.info(f'这是第{id}条用例，输入的用户名为{username},密码为{password}')
        loginpage = LoginPage(self.driver)
        loginpage.login(username,password)
     
        # 断言
        if id == 3:
            assert loginpage.get_expect_result() == '退出登录'
            self.log.info('--登陆成功--')
        else:
            pass