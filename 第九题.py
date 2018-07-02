# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:57:33 2018
12306.cn火车票余票查询
中国铁路火车票上的车次，有以C（读作“城”）打头的车次、
以D（读作“动车”）打头的车次、
以G（读作“高”）打头的车次、-------------------------------OK
以N（读作“内”）打头的车次、
以Z（读作“直”）打头的车次、
以T（读作“特”）打头的车次、
以K（读作“快”）打头的车次、
以L（读作“临”）打头的车次、
以Y（读作“游”）打头的车次和不带字母打头的车次等十余种。
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="v8hzesw92snv0p%2BXbBSYcvDvrkZJongII6gnHaa1K%2B5ZLSH2S1yiEmi5TocBRsVZ7KheRoWRj4s2%0AVRYp%2F1qQIXo6MxxZNB3giUuTVVn2qCjkK0zSOEIvJTiliIOKVW5rcQneIukZPdBmkyTOIosb%2FhFD%0AtpChpGqPNAY%2F29y3VTJO4Sh51LMePmFmF7Hv7THUyJDqN5VO5lYhnC611uP65vpluqQm243rAtJw%0AYiIa3SmEBr%2FXR331dZJkt7EmP3dw|预订|76000C630407|C6304|IXW|JFW|IVW|CNW|09:46|10:47|01:01|Y|NiY4S31uZETanTCgYyNeHA1zyfhqgCHmfzE%2B20yxLvYgcLOY|20180625|3|W1|02|06|1|0|||||||有||||无|无|||O0M0O0|OMO|0"
s=data[0]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')



#print('车次')
#print('ab')




s='N%2FySZswGXDqQPNR7KNqFwdBzvUwW%2Bl82FYFZ2hPdxUzg7dzpUdnAg2pq834pT2qxTxBpKYtUuHR0%0A%2FnW0SyuTkQBbT%2F4eQ77ZOW%2BtoKzu3wXAhd4uf4mUaXR1Yse3VS12QsN8ldXNn0NHYVwhbd7O2eW4%0AllD120G3NZiO%2FJsOiBpLp4zQ4QDtmRuAjMw9DdUyAs1m5xmrupP%2BsBCvBsljceSxMbjrmB2Pq2Gd%0ANnbvHm71zWRAdhG33ssxwkoMBNBU|预订|2400000G890B|G89|BXP|ICW|BXP|ICW|06:53|14:41|07:48|Y|I6f4%2F%2FVjmDh8FowzPFKFCfA38qy9Ynseatx1cYr0%2BTgDl0aA|20180626|3|P4|01|05|1|0|||||||||||有|19|1||O0M090|OM9|0'
ls2=s.split('|')

s='6nMecwwn%2FmtGuiPXKYxmT0FbbWWTvjF2UAaua033kdXVop408GE72Z0Fufh9%2BpIuEhIljbPBM5to%0AeTNk4ueWtfua5a3rTPfElUhDj2nUJsIc10AB%2B2Z6qteAs%2FcxgwcacnCL2RrIk3ECIB828Dc8NgOT%0Afl9aA60YO3fhi7afiBmwG6dGzDZNrBeuJsf19kj2%2FGIV9RwIle2l5ZSEE%2BnrJNZ6KPk3x9jmrzul%0Ana%2BW5R%2BKhCVf1klsJh0DiJcOC331|预订|240000G1010F|G101|VNP|AOH|VNP|NKH|06:43|11:14|04:31|Y|anKuw6ZIFPhViJi9kL%2Bo3KEA4Mj6oqybYA9LVMScFH3GP0MH|20180717|3|P2|01|08|1|0|||||||||||有|有|9||O0M090|OM9|0'
ls3=s.split('|')




#练习九
#BXP: "北京西", CQW: "重庆", CUW: "重庆北", CXW: "重庆西
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']
#Z96
p='  '
s="p8cj0ygMOpFMHP0OvsPTQuFYqs6lmTYt%2BIqU63p5OV9sYAbHfnkywmXHTJeU45iVJMjkkcsw7cQr%0AHIx19z6tUYYKDPE5Y7Dy5fq1JS0rOzMudpdIMzorPpodm4EnI3zbFCsZZDrYO9Wsxmv62zF3%2BDVp%0ACiMONUBS5qm0NBQDOla7KDNYJ%2BImoyvOrZjdK8RgGlnRg67V%2FZBoUN5AUv7Mn7wWu94iAP40vAjX%0AgvikIKWc7nGeUiBY6ZLO4ICAjIPJwxmyKFn4xhU%3D|预订|7700000Z9602|Z96|CUW|BXP|CUW|BXP|12:05|10:51|22:46|Y|WV%2FVMmQIrD7OrGqvQFkXQGXQSTlRY%2BvccwcKWXi%2Foiww1GLdriQrWLiuWKQ%3D|20180626|3|W2|01|14|0|0||||无|||有||无|有|||||10401030|1413|0"
s=data[4]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],'--','--','--','--','--','--','--','--',ls[29],ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')
#Z50
p='  '
s="gb2r4Njq%2FBhixyA0ZSzAhCtF9FFmUxWHGgdcw1KY4oZPBWUXZGuT01I4mAt8uu1KRQAo7jA8O0Dm%0AMCCvr2C5SziACJeEGZRfcD%2BZsdT9rs9MR23lRiX%2BBR0O%2BsrNWJ%2FbyxU%2BDaU5Ved5wXfVuiZF8ds0%0A3YIrcfZH7d3dAnWDrTg2YDSsGM7%2FmjVAGWbQC5P97MOkNfFWoeMl4AkJAzjvEGw5jC7C8q5%2B68GL%0ABUG0juRbDzTQ3V7vvf%2Fc%2BHgG%2FBtILHdBFc5r5JE%3D|预订|7600000Z5003|Z50|CDW|BXP|CUW|BXP|14:44|10:02|19:18|Y|RjH58DLRiV%2B0uUhwPZAziv6LrwCccy8Xj8OeTLrC8PbzRDLyHoXEFgi49jE%3D|20180626|3|W1|04|11|0|0||||无|||有||无|无|||||10401030|1413|0"
s=data[5]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],'--','--','--','--','--','--','--','--',ls[29],ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')
#Z4
p='  '
s="U5ZfilFzuPh605GAMPwWd3eelzSqtF7QPvNpDbLx1k9wqIGvoAXyN%2Bj%2Fh2Z7CDxuW0kRWyXd2g5b%0AYAiwEavY3YnCYVKADNVFJMG6v2tOUFADie7AWTNrhss0PltdVR7sDGjxRFU1FCzcsHhFj2VL5Tbv%0ABUGlRR0p0gk8kG52RWhVATQiUWuQJslY%2B7IW5G9Yz2XLoIlrz9fEIooJzQKCtm760GpEMpEx1a7u%0ALSjkjZL4w3zXsQPqQtPSRI%2FuBH1II%2B8O0GGY9qI%3D|预订|77000000Z400|Z4|CUW|BXP|CUW|BXP|15:08|10:10|19:02|Y|cHZP%2BdkabaAKwm07yf11nDLCsu6xdeCulMTuedUGiupM0VlQALBfbNbplKk%3D|20180626|3|W1|01|08|0|0||||无|||有||无|有|||||10401030|1413|0"
s=data[6]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],'--','--','--','--','--','--','--','--',ls[29],ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')