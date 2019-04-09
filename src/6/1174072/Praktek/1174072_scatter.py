# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:47:48 2019

@author: Frnn
"""

#%% Nomor 2
from matplotlib import pyplot as plt

print(1174072%3+2)

def scatter_cs():
        x = [1,2,3,4,5]
        y = [2,3,6,5,7]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        plt.subplot(221)
        plt.scatter(x,y)
        plt.subplot(222)
        plt.scatter(x1,y1)
        plt.subplot(223)
        plt.scatter(x2,y2)
        plt.show()
   
scatter_cs()