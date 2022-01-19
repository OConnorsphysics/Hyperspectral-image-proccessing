# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:11:49 2020
Program opens text file of wavelength vs dn/reflectance, saves a plot of it, extracts dn value for single band, saves to new text file. 
This will iterate through each file in folder, creating an average and standard deviation for the dn value at specified band.
by changing attenuator value you can change folder, run again, and append to the existing txt file
@author: Liam O'Connor
"""


import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks
import os
from astropy import modeling
from numpy import *
import statistics
import re

f =open(r"C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/radiometric/ASD/DN700nm.txt","a")   #open text file to write peak values to, r stops characters in filename from being special chars
f.write("Wavelength peaks of all tiff files for labelled wavelength\r\n")            #header of text file
allpeaks = np.zeros(5)         #array to store a peak for each tiff file, number of files in folder

attenuator = str(12000)               #attenuator setting in steps used to name files
print(attenuator)
f.write("attenuator setting of  ")
f.write(attenuator)
f.write("****************************\n")
def sorted_alphanumeric(data):                          #sorts directory by 0, 1,2,3 not 0,1,10,2
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir('C:/python/Radiometric/ASD/ASCII/'+str(attenuator)))
print(dirlist)
filenumber = 0           #interger for filename/ nummber of text files to be saved, as file variable is 0.tiff for example
for file in dirlist:          #run through each file in directory, use path for data to be aquired
  #  image_stack = tifffile.imread(os.path.join("C:/python/data/",file)         #image_stack lines are to use tifffile library
    print(file)
    wavelength, reflectance = loadtxt(os.path.join("C:/python/Radiometric/ASD/ASCII/"+str(attenuator),file), unpack=True, skiprows = 44) #skiprows 44 for data from ASD RS3 program (skips header)
    print(wavelength.shape)
    print("wavelength[526] has value")
    print(wavelength[349])
    print("corresponds to dn value of")
    print(reflectance[349])
    #plt.plot(wavelength[peaks2], reflectance[peaks2], "ob")
    plt.plot(wavelength, reflectance); 
    plt.xlabel("Wavelength (nm)"); plt.ylabel("Camera Response (DN)")
    plt.savefig("C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/radiometric/ASD/"+str(attenuator)+str(filenumber))    #add +"/" before +str(filenumber) to put in separate folder
    plt.show()
    f.write(str(reflectance[349]))      #write dn value of wavelength[526] =700nm to text file vnir, [349]=700nm asd
    f.write("\n")
    allpeaks[filenumber]= reflectance[349]
    filenumber= filenumber +1
    
    
#f.write(allpeaks)       #write array of peaks to .txt file
f.write("average equals \n")
average = statistics.mean(allpeaks)
f.write(str(average))
f.write("\n")
f.write("standard deviation of peaks is \n")
sdevi= statistics.stdev(allpeaks)       #calculate standard deviation of data set in all peaks list
f.write(str(sdevi))
f.write("\n")
f.close()
#fitter = modeling.fitting.LevMarLSQFitter()              #possible fitting sequence using astropy
#model = modeling.models.Gaussian1D()   # depending on the data you need to give some initial values
#fitted_model = fitter(model, wavelength, reflectance)
#plt.plot(wavelength, reflectance)
#plt.plot(wavelength, fitted_model(wavelength))