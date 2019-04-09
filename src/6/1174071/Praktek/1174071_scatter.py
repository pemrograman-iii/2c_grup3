# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:08:46 2019

@author: COMPAQ
"""

from matplotlib import pyplot as plt

def scatter():

    hasil = 1174071 % 3 + 2
    
    x = [1,2.5,3,3.4,3,3.6,7.6]
    y = [9.5,9,8.9,9,9.7,8,9.10]
     
    x1=[7,8.9,9,9.8,7,10.5,11]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='Pengguna Android',color='r')
        plt.scatter(x1,y1,label='Pengguna IOS',color='c')
        plt.xlabel('Dewasa')
        plt.ylabel('Anak-anak')
        plt.title('Penggunakan Mobile Device')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()