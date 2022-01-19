# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:24:11 2020
tiff cubemaker with tifffile library 
@author: Liam O'Connor
"""

from PIL import Image
import numpy as np
import matplotlib
import os
import re
framecount = 418      #number of frames to put in array
band = 500              #band number to select frame output
outputfile = "singleslice"          #enter name for output file
tiffarray = np.zeros((1024, 1344, framecount), dtype =np.uint16)            #convert raster tiff to arraybased on tiff dimensions
#print(tiffarray.size)
i = 0

def sorted_alphanumeric(data):                          #sorts directory by 0, 1,2,3 not 0,1,10,2
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir('C:/python/data/B_200mm_1000ms_19apt/'))
print(dirlist)

for file in dirlist:          #run through each file in directory, use path for data to be aquired
  #  image_stack = tifffile.imread(os.path.join("C:/python/data/",file)         #image_stack lines are to use tifffile library

   tiff = Image.open(os.path.join("C:/python/data/B_200mm_1000ms_19apt",file))       #open tiff file, image.open uses pil library
   print(file)
   singlearray = np.array(tiff)            #convert raster tiff to array
   print(singlearray.shape)
   tiffarray[:, :, i] = singlearray   #fill the ith frame of 3d tiffarray cube with a single i frame
   i=i+1
#print(image_stack.size)
#print(image_stack.shape)

temparray = np.zeros((1024, framecount), dtype = np.uint16)            #array of zeros
#print(temparray.shape)
#print(temparray.size)
temparray = tiffarray[:,0,:]
print(tiffarray[:,0,:].shape)

#matplotlib.image.imsave('rotated_frames/spectralonongrid_all_432_all.tiff', tiffarray[:,band,:], dpi=1)      #saves to same directory as script, C:/python/
matplotlib.image.imsave('rotated_frames/B_200mm_1000ms_19apt_500_all_all.tiff', tiffarray[500,:,:], dpi=1 ) 
#matplotlib.image.imsave('rotated_frames/spectralonongrid_all_all_2.tiff', tiffarray[:,:,2], dpi=1) 
#np.savetxt('rotated_frames/focus_spectral.txt', [tiffarray[:,600,25]], delimiter='\n', header= 'tiffarray spectral data from (:,600,25)', fmt='%d')
