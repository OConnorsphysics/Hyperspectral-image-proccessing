# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:57:20 2020

@author: Liam O'Connor
"""

import numpy as np

#textfile = open("C:/python/spectral_cal/xydata_delete.txt")
#x,y = [], []
#for line in textfile:
#    row = line.split()
 #   x.append(row[0])
  #  y.append(row[1])
    
#print(x.size)
#print(y.shape)

from numpy import *
#DataIn = loadtxt('C:/python/spectral_cal/xydata_delete.txt')
wavelength, reflectance = loadtxt('C:/python/spectral_cal/15948(6327)stepfromhome00000.asd.txt', unpack=True)
print(wavelength.shape)

print(reflectance[5])