# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:46:24 2019

@author: Frnn
"""

#%% Nomor 4
from matplotlib import pyplot as plt

print(1174072%3+2)

def plot_cs():
  
        x = [11,12,13,14,15]
        y = [12,13,16,15,17] 
        
        x1 = [10,20,30,40,50,60,70]
        y1 = [11,9,20,21,22,25,23]
        
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [23,20,53,25,25,35,14,15,15,17]
        plt.subplot(221)
        plt.plot(x,y)
        plt.subplot(222)
        plt.plot(x1,y1)
        plt.subplot(223)
        plt.plot(x2,y2)
        plt.show()

plot_cs()