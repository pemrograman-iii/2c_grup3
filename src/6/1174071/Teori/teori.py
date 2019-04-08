# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:16:52 2019

@author: COMPAQ
"""

import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

plt.plot(x,y)
plt.show()
#%%
import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

plt.bar(x,y)
plt.show()
#%%
import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (2)

plt.hist(x,y)
plt.show()
#%%
import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

plt.scatter(x,y)
plt.show()

#%%
import matplotlib.pyplot as plt
x = (6,10,15,19,22)
y = (44, 37, 88, 68, 35)
plt.bar(x,y, label='Perasaan Cinta')

x1 = (4,8,13,17,20)
y1 = (54, 67, 98, 78, 45)
plt.bar(x1,y1, label='Perasaan Sayang')

plt.legend()
plt.show()
#%%
#subplot
import matplotlib.pyplot as plt
x = [2,4,5,8,10]
y = [12,14,16,18,20]
plt.subplot(331)
plt.bar(x, y)
plt.subplot(332)
plt.hist(x, 2)
plt.subplot(333)
plt.scatter(x, y)
plt.subplot(334)
plt.plot(x, y)
plt.subplot(335)
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