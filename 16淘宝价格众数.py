# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:02:29 2018
1.获得不重复的列表set()
2.求列表中每个元素的个数  元素-个数
3.根据列表中 每个元素-个数 的个数排序(升序)
4.求得最后的元素
@author: Administrator
"""
ls=[28,30,10,10,10,10,39.9]
l=set(ls)
myls=[]
for i in l:
    myls.append('{}-{}'.format(i,ls.count(i)))

mysort=lambda x:int(x.split('-')[1])
myls.sort(key=mysort,reverse=True)#降序，列表中的每个元素都会调用一次mysort函数
zhongshu=myls[0].split('-')
print('出现次数对多的元素是：{} 次数是：{}'.format(zhongshu[0],zhongshu[1]))
#

###################匿名函数 lambda函数
def x(i):
    return i*i

x(3)

xx=lambda i:i*i
xx(4)




















