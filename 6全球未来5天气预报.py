# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。



@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量
data['list'][0]['main']['temp_max']
#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量
data['list'][0]['main']['temp_min']

#第四题(1)
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

#2018-06-21 06:00:00
a1=print('2018-06-21 06:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][0]['main']['temp'],
              data['list'][0]['weather'][0]['description'],
              data['list'][0]['main']['pressure'],
              data['list'][0]['main']['temp_max'],
              data['list'][0]['main']['temp_min'],
              ))
#2018-06-21 12:00:00
a2=print('2018-06-21 12:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][2]['main']['temp'],
              data['list'][2]['weather'][0]['description'],
              data['list'][2]['main']['pressure'],
              data['list'][2]['main']['temp_max'],
              data['list'][2]['main']['temp_min'],
              ))
#2018-06-21 18:00:00
a3=print('2018-06-21 18:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][4]['main']['temp'],
              data['list'][4]['weather'][0]['description'],
              data['list'][4]['main']['pressure'],
              data['list'][4]['main']['temp_max'],
              data['list'][4]['main']['temp_min'],
              ))
b1=print('建议：今天有小雨，不适合户外运动，出门请记得带伞，平均气温在23度左右，感觉冷的话可以适当加衣')
#2018-06-22 06:00:00
a4=print('2018-06-22 06:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][8]['main']['temp'],
              data['list'][8]['weather'][0]['description'],
              data['list'][8]['main']['pressure'],
              data['list'][8]['main']['temp_max'],
              data['list'][8]['main']['temp_min'],
              ))
#2018-06-22 12:00:00
a5=print('2018-06-22 12:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][10]['main']['temp'],
              data['list'][10]['weather'][0]['description'],
              data['list'][10]['main']['pressure'],
              data['list'][10]['main']['temp_max'],
              data['list'][10]['main']['temp_min'],
              ))
#2018-06-22 18:00:00
a6=print('2018-06-22 18:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][12]['main']['temp'],
              data['list'][12]['weather'][0]['description'],
              data['list'][12]['main']['pressure'],
              data['list'][12]['main']['temp_max'],
              data['list'][12]['main']['temp_min'],
              ))
b2=print('建议：今天上午有小雨，下午有大雨，不适合户外运动，出门请记得带伞，平均气温在23度左右，感觉冷的话可以适当加衣')
#2018-06-23 06:00:00
a7=print('2018-06-23 06:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][16]['main']['temp'],
              data['list'][16]['weather'][0]['description'],
              data['list'][16]['main']['pressure'],
              data['list'][16]['main']['temp_max'],
              data['list'][16]['main']['temp_min'],
              ))
#2018-06-23 12:00:00
a8=print('2018-06-23 12:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][18]['main']['temp'],
              data['list'][18]['weather'][0]['description'],
              data['list'][18]['main']['pressure'],
              data['list'][18]['main']['temp_max'],
              data['list'][18]['main']['temp_min'],
              ))
#2018-06-23 18:00:00
a9=print('2018-06-23 18:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][20]['main']['temp'],
              data['list'][20]['weather'][0]['description'],
              data['list'][20]['main']['pressure'],
              data['list'][20]['main']['temp_max'],
              data['list'][20]['main']['temp_min'],
              ))
b3=print('建议：今天一天都有小雨，不适合户外运动，出门请记得带伞，平均气温在24度左右')
#2018-06-24 06:00:00
a10=print('2018-06-24 06:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][24]['main']['temp'],
              data['list'][24]['weather'][0]['description'],
              data['list'][24]['main']['pressure'],
              data['list'][24]['main']['temp_max'],
              data['list'][24]['main']['temp_min'],
              ))
#2018-06-24 12:00:00
a11=print('2018-06-24 12:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][26]['main']['temp'],
              data['list'][26]['weather'][0]['description'],
              data['list'][26]['main']['pressure'],
              data['list'][26]['main']['temp_max'],
              data['list'][26]['main']['temp_min'],
              ))
#2018-06-24 18:00:00
a12=print('2018-06-24 18:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][28]['main']['temp'],
              data['list'][28]['weather'][0]['description'],
              data['list'][28]['main']['pressure'],
              data['list'][28]['main']['temp_max'],
              data['list'][28]['main']['temp_min'],
              ))
b4=print('建议：今天上午有中雨，不适合户外运动，出门请记得带伞，下午是多云，可以出门散步，呼吸新鲜空气，平均气温在25度左右')
#2018-06-25 06:00:00
a13=print('2018-06-25 06:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][32]['main']['temp'],
              data['list'][32]['weather'][0]['description'],
              data['list'][32]['main']['pressure'],
              data['list'][32]['main']['temp_max'],
              data['list'][32]['main']['temp_min'],
              ))
#2018-06-25 12:00:00
a14=print('2018-06-25 12:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][34]['main']['temp'],
              data['list'][34]['weather'][0]['description'],
              data['list'][34]['main']['pressure'],
              data['list'][34]['main']['temp_max'],
              data['list'][34]['main']['temp_min'],
              ))
#2018-06-25 18:00:00
a15=print('2018-06-25 18:00:00{}的温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{},'
      .format(
              data['city']['name'],
              data['list'][36]['main']['temp'],
              data['list'][36]['weather'][0]['description'],
              data['list'][36]['main']['pressure'],
              data['list'][36]['main']['temp_max'],
              data['list'][36]['main']['temp_min'],
              ))
b5=print('建议：今天的天气是多云，可以出门运动，呼吸新鲜空气，平均气温在25度左右')


#2018-06-21 06:00:00
a1=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][0]['dt_txt'],
              data['city']['name'],
              data['list'][0]['main']['temp'],
              data['list'][0]['weather'][0]['description'],
              data['list'][0]['main']['pressure'],
              data['list'][0]['main']['temp_max'],
              data['list'][0]['main']['temp_min'],
              ))
#2018-06-21 12:00:00
a2=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][2]['dt_txt'],
              data['city']['name'],
              data['list'][2]['main']['temp'],
              data['list'][2]['weather'][0]['description'],
              data['list'][2]['main']['pressure'],
              data['list'][2]['main']['temp_max'],
              data['list'][2]['main']['temp_min'],
              ))
#2018-06-21 18:00:00
a3=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][4]['dt_txt'],
              data['city']['name'],
              data['list'][4]['main']['temp'],
              data['list'][4]['weather'][0]['description'],
              data['list'][4]['main']['pressure'],
              data['list'][4]['main']['temp_max'],
              data['list'][4]['main']['temp_min'],
              ))
#2018-06-22 06:00:00
a1=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][8]['dt_txt'],
              data['city']['name'],
              data['list'][8]['main']['temp'],
              data['list'][8]['weather'][0]['description'],
              data['list'][8]['main']['pressure'],
              data['list'][8]['main']['temp_max'],
              data['list'][8]['main']['temp_min'],
              ))
#2018-06-22 12:00:00
a2=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][10]['dt_txt'],
              data['city']['name'],
              data['list'][10]['main']['temp'],
              data['list'][10]['weather'][0]['description'],
              data['list'][10]['main']['pressure'],
              data['list'][10]['main']['temp_max'],
              data['list'][10]['main']['temp_min'],
              ))
#2018-06-22 18:00:00
a3=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][12]['dt_txt'],
              data['city']['name'],
              data['list'][12]['main']['temp'],
              data['list'][12]['weather'][0]['description'],
              data['list'][12]['main']['pressure'],
              data['list'][12]['main']['temp_max'],
              data['list'][12]['main']['temp_min'],
              ))
#2018-06-23 06:00:00
a1=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][16]['dt_txt'],
              data['city']['name'],
              data['list'][16]['main']['temp'],
              data['list'][16]['weather'][0]['description'],
              data['list'][16]['main']['pressure'],
              data['list'][16]['main']['temp_max'],
              data['list'][16]['main']['temp_min'],
              ))
#2018-06-23 12:00:00
a2=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][18]['dt_txt'],
              data['city']['name'],
              data['list'][18]['main']['temp'],
              data['list'][18]['weather'][0]['description'],
              data['list'][18]['main']['pressure'],
              data['list'][18]['main']['temp_max'],
              data['list'][18]['main']['temp_min'],
              ))
#2018-06-23 18:00:00
a3=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][20]['dt_txt'],
              data['city']['name'],
              data['list'][20]['main']['temp'],
              data['list'][20]['weather'][0]['description'],
              data['list'][20]['main']['pressure'],
              data['list'][20]['main']['temp_max'],
              data['list'][20]['main']['temp_min'],
              ))
#2018-06-24 06:00:00
a1=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][24]['dt_txt'],
              data['city']['name'],
              data['list'][24]['main']['temp'],
              data['list'][24]['weather'][0]['description'],
              data['list'][24]['main']['pressure'],
              data['list'][24]['main']['temp_max'],
              data['list'][24]['main']['temp_min'],
              ))
#2018-06-24 12:00:00
a2=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][26]['dt_txt'],
              data['city']['name'],
              data['list'][26]['main']['temp'],
              data['list'][26]['weather'][0]['description'],
              data['list'][26]['main']['pressure'],
              data['list'][26]['main']['temp_max'],
              data['list'][26]['main']['temp_min'],
              ))
#2018-06-24 18:00:00
a3=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][28]['dt_txt'],
              data['city']['name'],
              data['list'][28]['main']['temp'],
              data['list'][28]['weather'][0]['description'],
              data['list'][28]['main']['pressure'],
              data['list'][28]['main']['temp_max'],
              data['list'][28]['main']['temp_min'],
              ))
#2018-06-25 06:00:00
a1=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][32]['dt_txt'],
              data['city']['name'],
              data['list'][32]['main']['temp'],
              data['list'][32]['weather'][0]['description'],
              data['list'][32]['main']['pressure'],
              data['list'][32]['main']['temp_max'],
              data['list'][32]['main']['temp_min'],
              ))
#2018-06-25 12:00:00
a2=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][34]['dt_txt'],
              data['city']['name'],
              data['list'][34]['main']['temp'],
              data['list'][34]['weather'][0]['description'],
              data['list'][34]['main']['pressure'],
              data['list'][34]['main']['temp_max'],
              data['list'][34]['main']['temp_min'],
              ))
#2018-06-25 18:00:00
a3=print('time:{},city:{},temp:{},weather:{},pressure:{},temp_max:{},temp_min:{},'
      .format(data['list'][36]['dt_txt'],
              data['city']['name'],
              data['list'][36]['main']['temp'],
              data['list'][36]['weather'][0]['description'],
              data['list'][36]['main']['pressure'],
              data['list'][36]['main']['temp_max'],
              data['list'][36]['main']['temp_min'],
              ))

#根据温度打印出问题折线图
temp1=data['list'][0]['main']['temp']
temp2=data['list'][2]['main']['temp']
temp3=data['list'][4]['main']['temp']
temp4=data['list'][8]['main']['temp']
temp5=data['list'][10]['main']['temp']
temp6=data['list'][12]['main']['temp']
temp7=data['list'][16]['main']['temp']
temp8=data['list'][18]['main']['temp']
temp9=data['list'][20]['main']['temp']

print(int(temp1)*"-")
print(int(temp2)*"-")
print(int(temp3)*"-")
print(int(temp4)*"-")
print(int(temp5)*"-")
print(int(temp6)*"-")
print(int(temp7)*"-")
print(int(temp8)*"-")
print(int(temp9)*"-")



#计算出天气排名，按着大到小的顺序
ls=[]
ls.append(data['list'][0]['main']['temp'])
ls.append(data['list'][2]['main']['temp'])
ls.append(data['list'][4]['main']['temp'])
ls.append(data['list'][8]['main']['temp'])
ls.append(data['list'][10]['main']['temp'])
ls.append(data['list'][12]['main']['temp'])
ls.append(data['list'][16]['main']['temp'])
ls.append(data['list'][18]['main']['temp'])
ls.append(data['list'][20]['main']['temp'])
ls=sorted(ls)
ls1=reversed(ls) 
print(ls1)
for i in ls1:
    print(i)




def msg(b):
          a1=data['city']['name'],
          a2=data['list'][b]['dt_txt'],
          a3=data['list'][b]['main']['temp'],
          a4=data['list'][b]['weather'][0]['description'],
          a5=data['list'][b]['main']['pressure'],
          a6=data['list'][b]['main']['temp_max'],
          a7=data['list'][b]['main']['temp_min'],
          print('城市是{},时间是{},温度是{},天气情况是{},气压是{},最高温度是{},最低温度是{}'
          .format(a1,a2,a3,a4,a5,a6,a7))
msg(0)
msg(2)
msg(4)
msg(8)
msg(10)
msg(12)
msg(16)
msg(18)
msg(20)
msg(24)
msg(26)
msg(28)
msg(32)
msg(34)
msg(36)

def msg(b):
          a1=data['list'][b]['dt_txt']
          a2=data['list'][b]['main']['temp']
          print(a1,int(a2)*'-',a2)
msg(0)
msg(2)
msg(4)
msg(8)
msg(10)
msg(12)
msg(16)
msg(18)
msg(20)
msg(24)
msg(26)
msg(28)
msg(32)
msg(34)
msg(36)          

