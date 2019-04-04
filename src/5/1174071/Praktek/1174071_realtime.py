# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:00:24 2019

@author: COMPAQ
"""

import serial

def getData():
    ser = serial.Serial('COM5',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

getData()

import serial
import csv

def writeCsv():
    ser = serial.Serial('COM5',9600)
    with open('praktek5.txt', mode='w') as csv_file:
        fieldnames = ['jarak']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'jarak': data})
            
writeCsv()