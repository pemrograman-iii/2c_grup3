# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:38:55 2019

@author: ASUS
"""

import serial

def ambildata():
    ser = serial.Serial('COM4',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ambildata()

import csv

def tuliscsv():
    ser = serial.Serial('COM4',9600)
    with open('ainul.csv',mode='w') as csv_file:
        fieldnames = ['jarak']
        writer = csv.DictWriter(csv_file, fieldname=fieldnames)

        writer.writeheader()
        while(1):
            data = ser.readline().decode("utf-8").strip('\n').strip('r')
            writer.writerow({'jarak': data})
            
tuliscsv()