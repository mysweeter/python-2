# -*- coding: utf-8 -*-
"""
Spyder Editor
ctrl +   方法字体
ctrl enter  选中运行
第一题
1.定义一个天气列表。写出里面一周每个温度
2.打印出7天的天气，并且如果是星期三的话，打印星期三是X度

This is a temporary script file.
"""
#数据类型
x=3#int
y='男厕所'#str
a=1.19838493#float
b=True#bool
d=[True,False,False,False,False]#list
c=['男厕所','女厕所','中性']#[type,...]
print(c[0])
print(d[2])
##    print("今天是："+f)
#TypeError: must be str, not int
f=28
print("今天是："+str(f))
float(f)
str(f)
int(f)


#第一题
w=["25","26","27","28","29","30","31"]
print(w[0],w[1],w[2],w[3],w[4],w[5],w[6])

print("星期三是："+str(w[2]))

print("星期三是{}度".format(w[2]))
































