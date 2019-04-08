# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:54:39 2019

@author: User
"""

from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
def bar():
    plt.bar([1.30,2.30,3.30,4.30,5.30],[5,2,4,1,2],
    label="NVIDIA",color='y',width=.5)
    plt.bar([1.80,2.80,3.80,4.80,5.80],[3,2,6,5,1],
    label="AMD", color='r',width=.5)
    
    
def hist():
    nilai = [11,12,23,25,77,80,90,96,97,96,93,65,43,22,78,77,67,88,90,96,97]
    mhs = [0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(nilai, mhs, histtype='bar', rwidth=0.8)

    
def area():
    days = [1,2,3,4,5]
      
    sleeping =[10,10,8,10,7]
    eating = [2,2,2,2,2]
    working =[8,10,7,4,2]
    playing = [4,2,7,8,13]
  
    plt.plot([],[],color='m', label='Sleeping', linewidth=5)
    plt.plot([],[],color='c', label='Eating', linewidth=5)
    plt.plot([],[],color='r', label='Working', linewidth=5)
    plt.plot([],[],color='k', label='Playing', linewidth=5)
      
    plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
      

plt.subplot(331)
bar()


plt.subplot(332)
bar()


plt.subplot(333)
hist()

plt.subplot(334)
bar()

plt.subplot(335)
area()

plt.subplot(336)
hist()

plt.subplot(337)
hist()

plt.subplot(338)
area()

plt.subplot(339)
bar()