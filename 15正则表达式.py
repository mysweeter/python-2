# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:56:47 2018
一种规则：re.... 匹配

正则表达式，又称规则表达式。
（英语：Regular Expression，在代码中常简写为regex、regexp或RE），
计算机科学的一个概念。正则表达式通常被用来检索、
替换那些符合某个模式(规则)的文本。

就像txt,word,网页...中的文本搜索
正则表达式字符分成两类：
1.字符
2.元字符
主要内容：
匹配字符
匹配次数
精准匹配
正则修正符
@author: Administrator
"""
import re#导入正则工具包
ls=re.compile('yu').findall("aliyuneduyu")#匹配普通字符
ls=re.compile('yun\n').findall('''aliyun
edu''')#匹配换行符
ls1=re.compile('\w\w\w\w\w').findall('123a_')#匹配字母 数字 下划线
#我 汉字找不到？
ls2=re.compile('\W').findall('123$&a_')#除匹配字母 数字 下划线

ls3=re.compile('\d').findall('a1b2c3')#匹配十进制数字

ls4=re.compile('\w\d[nedu]\w').findall('aliyu89787nedu')

ls5=re.compile('^li...').findall('''aliyunnnnji87362387aoyubaidu''')

ls6=re.compile('yun{1,2}').findall('aliyunnnnji87362387aoyubaidu')
#print('\'')
ls6=re.compile('id="(.*)"').findall('id="dialog_smoker_msg"')

ls7=re.compile('p.*?y').findall('poytphonyhjskjsa')#精准模式

ls8=re.compile('p.*y').findall('poytphonyhjskjsa')#贪婪模式

s="""我是阿里云大学
欢迎来学习
Python网络爬虫课程
"""

re.compile('阿里.*?python',re.S|re.I).findall(s)




























