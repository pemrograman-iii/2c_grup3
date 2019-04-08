# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:23:12 2019

@author: User
"""
from matplotlib import pyplot as plt

#jawaban 2 dan 3

x=[3,6,4]
y=[1,6,4]
plt.plot(x,y)
plt.title('contoh')
plt.show
#jawaban 3
#bar
plt.bar([1.30,2.30,3.30,4.30,5.30],[5,2,4,1,2],
label="NVIDIA",color='y',width=.5)
plt.bar([1.80,2.80,3.80,4.80,5.80],[3,2,6,5,1],
label="AMD", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Sold')
plt.title('Contoh Bar')
plt.show()

#histogram
nilai = [11,12,23,25,77,80,90,96,97,96,93,65,43,22,78,77,67,88,90,96,97]
mhs = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(nilai, mhs, histtype='bar', rwidth=0.8)
plt.xlabel('Nilai')
plt.ylabel('Banyak Mahasiswa')
plt.title('Contoh Histogram')
plt.show()

#Scatter
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[6.1,6.2,6.3,7.1,7.2,8.1,9.5]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='Dot hijau',color='g')
plt.scatter(x1,y1,label='dot hitam',color='k')
plt.xlabel('label x')
plt.ylabel('label y')
plt.title('Contoh Scatter Plot')
plt.legend()
plt.show()

#area plot
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
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Plot')
plt.legend()
plt.show()

#pie
days = [1,2,3,4,5]
  
sleeping =[10,10,8,10,7]
eating = [2,2,2,2,2]
working =[8,10,7,4,2]
playing = [4,2,7,8,13]
slices = [13,2,3,6]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=70,
  shadow= True,
  explode=(0,0.5,0,0),
  autopct='%1.1f%%')
 
plt.title('contoh Pie')
plt.show()

#jawaban 5