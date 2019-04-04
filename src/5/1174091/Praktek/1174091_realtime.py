# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:22:59 2019

@author: User
"""
#no 1
import serial

ser = serial.Serial('COM5',9600)

def coba():
    data = ser.readline().decode("utf-8").strip('\n').strip('\r')
    print(data)
    
#no 3
import csv

def cobaCsv():
    
    with open('mahasiswa.csv', mode='w') as csv_file:
        field = ['nama']
        tulis = csv.DictWriter(csv_file, fieldnames=field)
        data = ser.readline().decode("utf-8").strip('\n').strip('\r')
        tulis.writerow({'nama': data})
