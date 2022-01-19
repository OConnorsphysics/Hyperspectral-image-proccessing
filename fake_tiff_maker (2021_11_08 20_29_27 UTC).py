from PIL import Image
import numpy as np
import matplotlib
import os
framecount = 338       #number of frames to put in array
band = 450              #band number to select frame output
outputfile = "singleslice"          #enter name for output file
tiffarray = np.zeros((1024, 1344, framecount))            #convert raster tiff to arraybased on tiff dimensions
#print(tiffarray.size)

#for i in range(338):          #run through each file in directory, use path for data to be aquired

tiffarray[:, :, :] = 100000 

temparray = np.zeros((1024, framecount))            #array of zeros
#print(temparray.shape)
#print(temparray.size)
temparray = tiffarray[:,0,:]
print(tiffarray[:,0,:].shape)

matplotlib.image.imsave('rotated_frames/0test.tiff', tiffarray[:,band,:])      #saves to same directory as script, C:/python/

np.savetxt('rotated_frames/array.txt', [tiffarray[500,band,:]], delimiter=',', fmt='%d')
