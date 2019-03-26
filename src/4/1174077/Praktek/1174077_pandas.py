# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:56:18 2019

@author: ASUS
"""

import pandas

#Jawaban No. 3
def openModeListPandas():
    avn = pandas.read_csv('cocol.csv')
    print(avn)

#Jawaban No. 4
def openModeDictPandas():
    abc = pandas.read_csv('cocol.csv')
    avn = pandas.DataFrame.from_dict(abc)
    print(avn)
    
#Jawaban No. 5
def changeFormatTanggal():
    avn = pandas.read_csv('cocol.csv', parse_dates=['tanggal lahir'])
    print(avn)

#Jawaban No. 6
def changeIndexKolom():
    avn = pandas.read_csv('cocol.csv')
    avn.index = ['baris_1', 'baris_2']
    print(avn)

#Jawaban No. 7
def changeNamaKolom():
    avn = pandas.read_csv('cocol.csv')
    avn.columns =['kolom_1', 'kolom_2', 'kolom_3', 'kolom_4'] 
    print(avn)
    
def writeCsvPandas():
    avn = pandas.read_csv('cocol.csv', 
            index_col='nama', 
            parse_dates=['tanggal lahir'],
            header=0, 
            names=['nama', 'jenis kelamin', 'umur', 'tanggal lahir'])
    avn.to_csv('cobanulis2.csv')