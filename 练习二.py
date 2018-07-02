# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:01:56 2018
字典dict：
{str:type,...}
第二题：
1.定义一个字典：里面存储7天的天气信息，信息有：7天的温度，7天的天气情况，今天最高温度
2.打印星期三的温度和天气情况，以及打印今天的最高温度
@author: Administrator
"""
msg={"phone":10086,"内容":'查询话费','发送日期':'20180620'}
msg['phone']
msg['内容']
####################基础功能
xuezhiqian={'name':'薛之谦','songs':['丑八怪','演员','认真的雪']}
xuezhiqian['songs'][1]


#第二题
tianqi={"temp":['21','22','23','24','25','26','27'],"weather":['晴','晴','多云','晴','多云','小雨','晴'],"Htemp":['30','31','32','33','34','35','36']}
print(tianqi["temp"][2])
print(tianqi["weather"][2])
print(tianqi["Htemp"][2])