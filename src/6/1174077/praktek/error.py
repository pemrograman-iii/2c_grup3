# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:24:36 2019

@author: ASUS
"""

from matplotlib import pyplot as plt

x = [9,10,11,12,13,14,15]
y = [21,22,25,31,67,56,30]

x1 = [4,7,9,3,6]
def tryExceptError():
    try:
        plt.plot(x,x1)
        plt.show()
    except ValueError:
        print("Nilai yang dimasukkan ada masalah")
    except NameError:
        print("Variabel yang di cari tidak ada")
    except SyntaxError:
        print("Penulisan syntax ada masalah")
    except:
        print("Sepertinya ada sedikit masalah")
        
tryExceptError()