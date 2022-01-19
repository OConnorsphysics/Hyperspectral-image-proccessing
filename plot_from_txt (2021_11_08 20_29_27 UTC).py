# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:56:55 2020
plot from text file
@author: Liam O'Connor
"""
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import statistics

f =open(r"C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/radiometric/ASD/DN700nm.txt","r")   #open text file to write peak values to, r stops characters in filename from being special chars
i =    25            #loop control, 25 data points in txt file
dnValue = np.zeros([i, 4], dtype =np.double)         # array for x , y, error in y value, and relative intensity, for i number of points, (attenuator vs DN)
lines =  f.readlines()              #reads all lines of file
j=0
while (j < i):
    print(j)
    dnValue[j,0] = j*500
    dnline = 12*j +9               #dn values are on lines 13, 26, 39, etc for 13*j+12
    print(dnline)
    dnValue[j,1] = float(lines[dnline])# - float(lines[10])    #subtracts minimum dn value of dark measurement
    errorline = j*12 +11 
    dnValue[j,2] = lines[errorline]
    dnValue[j,3] = float(lines[dnline])/float(lines[297])       #relative DN = DNj/DNmax
    j = j+1
print(dnValue.shape)
print(dnValue[:,2])
meansig = int(statistics.mean(dnValue[:,2]) )    #averagees standard deviation in file and makes it an int, no decimal
plt.plot(dnValue[:,0], dnValue[:,1], color= 'b'); plt.text(0, 37000, r'$\bar\sigma=$'+ str(meansig));     #plot dn value, must manually enter sigma location on graph
plt.xlabel("Variable Attenuator Position (steps)"); plt.ylabel("ASD Response (DN)");plt.errorbar(dnValue[:,0], dnValue[:,1], yerr = dnValue[:,2], ecolor ='k', capsize = 3); 
blue_patch = mpatches.Patch(color='blue', label='700nm Band')
plt.legend(handles=[blue_patch])
plt.savefig("C:/Users/Liam O'Connor/Documents/uni/UG THESIS/plots/radiometric/ASD/DNresponse700nmwlinear")
plt.show()
plt.close()
plt.plot(dnValue[:,0], dnValue[:,3], color= 'r');
plt.show()