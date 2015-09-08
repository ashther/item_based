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

rating = defaultdict(dict)

def VPrint(content):
    print json.dumps(content, encoding='utf-8', ensure_ascii=False, indent=1)

f = open('rating.csv', 'rb')
for line in csv.reader(f):
    rating[line[0]][line[1]] = float(line[2])
f.close()