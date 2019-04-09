# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:03:09 2019

@author: ASUS
"""

from matplotlib import pyplot as plt

print(1174077%3+2)

def pie_chart(): 
    aktivity = [1,6,2,4]
    game = [14,1,9]
    buah = ['nanas','anggur','sirsak','apel']
    hewan = ['kelinci','anjing','garuda']
    cols = ['b','g','r','y']

    plt.subplot(221)
    plt.pie(aktivity,
             labels=buah,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.1,0,0,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Buah')

    plt.subplot(222)
    plt.pie(game,
             labels=hewan,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Hewan')
    plt.show() 