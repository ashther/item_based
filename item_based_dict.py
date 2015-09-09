# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 10:07:00 2015

@author: Administrator
"""
import pandas as pd
import numpy as np
import json
from itertools import permutations
from dataSource import *

def VPrint(content):
    print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=1)

def coocCreate(rating):
    #users = sorted(rating.keys())
    items = sorted(list(set([y for x in rating.values() for y in x.keys()])))
    
    co_occurrence = pd.DataFrame(0, index=items, columns=items)
    
    for u, ir in rating.items():
        for i in ir.keys():
            co_occurrence.loc[i, i] += ir[i] * ir[i]
        if len(ir.keys()) > 1:
            for per in list(permutations(ir.keys(), 2)):
                co_occurrence.loc[per[0], per[1]] += ir[per[0]] * ir[per[1]]
    return co_occurrence

def raMatCreate(co_occurrence, u, rating):
    res = np.zeros(len(co_occurrence))
    for i, ind in enumerate(co_occurrence.index):
        if ind in rating[str(u)].keys():
            res[i] = rating[str(u)][ind]
    return res
    
def recommend(u, rating):    
    co_occurrence = coocCreate(rating)
    rating_now = raMatCreate(co_occurrence, u, rating)
    rating_predict = np.dot(co_occurrence, rating_now)
    recommend = dict(zip(co_occurrence.index, rating_predict))
    
    return sorted([(k, v) for k, v in recommend.items() \
                    if k not in rating[str(u)].keys()], 
                   key=lambda recmd:recmd[1], reverse=True)
