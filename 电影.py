# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 16:21:47 2018

@author: Administrator
"""

m=[]
import urllib.request as r    
for i in range(1,101):
    url='http://dianying.2345.com/list/-------{}.html'.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    p=r.urlopen(req).read().decode('gbk','ignore')
    print('第{}页获取结束'.format(i))
    m.append(p)
####################
import re

n=[]
for i in range(len(m)):
    ls=re.compile('<div data-id="(.*?)"').findall(m[i])
    n.append(ls)
    

a=[]
for i in range(len(n)):
    for j in range(20):
        b=n[i][j]
        a.append(b)

s=[]
for k in range(len(a)):
    url='http://xiaohua.zol.com.cn/detail60/{}.html'.format(a[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    print('成功{}'.format(k))
    s.append(data)


f=open('./dianying1.txt','w')
import re
for y in range(len(s)):
    name=re.compile('<h1>(.*?)</h1>',re.S).findall(s[y])
    pinfen=re.compile('<em class="emScore">(.*?)</em>',re.S).findall(s[y])
    jianjie=re.compile('<span class="sAll">(.*?)</span>',re.S).findall(s[y])
    diqu=re.compile('<a title="(.*?)" data-ajax83="ys_dy_2015_detail_diq').findall(s[y])
    zhuyan=re.compile('<a data-ajax83="ys_dy_2015_detail_zhy_." title="(.*?)" href',re.S).findall(s[y])
    shichang=re.compile('<em class="emTit">时长：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    niandai=re.compile('<em class="emTit">年代：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    print('{}数据已录取'.format(y))
    f.write('电影名：{},豆瓣评分:{},地区:{},年代:{},时长:{},主演:{},电影简介:{}\n'.format(name,pinfen,diqu,niandai,shichang,zhuyan,jianjie))
f.close()













c=[]
import urllib.request as r
url='file:./dianying1.txt'
data=r.urlopen(url).read().decode('gbk')

ls1=data.split(' ')


import json
for i in range(3500):
    a=json.loads(data[i])
    c.append(a)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
m=[]
import urllib.request as r
url='file:./dianying.txt'
data=r.urlopen(url).read().decode('gbk')
data1=data.split('\n')

ls1=[]
ls2=[]
ls3=[]
for i in range(len(data1)):#电影名,时长，简介.
    if i%3==0:
        ls1.append(data1[i])
    if i%3==1:
        ls2.append(data1[i])
    if i%3==2:
        ls3.append(data1[i])

import re
dy=re.compile("电影名：..(.*?)..,").findall(data)
dy1=str(dy)

out=re.sub('(.*?)', '',dy1)


#for a in range(len(ls1)):
#    s=input('请输入电影名称')
#    if s==dy[a]:
#        print(ls1[a],ls2[a],ls3[a]) 
#input('')



#s=input('请输入电影名称')
#for a in range(len(ls1)):
#    if s==dy[a]:
#        print('{}'.format(ls1[a]))
#        print('{}'.format(ls2[a]))
#        print('{}'.format(ls3[a]))
#input('')












#for a in range(len(ls1)):
#    s=input('请输入电影名称')
#    if s==dy[a]:
#        print('{}'.format(ls1[a]))
#        print('{}'.format(ls2[a]))
#        print('{}'.format(ls3[a]))
#        continue
#    else:
#        print('无此电影资源,请重新输入电影名')
#    break
#input('输入任意退出')











#b=input('请输入电影名称：')
#for i in dy:
#    if i.startswith(b):
#        print('{}'.format(ls1[a]))
#        print('{}'.format(ls2[a]))
#        print('{}'.format(ls3[a]))
#    elif i.endswith(b):
#        print('{}'.format(ls1[a]))
#        print('{}'.format(ls2[a]))
#        print('{}'.format(ls3[a]))
#    elif i.index(b):
#        print('{}'.format(ls1[a]))
#        print('{}'.format(ls2[a]))
#        print('{}'.format(ls3[a]))
#        
#b=input('请输入电影名称：')        
#for i in dy:
#    try:
#        i.index(b)
#        print(i)
#    except Exception as r:
#        pass

#b=input('请输入电影名称：')
#for i in dy:
#    if i.startswith(b):
#        print(i)
#    elif i.endswith(b):
#        print(i)
#    elif i.index(b):
#        print(i)
        
#ls=['abc','4sbc2','1abc13']
#x='bc'
#for i in ls:
#    if i.index(x):
#        print(i)

b=input('请输入电影名称：')        
for i in range(len(dy)):
    a=dy[i]
    try:
        a.index(b)
        print('{}\n{}\n{}\n'.format(ls1[i],ls2[i],ls3[i]))
    except Exception as r:
        pass
