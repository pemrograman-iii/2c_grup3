# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:35:35 2019

@author: HP
"""

from matplotlib import pyplot as coba

print(1174080%3+2)

def pie(): 
    aktivity = [7,2,2,14]
    game = [10,15,7]
    activities = ['Tidur','Makan','Kerja','Main']
    games = ['Builder','Survival','Action']
    cols = ['c','m','r','b']

    coba.subplot(221)
    coba.pie(aktivity,
             labels=activities,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.2,0,0,0),
             autopct='%1.1f%%')
    coba.title('Plot Pie Aktivitas')
    
    coba.subplot(222)
    coba.pie(game,
             labels=games,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    coba.title('Plot Pie Game')
    coba.show()