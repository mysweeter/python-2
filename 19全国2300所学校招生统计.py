# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:22:13 2018
ctrl+1 注释代码
@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
req=r.Request(url,headers=headers,data='id=477&type=2&city=23&state=1'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')

#东北
#黑龙江	吉林 	辽宁
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan={'东北':0}
areaplan['东北']=areaplan['东北']+8
###########通过下面定义多个变量赋值，计算出中国地区的人数
a=0
b=0
c=0
if '东北'==plan:
   a=a+1 

import json
data=json.loads(data)

for i in range(2300):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
        
#d='id=477&type=2&city=23&state=1'.encode()#bytes
#
#print(d)
#print(type(d))




f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
s2=re.compile('.*?\t').findall(s)
for i in range(len(s1)):
    print('学校：{}学校代码：{}'.format(s2[i*2],s1[i]))
f.close()

area={'陕西':'西北','青海':'西北','甘肃':'西北'}
areaplan={'西北':0}
    
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for x in s1:
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
    req=r.Request(url,headers=headers,data='id={}&type=2&city=63&state=1'.format(x).encode())
    data=r.urlopen(req).read().decode('utf-8','ignore')        
    
import json
data=json.loads(data)

for i in range(len(s1)):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
#        print(area[city])
#        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])        
        
        
ls=[]
f=open('./陈建-甘肃-文科-招生数据.txt','r')
ls1=f.readlines()
ls.append(ls1)      
f=open('./李月-陕西-理科-招生数据.txt','r')
ls2=f.readlines()
ls.append(ls2)        
f=open('./邱令-甘肃-理科-招生数据.txt','r')
ls3=f.readlines()
ls.append(ls3)        
f=open('./石媛-青海-文科-招生数据.txt','r')
ls4=f.readlines()
ls.append(ls4)       
f=open('./王军林-青海-理科-招生数据.txt','r')
ls5=f.readlines()
ls.append(ls5)
f=open('./谢吉-陕西-文科-招生数据.txt','r')
ls6=f.readlines()
ls.append(ls6)
import json
for i in range(len(ls)):
    for x in range(len(ls[i])):
        if ls[i][x]['status']==1:
            12=len(ls[i][x]['data'])
            for c in range(12):
                b=b+int(ls[i][x]['data'][c]['plan'])
                d=d+int(ls[i][x]['data'][c]['plan'])
    print('{}的招生人数是:{}'.format(ls7[i],d))
            




f=open('./青海理科.txt','r',encoding='utf-8')
s1=f.read()
import re
s11=re.compile('"plan":"(.*?)",',re.S).findall(s1)
a=0
for i in range(len(s11)):
    a=a+int(s11[i])


f=open('./陈建-甘肃-文科-招生数据.txt','r',encoding='utf-8')
s2=f.read()
import re
s22=re.compile('"plan":"(.*?)",',re.S).findall(s2)
b=0
for i in range(len(s22)):
    b=b+int(s22[i])


f=open('./李月-陕西-理科-招生数据.txt','r',encoding='utf-8')
s3=f.read()
import re
s33=re.compile('"plan":"(.*?)",',re.S).findall(s3)
c=0
for i in range(len(s33)):
    c=c+int(s33[i])


f=open('./邱令-甘肃-理科-招生数据.txt','r',encoding='utf-8')
s4=f.read()
import re
s44=re.compile('"plan":"(.*?)",',re.S).findall(s4)
d=0
for i in range(len(s44)):
    d=d+int(s44[i])

        
f=open('./石媛-青海-文科-招生数据.txt','r',encoding='utf-8')
s5=f.read()
import re
s55=re.compile('"plan":"(.*?)",',re.S).findall(s5)
e=0
for i in range(len(s55)):
    e=e+int(s55[i])
      
        
f=open('./谢吉-陕西-文科-招生数据.txt','r',encoding='utf-8')
s6=f.read()
import re
s66=re.compile('"plan":"(.*?)",',re.S).findall(s6)
f=0
for i in range(len(s66)):
    f=f+int(s66[i])

print('青海理科的人数是:{}\n甘肃文科的人数是:{}\n陕西理科的人数是:{}\n甘肃理科的人数是:{}\n青海文科的人数是:{}\n陕西文科的人数是:{}\n'.format(a,b,c,d,e,f))
g=a+b+c+d+e+f
print('西北地区总招生人数是:{}'.format(g))
        
        
        
        
        
        
        
        
        