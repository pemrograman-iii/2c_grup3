# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:20:08 2019

@author: User
"""

from matplotlib import pyplot as plt

hasil = 1174091 % 3 + 2
print(hasil)

def pie():
    days = [1,2,3,4,5]
  
    sleeping =[10,10,8,10,7]
    eating = [2,2,2,2,2]
    working =[8,10,7,4,2]
    playing = [4,2,7,8,13]
    slices = [13,2,3,6]
    activities = ['sleeping','eating','working','playing']
    cols = ['c','m','r','b']

    for a in range(1,5):
        plt.subplot(2,2,a)
        plt.pie(slices,
                labels=activities,
                colors=cols,
                startangle=70,
                shadow= True,
                explode=(0,0.5,0,0),
                autopct='%1.1f%%')
 
    plt.title('contoh Pie')
    plt.show()