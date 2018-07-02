import urllib.request as r
jianchajiancha=[]
import re
print('欢迎界面（闪屏）')
myconn=r.urlopen('http://www.xiao688.com/')
if myconn.getcode()==200:
    data=myconn.read().decode('utf-8')
else:
    print('无法访问网站!')
z=re.compile('(<li><a href="/cms/list/typeid-2.html">经典笑话</a></li>.*?">个性签名</a></li>)',re.S).findall(data)
fenlei=re.compile('html">(.*?)</a></li>').findall(z[0])
fenleiwangzhi=re.compile('<li><a href="(.*?)">').findall(z[0])
x=0
while (x<1):
    fanhui=0
    a=input('搜索关键词请输入“A”、查看笑话分类请输入“B”  ：')
    if a=='B':
        b=0
        while (b<1):
            for i in range(len(fenlei)):
                print('编号{}：{}'.format(i+1,fenlei[i]))
            print('\n请在下面输入对应编号-数字-选择笑话分类输入9999返回上一级菜单)QAQ\n')
            x1=input('请输入：')
            try:
                x1=int(x1)
            except Exception as err:
                input('请正确输入，回车键继续')
                continue
            a12684=0
            if x1==9999:
                print('正在返回主菜单……')
                break
            for i2 in range(len(fenlei)):
                a12684=a12684+1
                print('---------------{}'.format(a12684))
                if str(x1)==str(i2+1):
                    xiaohuayulan=[]
                    myconn=r.urlopen('http://www.xiao688.com/{}'.format(fenleiwangzhi[i2]))
                    if myconn.getcode()==200:
                        print('正在获取{},请稍候……'.format(fenlei[i2]))
                        data2=myconn.read().decode('utf-8')
                    else:
                        input('无法访问网站!\n请按回车键返回上一级菜单')
                        break
                    xiaohuaming=re.compile('title="(.*?)" target="_blank">').findall(data2)
                    xiaohuayulan1=re.compile('<div class="content">(.*?)</div>\r\n\t\t\t\t\t\t<div class="func cfix">',re.S).findall(data2)
                    xiaohuayulan=[]
                    for i in range(len(xiaohuayulan1)):
                        buquanxiaohuazazhi=re.compile('(<p class="m_content">...<a href=".*?" target="_blank">点击浏览全部内容</a>)',re.S).findall(xiaohuayulan1[i])
                        jianchajiancha.append(buquanxiaohuazazhi)
                        if len(buquanxiaohuazazhi)==1:
                            for i3 in range(len(buquanxiaohuazazhi)):
                                x2=buquanxiaohuazazhi[i3]
                                quchuzazhi=xiaohuayulan1[i].replace(x2,'').replace('<br />','\n').replace('</p>','').replace('<p>','').replace('<span>','').replace('</span>','').replace('&nbsp;',' ').replace('<p style="text-align:left;">',' ')
                                xiaohuayulan.append(quchuzazhi)
                        if len(buquanxiaohuazazhi)==0:
                            quchuzazhi=xiaohuayulan1[i].replace('<br />','\n').replace('</p>','').replace('<p>','').replace('<span>','').replace('</span>','').replace('&nbsp;',' ').replace('<p style="text-align:left;">',' ')
                            xiaohuayulan.append(quchuzazhi)
                    for i in range(len(xiaohuayulan)):
                        if len(jianchajiancha[i])==0:
                            print('{}\n\n{}\n'.format(xiaohuaming[i],xiaohuayulan[i]))
                            a1=0
                            while (a1==0):
                                shuru=input('---------------------------------\n请输入数字2查看下一条笑话，输入r返回上一级菜单,输入f返回主菜单')
                                if shuru=='2':
                                    xuanze=1
                                    break
                                elif shuru=='r':
                                    xuanze=2
                                    fanhui=1
                                    break
                                elif shuru=='f':
                                    xuanze=3
                                    fanhui=2
                                else:
                                    xuanze=4
                                    input('请正确输入，回车键继续！')
                                    continue
                            if xuanze==2:
                                break
                            if xuanze==3:
                                break
                        else:
                            buchongwangzhi=re.compile('href="/(.*?)" target="_blank">点击浏览全部内容</a>',re.S).findall(jianchajiancha[i][0])
                            buchongwangzhi=buchongwangzhi[0]
                            myconn=r.urlopen('http://www.xiao688.com/{}'.format(buchongwangzhi))
                            if myconn.getcode()==200:
                                data3=myconn.read().decode('utf-8')
                            else:
                                input('无法访问网站!请按回车键返回上一级菜单')
                                fanhui=1
                                break
                            xiaohuaquanbu=re.compile('<div class="content"(.*?)</div>\r\n\t\t\t<div class=',re.S).findall(data3)
                            xiaohuaquanbu=re.compile('class="ads_jc_r"></div>(.*$)',re.S).findall(xiaohuaquanbu[0])
                            xiaohuaquanbu=xiaohuaquanbu[0].replace('<br />','\n').replace('</p>','').replace('<p>','').replace('<span>','').replace('</span>','').replace('&nbsp;',' ').replace('<p style="text-align:left;">',' ').repalce('&quot','')
                            print('{}\n\n{}\n'.format(xiaohuaming[i],xiaohuaquanbu))
                            a1=0
                            while (a1==0):
                                shuru=input('---------------------------------\n请输入数字2查看下一条笑话，输入r返回上一级菜单,输入f返回主菜单')
                                if shuru=='2':
                                    break
                                elif shuru=='r':
                                    fanhui=1
                                    break
                                elif shuru=='f':
                                    fanhui=2
                                else:
                                    input('请正确输入，回车键继续！')
                                    continue
                    if fanhui==1:
                        break
                    if fanhui==2:
                        break
            if fanhui==1:
                continue
            elif fanhui==2:
                break
            x=x+1
            break
        if x==1:
            break
###########################下面是搜索功能区域
#r.quote('我')#url网址可以识别的汉字
    elif a=='A':
        b=0
        fanhui=0
        while (b<1):
            shuru=input('搜索功能还在努力开发当中QAQ，待开发完成后会通知大家\n输入f返回主菜单,输入q退出应用')
            if shuru=='f':
                xuanze=1
                break
            if shuru=='q':
                xuanze=1111
                break
            else:
                input('请正确输入，回车键继续！')
                continue
            x=x+1
            break
        if xuanze==1:
            continue
        if xuanze==1111:
            x=x+1
            break
    else:
        input('请正确输入，回车键继续！')
        
        
#a=input('sss:')
#print(type(a))
#a='2'
#print(type(a))
        
        
        
        
        
        
 

m=[]
import urllib.request as r    
for i in range(1,120):
    url='http://xiaohua.zol.com.cn/xiaoyuan/{}.html'.format(i)
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




f=open('./xiaoyuan.txt','w',encoding='gbk')
import re
for y in range(len(m)):
    zuozhe=re.compile('<h1 class="article-title">(.*?)</h1>',re.S).findall(s[y])
    laiyuan=re.compile('</span><span>(.*?)/span>',re.S).findall(s[y])
    neirong=re.compile('<div class="article-text">(.*?)</div>',re.S).findall(s[y])
    print('{}数据已录取'.format(y))
    f.write('作者:{},来源:{},内容:{}\n'.format(zuozhe,laiyuan,neirong).replace('p','').replace('<','').replace('>','').replace('/',''))
f.close()








f=open('./lengxiaohua8.txt','w',encoding='utf-8')

        
        
        
        
        
        
        
        
        # 打开旧文件
f=open('lengxiaohua9.txt','r',encoding='gbk')

# 打开新文件
f1=open('7.txt','w',encoding='gbk')


# 循环读取旧文件
for line in f:
    # 进行判断
    if "n" in line:
        line=line.replace('n','')
        line=line.replace('r','')
        line=line.replace('t','')
    # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
    f1.write(line)
f.close()
f1.close()
        
        
        
        
        
        
        
        
        
        
        
                # 打开旧文件
f=open('7.txt','r',encoding='gbk')

# 打开新文件
f1=open('8.txt','w',encoding='gbk')


# 循环读取旧文件
for line in f:
    # 进行判断
    if "\\" in line:
        line=line.replace('\\','')
    # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
    f1.write(line)
f.close()
f1.close()
        
        
        
m=[]
import urllib.request as r
url='file:./8.txt'
data=r.urlopen(url).read().decode('gbk')
data1=data.split('\n')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        