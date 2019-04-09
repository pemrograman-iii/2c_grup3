# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:40:56 2019
@author: frnn
"""

#plt.plot([1,2,3,4], [1,4,9,16])
# In[1]: bar
#no3 
#Garis
x = (4,8,13,17,20)
y = (52, 65, 76, 66, 48)

import matplotlib.pyplot as Teo
Teo.plot([2,4,6,8,10],[15, 20, 17, 48, 17])
Teo.show()
# In[2]: bar
#Scatter
import matplotlib.pyplot as Teo
x = [6,6,9,15,11,13,18,25,32,31,35,42,47,53,55,67,62,73,75,76]
y = [78,73,43,5,23,99,129,30,78,23,68,73,24,84,45,153,231,23,212,234]
Teo.scatter(x,y)
Teo.show()
# In[3]: bar
#Histogram
import matplotlib.pyplot as Teo
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = Teo.hist(x, num_bins, facecolor = 'C')
Teo.show()
# In[4]: bar
#Pie chart
import matplotlib.pyplot as Teo
 
days = [1,2,3,4,5]
 
Mager =[2,6,6,10,7]
Makan = [5,5,4,4,2]
Tidur =[7,7,7,2,5]
Main = [10,6,7,8,10]
slices = [7,2,2,13]
activities = ['Mager','Makan','Tidur','main']
cols = ['c','m','r','b']
 
Teo.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0.1,0,0,0),
  autopct='%1.1f%%')
 
Teo.title('Pie Plot')
Teo.show()

# In[5]: bar
#area plot
import matplotlib.pyplot as Teo
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
Teo.plot([],[],color='k', label='mager', linewidth=5)
Teo.plot([],[],color='r', label='makan', linewidth=5)
Teo.plot([],[],color='c', label='tidur', linewidth=5)
Teo.plot([],[],color='m', label='main', linewidth=5)
  
Teo.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
  
Teo.xlabel('x')
Teo.ylabel('y')
Teo.title('mager masa gitu!')
Teo.legend()
Teo.show()

# In[5]: bar
#subplot
fig, ax = Teo.subplots(4, 4, sharex='col', sharey='row')