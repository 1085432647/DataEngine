# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:33:40 2021

@author: chentianyu
"""


import requests
import pandas as pd
from bs4 import BeautifulSoup

#要爬取网址
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-.shtml'

#模拟浏览器请求
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

#通过header模拟浏览器，通过request想服务器发起请求
html=requests.get(url,headers=headers,timeout = 10)

#text保存网页
content = html.text

#print(content)

soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

#查找网页模块中“tslb_b”类信息
temp = soup.find('div', class_='tslb_b')
#print(temp)

#创建DataFrame
Df_1 = pd.DataFrame(columns = ['编号','品牌','车系', '车型', '问题简述', '问题', '时间', '状态'])
    
#查找模块中所有行信息
list_1 = temp.find_all('tr')
#print(list_1)

for tr in list_1:
    temp = {}
#查找列信息
    list_2 = tr.find_all('td')
    #print(list_2)
    if len(list_2)>0:
        #提取标签下字符串
        temp['编号'], temp['品牌'], temp['车系'], temp['车型'], temp['问题简述'], temp['问题'], temp['时间'], temp['状态'] = list_2[0].text, list_2[1].text, list_2[2].text, list_2[3].text, list_2[4].text, list_2[5].text, list_2[6].text, list_2[7].text
        #append进DataFrame
        Df_1 = Df_1.append(temp,ignore_index=True)

#print(Df_1)

#保存
Df_1.to_excel('D:/test2.xlsx', index=False)