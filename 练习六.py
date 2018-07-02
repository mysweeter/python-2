# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title']


#练习六
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180621&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

for i in range(36):
                raw_title=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
                view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
                view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
                nick=data['mods']['itemlist']['data']['auctions'][i]['nick']
                item_loc=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
                print('商品名:{},价格:{},付款:{},店铺名:{},地址:{},'.format(raw_title,view_price,view_sales,nick,item_loc))


ls=[]
for i in range(36):
    view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    a=float(view_price)
    ls.append(a)
    
sorted(ls)
ls1=sorted(ls,reverse=True) 
print(ls1)

import re
ls=[]
for i in range(36):
    view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    b=re.sub('\D','',view_sales)
    c=float(b)
    ls.append(c)
 
sorted(ls)
ls1=sorted(ls,reverse=True) 
print(ls1)

for i in range(36):
    raw_title=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    nick=data['mods']['itemlist']['data']['auctions'][i]['nick']
    item_loc=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    view_fee=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if (view_fee=='0.00'):
        try:
            icon_content=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]['icon_content']
        except Exception as err:
            if (icon_content=='15天退货'):
                print('商品名:{},价格:{},付款:{},店铺名:{},地址:{},包邮,支持{}'.format(raw_title,view_price,view_sales,nick,item_loc,icon_content))


for i in range(36):
    raw_title=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    view_sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    nick=data['mods']['itemlist']['data']['auctions'][i]['nick']
    item_loc=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    view_fee=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if (view_fee=='0.00'):
        try:
            icon_content=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]['icon_content']
            if (icon_content=='15天退货'):
                print('商品名:{},价格:{},付款:{},店铺名:{},地址:{},包邮,支持{}'.format(raw_title,view_price,view_sales,nick,item_loc,icon_content))
        except Exception as err:
            continue