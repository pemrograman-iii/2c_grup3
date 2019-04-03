# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:45:51 2019

@author: ASUS
"""

import serial

def ulang():
    ser = serial.Serial('COM4',9600)
    while(1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ulang()