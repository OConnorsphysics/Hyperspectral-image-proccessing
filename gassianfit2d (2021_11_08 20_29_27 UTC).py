# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:50:31 2020

@author: Liam O'Connor
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting


x, y = loadtxt('C:/python/Radiometric/vnira_texts/4000_3.txt', unpack=True, skiprows = 2) #skiprows 44 for data from ASD RS3 program

# Generate fake data
#np.random.seed(0)
#x = np.linspace(-5., 5., 200)
#y = 3 * np.exp(-0.5 * (x - 1.3)**2 / 0.8**2)
#y += np.random.normal(0., 0.2, x.shape)

# Fit the data using a box model.
# Bounds are not really needed but included here to demonstrate usage.
t_init = models.Trapezoid1D(amplitude=35000., x_0=0., width=200., slope=0.5,
                            bounds={"x_0": (-5., 5.)})
fit_t = fitting.LevMarLSQFitter()
t = fit_t(t_init, x, y)

# Fit the data using a Gaussian
g_init = models.Gaussian1D(amplitude=38000., mean=700, stddev=100.)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, x, y)

# Plot the data with the best-fit model
plt.figure(figsize=(8,5))
plt.plot(x, y, 'ko')
#plt.plot(x, t(x), label='Trapezoid')
plt.plot(x, g(x), label='Gaussian')
plt.xlabel('Position')
plt.ylabel('Flux')
plt.legend(loc=2)