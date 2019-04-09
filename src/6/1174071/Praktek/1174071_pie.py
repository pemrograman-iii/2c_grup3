# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:09:16 2019

@author: COMPAQ
"""

from matplotlib import pyplot as plt

def pie():

    hasil = 1174071 % 3 + 2
    
    slice = [5,10,30,22]
    makanan = ['Nasi Padang','KFC','Warteg','Mie Instan']
    warna = ['r','b','c','g']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(slice,
        labels=makanan,
        colors=warna,
        startangle=90,
        shadow= True,
        explode=(0,0,0,0.2),
        autopct='%1.1f%%')         
        plt.title('Makanan anak kost')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()