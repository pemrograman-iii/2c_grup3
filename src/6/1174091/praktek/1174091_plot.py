# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:19:23 2019

@author: User
"""

from matplotlib import pyplot as plt

hasil = 1174091 % 3 + 2
print(hasil)
def plot():


    
    x = [1000,1100,1200,1300,1400,1500]
    y = [1,4,3,2,5,6]
    x2 = [1000,1100,1200,1300,1400,1500]
    y2 = [2,1,3,4,6,5]
    
    for a in range(1, 5):
        plt.subplot(2,2,a)
        plt.plot(x,y,'b',label='label 1', linewidth=1)
        plt.plot(x2,y2,'r',label='label 2',linewidth=1)
        plt.title('plot')
        plt.ylabel('vertikal')
        plt.xlabel('horizontal')
        plt.legend()
        plt.grid(True,color='k')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()