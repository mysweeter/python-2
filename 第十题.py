# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:12:06 2018

=====================一定要注意文件格式，保存的时候为utf-8
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序

@author: Administrator
"""
print('火车站三字码是：'+'BJX')

"""
    ls=open('./火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence
"""
def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)


#将火车站三字码替换成城市名map{}






#练习十
def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
#print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data1=data['data']['result']
p='  '
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(8),end='')
for a in range(len(data1)):
    b=data1[a]
    print()
    ls=b.split('|')
    ls[6]=data['data']['map'].get('{}'.format(ls[6]))
    ls[7]=data['data']['map'].get('{}'.format(ls[7]))
    if ls[0]=='':
        ls[1]=('不能确定')
    ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],ls[21],ls[23],'--',ls[28],ls[29],ls[26],'--',ls[1]]
    for i in ls:
        if i=='':
            i='--'
            print(str(i).center(11).replace('[','').replace(']',''),end='')

            


          
            
#出发时间排序
t1=[]
for i in range(len(data1)):
    ls=data[i].split('|')
    ls1=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],ls[21],ls[23],'--',ls[28],ls[29],ls[26],'--',ls[1]]
    t1.append(ls1)
mysort=lambda b:b[2][0]
t1.sort(key=mysort)
for x in range(9):
    ls11=ls[x]
    for x in ls11:
        print(str(x).replace('[','').replace(']','').cengter(12),end='')
    print('\n')


#历时排序
t2=[]
for i in range(len(data1)):
    s=data1[i]
    ls=s.split('|')
    ls1=ls[10]
    t2.append(ls1)
sorted(t2)    





#汪清贤做得循环
import urllib.request as r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-11&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=WHN&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)

data=data['data']['result']
p= ' '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
b='车次{}出发站{}到达站{}出发时间{}到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}能否预定{}'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
b=b.split(p)
for t in b:
    print(t.center(10),end='')
print('\t')
def ice(n):
    a=data[n]
    a=a.split('|')
    if a[3].startswith('G'):
        a=[a[3],a[6],a[7],a[8],a[9],a[10],a[32],a[31],a[30],'-','-','-','-','-','-','-',a[11]]
        for i in a:
            print(str(i).center(13),end='')
        print('\t')

for i in range(38):
    ice(i)



















#李月的代码
import urllib.request as r#导入联网工具包，命令为r
data=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(data,from_station,to_station)

url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(data,from_station,to_station).replace("\n","")
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data["data"]["result"]

p=" "
tit="车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注".format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
tit=tit.split(p)
for i in tit:
    print(i.center(10),end='')
print()

####按出发时间排序 
ls=[]
for x in range(9):
    sp=data[x].split('|')
    ls1=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    ls.append(ls1)
mysort=lambda b:b[2][0]
ls.sort(key=mysort)
for i in range(9):
    ls11=ls[i]
    for i in ls11:
        print(str(i).replace("[","").replace("]","").replace(",","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")

####按历时排序 
ls=[]
for x in range(9):
    sp=data[x].split('|')
    ls1=[sp[3],[sp[6],sp[5]],[sp[8],sp[9]],sp[10],sp[32],sp[31],sp[30],"--",sp[23],"--",sp[28],"--",sp[29],sp[26],"--",sp[1]]
    ls.append(ls1)
mysort=lambda b:b[3]
ls.sort(key=mysort)
for i in range(9):
    ls11=ls[i]
    for i in ls11:
        print(str(i).replace("[","").replace("]","").replace(",","").replace("'","") .replace("CXW","重庆西").replace("BXP","北京西").replace("CUW","重庆北").replace("CQW","重庆").center(12),end='')
    print("\n")






