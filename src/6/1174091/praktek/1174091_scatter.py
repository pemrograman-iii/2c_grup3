# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:20:08 2019

@author: User
"""

from matplotlib import pyplot as plt

hasil = 1174091 % 3 + 2
print(hasil)

def scatter():
    x = [1,1.5,2,2.5,3,3.5,3.6]
    y = [7.5,8,8.5,9,9.5,10,10.5]
 
    x1=[6.1,6.2,6.3,7.1,7.2,8.1,9.5]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
 
    for a in range(1, 5):
        plt.subplot(2,2,a)
        plt.scatter(x,y, label='Dot hijau',color='g')
        plt.scatter(x1,y1,label='dot hitam',color='k')
        plt.xlabel('label x')
        plt.ylabel('label y')
        plt.title('Contoh Scatter Plot')
        plt.legend()
        plt.show()