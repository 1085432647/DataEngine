# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:51:24 2021

@author: chentianyu
"""


import pandas as pd

data = {'Chinese':[68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90]}

df = pd.DataFrame(data,index = ['zhangfei','guanyu','liubei','dianwei','xuchu'],columns = ['Chinese','Math','English'])

#print(df)

print(df.sum())

print(df.max())

print(df.min())

print(df.mean())

print(df.std())