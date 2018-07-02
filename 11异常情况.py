# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:10:02 2018
生活当中的异常:
    上课断网(解决方案手机热点)，上课断电(黑板)，关系异常(投入事业)
程序中的异常：
    3/0除数不能为零(程序异常机制)
    int('39人付款')(把人付款去掉)
@author: Administrator
"""
3/0#ZeroDivisionError: division by zero
int('39人付款')#ValueError: invalid literal for int() with base 10: '39人付款'

print(3/1)
print(2/1)
print(2/1)
try:
    print(3/0)#
except Exception as err:
    print('除数不能为零')#err.args异常的情况
print(4/2)















