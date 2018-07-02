# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

m=[]
import urllib.request as r    
for i in range(1,200):
    url='http://xiaohua.zol.com.cn/youmo/{}.html'.format(i)
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
    url='http://xiaohua.zol.com.cn/detail12/{}.html'.format(a[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    print('成功{}'.format(k))
    s.append(data)




f=open('./youmo.txt','w',encoding='gbk')
import re
for y in range(len(m)):
    zuozhe=re.compile('<h1 class="article-title">(.*?)</h1>',re.S).findall(s[y])
    laiyuan=re.compile('</span><span>(.*?)/span>',re.S).findall(s[y])
    neirong=re.compile('<div class="article-text">(.*?)</div>',re.S).findall(s[y])
    print('{}数据已录取'.format(y))
    f.write('作者:{},来源:{},内容:{}\n'.format(zuozhe,laiyuan,neirong).replace('p','').replace('<','').replace('>','').replace('/',''))
f.close()