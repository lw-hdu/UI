'''
Descripttion: 
Author: Liuwen
Date: 2022-03-01 08:45:15
LastEditTime: 2022-03-01 09:40:44
'''
class A:
    def __init__(self,i) -> None:
        self.i = i
    def a(self):
        print(f'这是类A的方法a,调用类A时需要传入参数{self.i}')
    
    def b(self):
        print('这是类A的方法b')


# a = A(3)
# a.a()