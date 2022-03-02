'''
Descripttion: 
Author: Liuwen
Date: 2022-03-01 08:48:51
LastEditTime: 2022-03-01 09:51:30
'''
import sys
sys.path.append('D:\\liuwen10\\Desktop\\ui_autotest\\testc')
from classa import A

class Case(A):
    

    def case1(self):
        print('这是类Case，这是第一个方法case1,该类继承类a')
        casea = A(9876536)
        casea.a()

    # def case2(self):
    #     print('这是第一个方法case2')
    #     casea.b()

    

case = Case(2345)
case.case1()