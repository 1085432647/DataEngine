# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:05:40 2021

@author: chentianyu
"""


import numpy as np
import pandas as pd

data = pd.read_csv('C:/Users/bailinglei/Desktop/Python/First Homework/car_complain.csv')

#print(data.head())

df_1 = pd.DataFrame(data)

#print(df_1.head())

df_1.loc[df_1.brand == '一汽-大众'] = '一汽大众'


car_result = df_1.groupby(['brand','car_model']).agg('count')

print(car_result['problem'].head())

brand_result = df_1.groupby('brand').agg('count')

print(brand_result['problem'].sort_values(ascending = False).head())


