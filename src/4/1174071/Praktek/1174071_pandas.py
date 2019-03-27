# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:11:34 2019

@author: COMPAQ
"""
import pandas

#No.3
def readlistpandas():
    rlp = pandas.read_csv('contoh.txt')
    print(rlp)
    
readlistpandas()

#No.4
def opendictlistpandas():
    odlp = pandas.read_csv('contoh.txt')
    odlp = pandas.DataFrame.from_dict(odlp)
    print(odlp)
    
opendictlistpandas()

#No5
def changedate():
    cd = pandas.read_csv('example.txt', parse_dates=['tanggal'])
    print(cd)
    
changedate()

#No.6
def changecollumn():
    cc = pandas.read_csv('contoh.txt')
    cc.index = ['Row_1', 'Row_2']
    print(cc)
    
changecollumn()

#No.7
def changecollumnname():
    ccn = pandas.read_csv('contoh.txt')
    ccn.columns =['Collumn_1', 'Collumn_2', 'Collumn_3'] 
    print(ccn)
    
changecollumnname()

def createpandas():
    cp = pandas.read_csv('coonto.txt', 
            names=['nama', 'kekuatan', 'isekainame', 'hobi'])
    cp.to_csv('pemogramanstone.csv')