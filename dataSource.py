# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 09:13:49 2015

@author: Administrator
"""
import csv
import json
from collections import defaultdict
#import pandas as pd
#
#df = pd.read_csv('rating.csv')
#df = df.rename(columns = {'user_id':'user', 'group_id':'item'})
def VPrint(content):
    print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=1)
    
rating = defaultdict(dict)

#f = open('rating.csv', 'rb')
#for line in csv.reader(f):
#    rating[line[0]][line[1]] = float(line[2])
#f.close()

f = open('u.data', 'rb')
for line in f.readlines():
    temp = line.split('\t')
    rating[temp[0]][temp[1]] = float(temp[2])
f.close()

#for ids, uir in enumerate(rating.items()):
#    if ids < 3:
#        VPrint(uir)
