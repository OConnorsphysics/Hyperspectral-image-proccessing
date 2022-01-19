# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:29:02 2020
converts tiff to text files for radiometric calibrations, does multiple files in a loop.
Has two seperate equations to convert pixel location to wavelength
path names can be changed by changing attenuator variable, originally meant for step location of integrating sphere attenuator
@author: Liam O'Connor
"""


from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import os
import re

attenuator = str(12000)               #attenuator setting in steps, used to name files

def sorted_alphanumeric(data):                          #sorts directory by 0, 1,2,3 not 0,1,10,2
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir('C:/python/Radiometric/VNIR-B/'+str(attenuator)))
print(dirlist)
filenumber = 0           #interger for filename/ nummber of text files to be saved, as file variable is 0.tiff for example
for file in dirlist:          #run through each file in directory, use path for data to be aquired
    print(file)

    Tiff = Image.open(os.path.join("C:/python/Radiometric/VNIR-B/"+str(attenuator),file))       #open tiff file, image.open uses pil library
    whitearray = np.array(Tiff)             #convert raster tiff to array
    print(whitearray.shape)
    print(whitearray.size)
    intensity = np.zeros((1024, 2), dtype =np.float64)   #2d array for corresponding wavelengths to intensity values of VNIR cameras
    i=0
    for i in range(1024):   #range should be 1024, number of pixels
        intensity[i,1] = float(whitearray[i,672])
        intensity[i,0] = (3.071*10**(-5))*float(i)*float(i) + (0.59717*float(i)) + 377.344       #equation for vnirB camera wavelength to pixel conversion
        #intensity[i,0] = (2.9264*10.0**(-5))*float(i)*float(i) + (0.59922*float(i)) + 377.536       #equation for vnirA camera wavelength to pixel conversion
    np.savetxt("C:/python/Radiometric/vnirb_texts/"+str(attenuator)+"/"+str(filenumber)+".txt", np.c_[intensity[:,0], intensity[:,1]], delimiter=' ', header= 'array from tiff [:,672], wavelength (nm) vs intensity, wavelength equation =(2.9264*10**(-5))*i*i + (0.59922*i) + 377.536 ', fmt='%f')
    plt.plot(intensity[:,0], intensity[:,1]);
    plt.xlabel("Wavelength (nm)"); plt.ylabel("Camera Response (DN)")
    plt.show()
    j = Image.fromarray(whitearray)             #image created from tiff array, same visual as the og tiff
    #j.save(os.path.join("C:/python/spectral_cal/vnirB_texts/640nm/",file))     #saves tiff of whitearray
    filenumber = filenumber + 1
    print(file)
    if file == "9.tiff":       #only 6 tiff files to do, avoid proccessing dark and white tiffs
        break
    