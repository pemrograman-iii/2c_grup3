# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:20:36 2019

@author: Frnn
"""

from matplotlib import pyplot as pra

print(1174072%3+2)


def bar_cs():
        x = [2,4,6,8,10]
        y = [5,10,15,20,25] 
        
        x1 = [10,20,30,40,50,60,70]
        y1 = [5,10,15,20,25,30,35]
        
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [20,19,18,17,16,15,14,13,12,11]
        
        pra.subplot(221)
        pra.bar(x,y)
        pra.subplot(222)
        pra.bar(x1,y1)
        pra.subplot(223)
        pra.bar(x2,y2)
        pra.show()
bar_cs()