# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:18:42 2019

@author: User
"""
import pandas
#jawaban 3
def pandasModeList():
    df = pandas.read_csv('mahasiswa.csv')
    print(df)
    
#jawaban 4
def pandasModeDict():
    df = pandas.read_csv('mahasiswa.csv', parse_dates=['tanggal_masuk'])
    print(df)
    

#jawaban 5
def pandasUbahTanggal():
    df = pandas.read_csv('mahasiswa.csv', parse_dates=['tanggal_masuk'])
    print(df)

#jawaban 6
def ubahIndexKolom():
    df = pandas.read_csv('mahasiswa.csv', index_col=['nama'])
    print(df)
    
#jawaban 7
def ubahattribut():
    df = pandas.read_csv('mahasiswa.csv', names=['nama mahasiswa','kls','nomor','tanggal'])
    print(df)
    
ubahattribut()