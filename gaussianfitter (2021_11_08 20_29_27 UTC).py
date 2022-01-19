# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:53:22 2020
script to fit data set with gaussian
@author: Liam O'Connor
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from astropy import modeling
from numpy import *

wavelength, reflectance = loadtxt('C:/python/Radiometric/vnira_texts/4000_3.txt', unpack=True, skiprows = 2) #skiprows 44 for data from ASD RS3 program

data = reflectance
mean,std=norm.fit(data)

plt.hist(data, bins=30, normed=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)
plt.show()