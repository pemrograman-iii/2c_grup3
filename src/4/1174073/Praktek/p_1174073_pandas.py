# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:49:49 2019

@author: ASUS
"""
import pandas 
def pandaslist():
    df = pandas.read_csv('1174073.csv')
    print(df)
    
def pandasdictionary():
    df = pandas.read_csv('1174073.csv')
    df.to_dict(orient='records')
    print(df)
pandasdictionary()

def pandastanggal():
    df = pandas.read_csv('1174073.csv',delimiter=';',parse_dates=['tanggal lahir'])
    print(df)
pandastanggal()
def pandasindex():
    df = pandas.read_csv('1174073.csv',delimiter=';',index_col='tanggal lahir')
    print(df)
pandasindex()

def pandasatribut():
    df = pandas.read_csv('1174073.csv',delimiter=';',
        header=0,
        names=['nama','tanggal lahir','npm'])
    print(df)
pandasatribut()

def pandaswrite():
    df = pandas.read_csv('1174073.csv', delimiter=';')
    df.to_csv('1174035_bikinan.csv')