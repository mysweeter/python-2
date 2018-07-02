# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=b75ea8bf00054988&rsv_t=dd9ayXxS7dBRFkeQivUcpx2d1SN3eyFM49rJXgYU7qeumVfQGLHsKRjuJJM&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&inputT=979&rsv_sug4=2969&rsv_sug=2'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)



#练习十一
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%B8%96%E7%95%8C%E6%9D%AF&oq=%25E9%25A3%259F%25E7%2589%25A9&rsv_pq=aefab37c00008234&rsv_t=cc8cXQDXbGqLD2SmPHOTPaGJMXTG7%2B%2ByfI4RbIRhLUd%2BPGGPpoSxkyHd5BU&rqlang=cn&rsv_enter=0&inputT=17298&rsv_sug3=13&rsv_sug1=26&rsv_sug7=101&bs=%E9%A3%9F%E7%89%A9'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)#爬取百度搜索标题
ls1=ls[5:10]
for i in range(len(ls1)):
    print("标题:{}".format(ls1[i]))
ls2=re.compile('class="c-abstract">(.*?)</div><div',re.S).findall(data)#爬取标题下的描述
for i in range(len(ls2)):
    print("描述:{}".format(ls2[i]))
ls3=re.compile('style="text-decoration:none;">(.*?)&nbsp').findall(data)#搜索的标题的网站
for i in range(len(ls3)):
    print("网址:{}".format(ls3[i]))
    
#练习十二
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
ls=re.compile('"dt_txt":(.*?),').findall(data)
ls1=re.compile('"temp":(.*?),').findall(data)
ls2=re.compile('"pressure":(.*?),').findall(data)
ls3=re.compile('"description":"(.*?)",').findall(data)
for i in range(36):
    print('时间:{},温度:{},气压:{},天气情况:{}'.format(ls[i],ls1[i],ls2[i],ls3[i]).replace('}','').replace(']',''))

