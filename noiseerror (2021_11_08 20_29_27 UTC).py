# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:33:08 2020
Program to extract peak to peak amplitude of simple noise signal from text file to be use as uncertainty
@author: Liam O'Connor
"""


import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks
from numpy import *
import statistics
from statistics import mean, median
from scipy.signal import argrelextrema
import astropy.stats as astats

wavelength, reflectance = loadtxt('C:/python/spectral_cal/vnirA_texts/660nm/test.txt', unpack=True, skiprows = 2) #spectral, skiprows 44 for data from ASD RS3 program
#wavelength, reflectance = loadtxt('C:/python/Radiometric/vnira_texts/5000_5.txt', unpack=True, skiprows = 2) #radiometric, skiprows 44 for data from ASD RS3 program

print(wavelength.shape)
print(reflectance.shape)
print(reflectance.size)
print(reflectance.dtype)
peaks2, _ = find_peaks(reflectance, prominence=80)      # BEST!
plt.plot(wavelength[peaks2], reflectance[peaks2], "ob"); plt.plot(wavelength, reflectance); plt.legend([wavelength[peaks2], reflectance[peaks2]])
plt.xlabel("Wavelength (nm)"); plt.ylabel("Absolute Reflectance")
plt.show()

#print(argrelextrema(reflectance, np.greater))
print(mean(reflectance))
print(np.ptp(reflectance))
print(statistics.stdev(reflectance,33537.32))
print(astats.mad_std(reflectance))
