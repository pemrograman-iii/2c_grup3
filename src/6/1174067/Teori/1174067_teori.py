import matplotlib.pyplot as plt

##1
#Penulisan sumbu X dan Y
plt.plot([8 , 4, 20, 19],[9, 6, 19, 98],'rH-.')
plt.show()

#
x=[8 , 4, 20, 19]
y=[9, 6, 19, 98]
plt.plot(x, y, 'rH-.')
plt.show()

##2
#line chart
plt.plot([8 , 4, 20, 19],[9, 6, 19, 98],'rH-.')
plt.show()

#Pie chart
import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0.1,0,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()

#Bar chart
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",color='m',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

#Scatter chart
import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('simpanan dalam ratusan')
plt.ylabel('pendapatan dalam ribuan')
plt.title('Scatter Plot')
plt.legend()
plt.show()

#Histogram chart
import matplotlib.pyplot as plt
population_age = [11,22,16,9,10,15,22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8, color='K')
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()

#Stack Chart
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
  
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()

##4
from matplotlib import pyplot as plt
from matplotlib import style
 
style.use('ggplot')
x = [2, 3, 3.5, 4, 5, 6, 6.6]
y = [101 , 202, 250, 322, 357, 380, 400 ]
x2 = [2, 3, 3.5, 4, 5, 6, 6.6]
y2 = [201 , 302, 410, 370, 350, 335, 301 ]
plt.plot(x,y,'r',label='GT-R Horsepower', linewidth=2)
plt.plot(x2,y2,'b',label='GT-R Torque',linewidth=2)
plt.title('2009 Nissan GT-R (JDM)' "\n" 'Herman Motive (Mustang Dyno)')
plt.ylabel('Hosepower(hp)' "\n" 'Torque(lb-ft)')
plt.xlabel('Engine Speed (RPM x 1000)')
plt.legend()
plt.grid(True,color='#999999')
plt.show()

##5
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1 * np.pi, 100)
y = np.sin(x ** 3)

f, axarr = plt.subplots(3, 3)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 1].plot(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
axarr[1, 1].plot(x, y)
axarr[1, 1].set_title('Axis [1,1]')
axarr[1, 2].plot(x, y)
axarr[1, 2].set_title('Axis [1,2]')
axarr[2, 1].plot(x, y ** 2)
axarr[2, 1].set_title('Axis [2,1]')
axarr[2, 2].plot(x, y)
axarr[2, 2].set_title('Axis [2,3]')
axarr[0, 2].plot(x, y)
axarr[0, 2].set_title('Axis [0,2]')
axarr[2, 0].plot(x, y ** 2)
axarr[2, 0].set_title('Axis [2,0]')

plt.show()

##6
#contoh penulisan warna
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

plt.close('all')

f, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.plot(x, y, color='0.5')
ax2.plot(x, y, color='tab:red')
ax3.plot(x, y, color='g')
ax4.plot(x, y, color='xkcd:deep blue')

f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

plt.show()

#%% Histogram 2
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plt.hist(x, 5,  histtype ='bar' , rwidth =0.8)
plt.xlabel('Angka')
plt.ylabel('Banyaknya angka rentang dari 5')
plt.show()
