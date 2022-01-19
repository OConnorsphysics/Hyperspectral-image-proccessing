# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:32:57 2020

@author: Liam O'Connor
"""
import os

import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir('C:/python/data/1secintg_100mm/'))
print(dirlist)