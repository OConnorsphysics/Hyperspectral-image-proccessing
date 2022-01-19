# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:38:34 2020
This program was written to open .txt files exported from RS cube program for a ASD spectroradiometer, and find the position and value of a spectral peak. 
The program then savesa plot of this.
change line 19 skip rows to skip number of lines for header text of the .txt file
@author: Liam O'Connor
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks

from astropy import modeling

from numpy import *
#wavelength, reflectance = loadtxt('C:/python/spectral_cal/vnirB_texts/820nm_15.txt', unpack=True, skiprows = 2) #spectral, skiprows 44 for data from ASD RS3 program
wavelength, reflectance = loadtxt('C:/python/Radiometric/vnira_texts/5000_5.txt', unpack=True, skiprows = 2) #radiometric, skiprows 44 for data from ASD RS3 program

print(wavelength.shape)

print(reflectance[5])
peaks, _ = find_peaks(reflectance, distance=50)
print(peaks.shape)
peaks2, _ = find_peaks(reflectance, prominence=80)      # BEST!
peaks3, _ = find_peaks(reflectance, width=20)
peaks4, _ = find_peaks(reflectance, threshold=0.4)     # Required vertical distance to its direct neighbouring samples, pretty useless
plt.plot(wavelength[peaks2], reflectance[peaks2], "ob"); plt.plot(wavelength, reflectance); plt.legend([wavelength[peaks2], reflectance[peaks2]])
plt.xlabel("Wavelength (nm)"); plt.ylabel("Absolute Reflectance")
#plt.savefig("C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/monochromator/asdlines/26164steps_1")
plt.show()
print(peaks2.shape)
print(peaks2)
print(reflectance[peaks2])

#fitter = modeling.fitting.LevMarLSQFitter()              #possible fitting sequence using astropy
#model = modeling.models.Gaussian1D()   # depending on the data you need to give some initial values
#fitted_model = fitter(model, wavelength, reflectance)
#plt.plot(wavelength, reflectance)
#plt.plot(wavelength, fitted_model(wavelength))