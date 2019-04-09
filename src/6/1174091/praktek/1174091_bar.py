# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:15:29 2019

@author: User
"""

from matplotlib import pyplot as plt

def bar():
    x = [1.30,2.30,3.30,4.30,5.30]
    y = [5,2,4,1,2]
    x2 = [1.80,2.80,3.80,4.80,5.80]
    y2 = [3,2,6,5,1]
    for a in range(1, 5):
        plt.subplot(2,2,a)
        plt.bar(x,y,label="NVIDIA",color='y',width=.5)
        plt.bar(x2,y2,label="AMD", color='r',width=.5)
        plt.legend()
        plt.xlabel('Days')
        plt.ylabel('Sold')
        plt.title('Contoh Bar')
        plt.show()
    