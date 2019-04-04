# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:57:12 2019

@author: Engkay Rokayah
"""

import pandas
def pandaslist():
    df = pandas.read_csv('1174075.csv')
    print(df)

def pandasdictionary():
    df = pandas.read_csv('1174075.csv')
    df.to_dict(orient='records')
    print(df)
pandasdictionary()

def pandastanggal():
    df = pandas.read_csv('1174075.csv',parse_dates=['tanggal lahir'])
    print(df)
pandastanggal()

def pandasindex():
    df = pandas.read_csv('1174075.csv',parse_dates=['tanggal lahir'])
    print(df)
pandasindex()

def pandasatribut():
    df = pandas.read_csv('1174075.csv',delimiter=',',
         header=0,
         names=['nama', 'kelas' , 'tanggal lahir'])
    print(df)
pandasatribut()

def pandaswrite():
    df = pandas.read_csv('1174075.csv')
    df.to_csv('1174075_bikin.csv')