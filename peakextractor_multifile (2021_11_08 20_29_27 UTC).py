
"""
Created on Wed Apr  8 22:38:34 2020
This program was written to open .txt files exported from RS cube program for a ASD spectroradiometer, and find the position and value of a spectral peak. 
The program then savesa plot of this.
change line 19 skip rows to skip number of lines for header text of the .txt file
This is a version intended to do all files in one folder
@author: Liam O'Connor
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks
import os
from astropy import modeling
from numpy import *
import statistics

bandfile = "640nm"            #name of folder to find .tiff files ex. "640nm"
f =open(r"C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/spectral/vnirb/peaks"+str(bandfile)+".txt","w+")   #open text file to write peak values to, r stops characters in filename from being special chars
#f =open(r"C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/monochromator/"+str(bandfile)+".txt","w+")   #open text file to write peak values to, r stops characters in filename from being special chars

f.write("Wavelength peaks of all tiff files for labelled wavelength\r\n")            #header of text file
allpeaks = np.zeros(52)         #array to store a peak for each tiff file, 26 for vnira data, 52 for vnir b data

def sorted_alphanumeric(data):                          #sorts directory by 0, 1,2,3 not 0,1,10,2
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir('C:/python/spectral_cal/vnirB_texts/'+str(bandfile)))  #create list of all items in folder
#dirlist = sorted_alphanumeric(os.listdir('C:/python/spectral_cal/monochromator/'+str(bandfile)))  #create list of all items in folder

print(dirlist)
filenumber = 0           #interger for filename/ nummber of text files to be saved, as file variable is 0.tiff for example
for file in dirlist:          #run through each file in directory, use path for data to be aquired
  #  image_stack = tifffile.imread(os.path.join("C:/python/data/",file)         #image_stack lines are to use tifffile library
    print(file)
    wavelength, reflectance = loadtxt(os.path.join("C:/python/spectral_cal/vnirB_texts/"+str(bandfile),file), unpack=True, skiprows = 1) #skiprows 1 for data from vnir text files (skips header)
    #wavelength, reflectance = loadtxt(os.path.join("C:/python/spectral_cal/monochromator/"+str(bandfile),file), unpack=True, skiprows = 44) #skiprows 44 for data from ASD RS3 program (skips header)
    print(wavelength.shape)
    #print(peaks.shape)
    peaks2, _ = find_peaks(reflectance, prominence=50,distance=10)      #find peak in discrete array data based on distances to neigbouring points
    plt.plot(wavelength[peaks2], reflectance[peaks2], "ob"); plt.plot(wavelength, reflectance); plt.legend([wavelength[peaks2], reflectance[peaks2]])
    plt.xlabel("Wavelength (nm)"); plt.ylabel("Camera Response (DN)")
    plt.savefig("C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/spectral/vnirb/"+str(bandfile)+"/"+str(filenumber))       #save plot of wavelength vs DN with peak  marked
    #plt.savefig("C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/monochromator/"+str(bandfile)+str(filenumber))       #save plot of wavelength vs DN with peak  marked
    plt.show()
    plt.close()
    print(peaks2.shape)
    print(peaks2)
    print(reflectance[peaks2])
    f.write(str(wavelength[peaks2]))
    f.write("\n")
    allpeaks[filenumber] = wavelength[peaks2]           #fill array with peak value for each tiff file, wont work if multiple peaks detected, comment out if multi peak or no peak
    filenumber= filenumber +1
    
    
f.write("average equals \n")
average = statistics.mean(allpeaks)
f.write(str(average))
f.write("\n")
f.write("standard deviation of peaks is \n")
sdevi= statistics.stdev(allpeaks)       #calculate standard deviation of data set in all peaks list
f.write(str(sdevi))
f.close()