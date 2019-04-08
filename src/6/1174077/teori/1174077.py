# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:44:38 2019

@author: ASUS
"""
#%%
from matplotlib import pyplot as plt

x=[1,2,3]
y=[4,5,1]
plt.plot(x,y)
plt.show()
#%%
from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[50,40,70,80,20],
label="Ferrari",color='Y',width=.5)
plt.bar([2,4,6,8,10],[80,20,20,50,60],
label="BMW", color='C',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()
#bar
#%%
from matplotlib import pyplot as plt

population_age = [40,80,11,22,16,9,10,15,22,55,62,45,21,22,102,95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()
#histogram
#%%
from matplotlib import pyplot as plt

x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='Pendapatan Tinggi Tapi Penyimpanan Rendah',color='C')
plt.scatter(x1,y1,label='Pendapatan Rendah Tapi Penyimpanan Tinggi',color='M')
plt.xlabel('Pensimpanan dalam ratusan')
plt.ylabel('Pendapatan dalam ribuan')
plt.title('Diagram Titik')
plt.legend()
plt.show()
#scatter
#%%
from matplotlib import pyplot as plt

plt.plot(x,y)
plt.show
#line
#%%
from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [6,7,8,9,10]
plt.subplot(331)#tinggi,lebar,urutan
plt.plot(x, y)
plt.subplot(332)
plt.bar(x, y)
plt.subplot(333)
plt.hist(x, 2)
plt.subplot(334)
plt.scatter(x, y)
plt.subplot(335)#tinggi,lebar,urutan
plt.plot(x, y)
plt.subplot(336)
plt.bar(x, y)
plt.subplot(337)
plt.hist(x, 2)
plt.subplot(338)
plt.scatter(x, y)
plt.subplot(339)
plt.hist(x, 2)
plt.show()
#subplot
#%%
from matplotlib import pyplot as plt

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plt.hist(x, 5,  histtype ='bar' , rwidth =0.8)
plt.xlabel('Angka')
plt.ylabel('Banyaknya angka rentang dari 5')
plt.show()
#histogram2
#%%