# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:12:48 2020

@author: Liam O'Connor
"""

t = linspace(0,2*pi,1000) ;
y = 100 * sin(2*pi*1.8*t) ;
s = sort(randperm(numel(t),19)) ; % 19 random points, sorted
plot(t,y,'b.-', t(s), y(s),'ro') ; % check
data = [t(s) ; y(s)].'
dlmwrite('export.txt',data)