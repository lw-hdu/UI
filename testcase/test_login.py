'''
Descripttion: 
Author: Liuwen
Date: 2021-12-09 14:42:33
LastEditTime: 2022-03-02 10:02:38
'''
import pytest
# from ddt import ddt, data, unpack
# from base.base_util import BaseUtil
# from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage
from common.read_excel import ReadExcel
from base.base_util import BaseUtil
#@ddt

class TestLogin(BaseUtil):
    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     print('-------start login-------')
    
    # def teardown_class(self):
    #     print('-------end login-------')
    #     self.driver.quit()
    
    # @data(*ExcelUtil().read_excel())
    # @unpack
    @pytest.mark.parametrize("id,username,password",ReadExcel().get_xls())
    def test_login(self,id,username,password):
        """ 登录 """
        loginpage = LoginPage(self.driver)
        loginpage.login(username,password)
        # if index==1:
        #     # 断言
        #     #self.assertEqual(lp.get_except_result(),'退出')
        #     assert lp.get_except_result() == '退出'