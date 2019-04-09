# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:09:39 2019

@author: COMPAQ
"""

from matplotlib import pyplot as plt

def plot():

    hasil = 1174071 % 3 + 2
    
    x = [2030,2031,2032,2033,2034,2035]
    y = [88,87,120,122,148,170]
    x2 = [2030,2031,2032,2033,2034,2035]
    y2 = [67,97,114,110,146,165]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.plot(x,y,'b',label='Aliran Pedang Shinmei', linewidth=1)
        plt.plot(x2,y2,'r',label='Eye of Agomoto',linewidth=1)
        plt.title('Kekuatan Isekai')
        plt.ylabel('Damage')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='k')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()