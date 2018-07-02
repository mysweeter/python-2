# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')




#练习十四
import urllib.request as r
data=r.urlopen('file:./all_school.txt').read().decode('utf-8')
import re
ls=re.compile('daxue-jianjie-(.*?).html').findall(data)
ls1=re.compile('(.*?)\t.*\t').findall(data)
for i in range(2300):
    print('学校:{},编号:{}'.format(ls1[i],ls[i]))


import urllib.request as r
url='http://www.gaokaopai.com/daxue-zhaosheng-477.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import re
a=re.compile('<li data-val="(.*?)" data-id="2"').findall(d)
b=re.compile(".setVar\S.claimCity',(.*?)\S\S>").findall(d)
for i in range(31):
    print('{}:{}'.format(a[i],b[i]))


import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in ls:
    data='id={}&type=2&city=63&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    ls2=re.compile('"plan":\S(.*?)\S,').findall(d)
    #print(ls2)
f=open('./a.txt','w')
f.write(d+"\n")
f.close()





f=open('./青海理科2.txt','w')
import urllib.request as r
url='file:./all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
c=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
b=re.compile('(.*?)http:/').findall(data)
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
for i in range(len(c)):
   data='id={}&type=2&city=63&state=1'.format(c[i])
   data1=data.encode()
   req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
   d=r.urlopen(req).read().decode('utf-8','ignore')
   print('输出次数{}'.format(i))
   f.write(d+"\n")
f.close()





f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
s2=re.compile('.*?\t').findall(s)
for i in range(len(s1)):
    print('学校：{}学校代码：{}'.format(s2[i*2],s1[i]))
f.close()
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=63&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=i
    print('输出{}次'.format(a))
#查错并纠正
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=63&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        continue
#生成最终的txt文件
f=open('./青海理科.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()



#最终版
f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=63&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=63&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))
        continue

f=open('./青海理科4.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()  







