# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:37:21 2019

@author: HP
"""

from matplotlib import pyplot as coba

print(1174080%3+2)

def titik():
    x = [2,4,6,8,10,12,14]
    y = [15,30,45,60,75,90,105]

    x1 = [10,7,18,9,30]
    y1 = [4,9,12,7,7]

    coba.subplot(221)
    coba.scatter(x,y)
    coba.subplot(222)
    coba.scatter(x1,y1)
    coba.show()