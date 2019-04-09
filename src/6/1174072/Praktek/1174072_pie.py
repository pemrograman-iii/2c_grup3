# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:49:11 2019

@author: Chandra Kirana Poetr
"""

#%% Nomor 3
from matplotlib import pyplot as coba

print(1174072%3+2)

def pie_cs():
    kegiatan = [7,2,2,14]
    game = [7,15,7]
    txt = [10,5,6,1]
    gabut = ['main hp','Makan','jalan','Main']
    games = ['CSGO','CSO','CS 1.6']
    mager = ['drakor','music','tidur','santai']
    cols = ['c','m','r','b']

    coba.subplot(221)
    coba.pie(kegiatan,
             labels=gabut,
             colors=cols,
             startangle=10,
             shadow= True,
             explode=(0.2,0,0,0),
             autopct='%1.1f%%')
    coba.title('Plot Pie Kegiatan')
    
    coba.subplot(222)
    coba.pie(game,
             labels=games,
             colors=cols,
             startangle=80,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    coba.title('Plot Pie Main')
    
    coba.subplot(223)
    coba.pie(txt,
             labels=mager,
             colors=cols,
             startangle=70,
             shadow=True,
             explode=(.1,0,0,0),
             autopct='%1.1f%%')
    coba.title('Plot Pie Mager')
    coba.show()
        
pie_cs()