# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 09:13:49 2015

@author: Administrator
"""

import pandas as pd
import numpy as np

df = pd.read_csv('rating.csv')
df = df.rename(columns = {'user_id':'user', 'group_id':'item'})