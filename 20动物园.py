# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:53:44 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例

@author: Administrator
"""
monkey={"绰号":'星期五','公母':'公','毛色':'黄色','猴龄':'3'}

print(monkey['绰号'])
monkey.suanshu(1,1)
#####这就是一个类，猴子类
class Monkey:
    #猴子对象产生的时候，会调用这个方法Monkey()
    def __init__(self,name,sex,color,age):#########系统固定的方法
        self.name=name
        self.sex=sex
        self.color=color
        self.age=age
    def calc(self,x,y):#self 有对象
        print(x+y)
    def bike(self):
        print(self.name+'猴子以20迈的速度正在前进')
a=Monkey('星期五','公','黄色','3')
print(a.name)
print(a.sex)
print(a.color)
print(a.age)################静态信息
a.calc(1,1)
b=Monkey('灵明石猴','公','黄色','800')
b.bike()


#练习十五
class Weather:
    def __init__(self,time,temp,description,pressure):
        self.time=time
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print('当前天气属性:时间 {},温度 {},天气情况 {},气压 {}'.format(self.time,self.temp,self.description,self.pressure))
a=Weather('2018年6月29日','30','阴','800')
b=Weather('2018年6月30日','35','晴','900')
c=Weather('2018年7月01日','35','晴','1000')
a.msg()
b.msg()
c.msg()



#练习十六
f=open('./全国招生计划表0206C正确.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('"plan":"(.*?)",',re.S).findall(s)
a=0
for i in range(len(s1)):
    a=a+int(s1[i])
print('全国高校总人数:{}'.format(a))



area={'陕西':'西北','宁夏':'西北','新疆':'西北','青海':'西北','甘肃':'西北',
      '黑龙江':'东北','吉林':'东北','辽宁':'东北',
      '北京':'华北','天津':'华北','河北':'华北','山西':'华北','内蒙古':'华北',
      '广东':'华南','广西':'华南','海南':'华南',
      '重庆':'西南','四川':'西南','贵州':'西南','云南':'西南','西藏':'西南',
      '河南':'华中','湖南':'华中','湖北':'华中',
      '上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','福建':'华东','江西':'华东','山东':'华东'}


areaplan={'西北':0,'东北':0,'华北':0,'华南':0,'西南':0,'华中':0,'华东':0}
f=open('./全国招生计划表0206C正确.txt','r',encoding='utf-8')
ls=f.readlines()#将所有的文本中的每行读取到一个列表中去
import json
for i in range(len(ls)):
    ls[i]=json.loads(ls[i])
    if ls[i]['status']==1:
        for x in range(len(ls[i]['data'])):
            plan=ls[i]['data'][x]['plan']
            city=ls[i]['data'][x]['city']
            areaplan[area[city]]=areaplan[area[city]]+int(plan)
print('西北招生人数{}\n东北招生人数{}\n华北招生人数{}\n华南招生人数{}\n西南招生人数{}\n华中招生人数{}\n华东招生人数{}\n'
      .format(areaplan['西北'],areaplan['东北'],areaplan['华北'],areaplan['华南'],areaplan['西南'],areaplan['华中'],areaplan['华东']))
print('全国高校总人数:{}'.format(a))





    















