# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 09:13:32 2015

@author: Administrator
"""

import pandas as pd
import numpy as np
from itertools import permutations

#读进数据
from dataSource import * 

def coocCreateIB(df):
    df = df.rename(columns = {df.columns[0]:'user', 
                              df.columns[1]:'item',
                              df.columns[2]:'val'})
    items = df['item'].unique()
    users = df['user'].unique()
    
    co_occurrence = pd.DataFrame(0, index=sorted(items), columns=sorted(items))  
    
    for u in users:
        rated = df[df['user'] == u]['item']
        
        for ra in rated:
            co_occurrence.loc[ra, ra] += \
                df.ix[(df['user']==u) & (df['item']==ra), 'val'].tolist()[0] ** 2
        
        if len(rated) > 1:
            for per in list(permutations(rated, 2)):
                co_occurrence.loc[per[0], per[1]] += \
                df.ix[(df['user']==u) & (df['item']==per[0]), 'val'].tolist()[0] * \
                df.ix[(df['user']==u) & (df['item']==per[1]), 'val'].tolist()[0]
    
    return co_occurrence

def raMatCreate(co_occurrence, u, df):
    res = [0 for _ in range(len(co_occurrence))]
    for i, ind in enumerate(co_occurrence.index):
        try:
            res[i] = df.ix[(df['user']==u) & (df['item']==ind), 'val'].tolist()[0]
        except:
            continue
    return np.array(res)


    
if __name__ == '__main__':
    co_occurrence = coocCreateIB(df)
    raMat = raMatCreate(co_occurrence, 1, df)
    print np.dot(co_occurrence, raMat)