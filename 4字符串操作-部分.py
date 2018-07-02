# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:27:19 2018
str的操作
代码自动补全快捷键：tab

@author: Administrator
"""
#占位符，动态内容
"今天温度是{}".format(28)
'q={}'.format('北京')
'我来自北京'[2]

s='2018-06-21 03:00:00'  #字符串=list
s=list(s)
s[0]   #获取单个数
s[0:10] #['2', '0', '1', '8', '-', '0', '6', '-', '2', '1']
s='2018-06-21 03:00:00'  #字符串=list
s[0:10]#'2018-06-21'         切片
s[11:19]#'03:00:00'


s[-1:]    #逆序截取
s[-9:]
#################
s.index('-21')#获取子字符串的位置

s.endswith('00:00')#True  是不是以xxx结束
s.startswith('2018')
len(s)

'Qqyulan'.lower()#变成小写
'Qqyulan'.upper()#变成大写


mima=input('请输入你的银行卡密码：')
print(mima)


t='2018-06-21 11:44:00'
t=list(t)
t[0:15]
t[1:]
t[-5:]
t='2018-06-21 11:44:00'
t[0:10]
t[0:1]

t[-9:]

t.index('-06-')
t.endswith('44:00')
t.startswith('2018')
len(t)
'idsofuiodhvsd'.upper()
'HFVUISHFSHIUS'.lower()
phone=input('请输入你的电话号码：')
print(phone)
