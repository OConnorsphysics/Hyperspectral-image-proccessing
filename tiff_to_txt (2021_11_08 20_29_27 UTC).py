# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:03:03 2020
tiff to txt
converts one tiff to txt file
@author: Liam O'Connor
"""

from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import os
Tiff = Image.open("C:\\python\\spectral_cal\\VNIR-B_Spectral\\700nm\\5.tiff")       #open tiff file, image.open uses pil library
whitearray = np.array(Tiff)             #convert raster tiff to array
print(whitearray.shape)
print(whitearray.size)
intensity = np.zeros((1024, 2), dtype =np.float64)   #2d array for corresponding wavelengths to intensity values of VNIR cameras
i=0
for i in range(1024):   
    intensity[i,1] = float(whitearray[i,672])
    intensity[i,0] = (3.071*10**(-5))*float(i*i) + (0.59717*float(i)) + 377.344           #equation for vnir B
    #intensity[i,0] = (2.9264*10**(-5))*i*i + (0.59922*i) + 377.536       #equation for vnirA camera wavelength to pixel conversion
#np.savetxt('spectral_cal\\vnirA_texts\\700nm_3.txt', [whitearray[:,600]], delimiter='\n', header= 'array from tiff 700nm_3[:,600]', fmt='%d')
np.savetxt('spectral_cal\\vnirb_texts\\700nm_corrected_5.txt', np.c_[intensity[:,0], intensity[:,1]], delimiter=' ', header= 'array from tiff 700nm_5[:,672], wavelength (nm) vs intensity', fmt='%f')
plt.plot(intensity[:,0], intensity[:,1])
plt.show()
j = Image.fromarray(whitearray)
#j.save("spectral_cal\\vnirA_texts\\800nm_25.png")