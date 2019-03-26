# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:31:09 2019

@author: Fernando Lorencius S
"""

import pandas
#no3
df = pandas.read_csv('csv_coba.csv')
print(df)

#no4
df = pandas.read_csv('csv_coba.csv')
uji = pandas.DataFrame.from_dict(df)
print(uji)

#no5
df = pandas.read_csv('csv_pandas.csv', parse_dates=['TanggalLahir'])
print(df)

#no6
df = pandas.read_csv('csv_pandas.csv', index_col='Nama')
print(df)

#no7
df = pandas.read_csv('csv_pandas.csv',
        header=0, 
        names=['Nama', 'tgl lahir','Gaji', 'Jatah Sakit'])
print(df)

def bacalistpandas():
    df = pandas.read_csv('csv_pandas.csv')
    print(df)

def write():
    df = pandas.read_csv('isipandas.csv', 
            index_col='Pekerjaan', 
            parse_dates=['tanggal'],
            header=0, 
            names=['Pekerjaan', 'Hired', 'tanggal', 'Sakit'])
    df.to_csv('d1174095_pandas_baru.csv')