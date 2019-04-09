# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:43:29 2019

@author: COMPAQ
"""

from matplotlib import pyplot as plt

def bar():

    hasil = 1174071 % 3 + 2
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.bar([2030.7,2031.7,2032.7,2033.7,2034.7,2035.7],[9,9.5,10,15,20,25],
        label="Mobil Listrik",color='b',width=.3)
        plt.bar([2031,2032,2033,2034,2035,2036],[20,25,30,35,40,45],
        label="Motor Listrik",color='r',width=.3)
        plt.bar([2031.3,2032.3,2033.3,2034.3,2035.3,2036.3],[10,11,15,17,20,30],
        label="Mobil Terbang",color='g',width=.3)
        plt.legend()
        plt.xlabel('Tahun')
        plt.ylabel('Pengguna (Juta)')
        plt.title('Jenis transportasi yang digunakan di masa depan')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
    plt.show()