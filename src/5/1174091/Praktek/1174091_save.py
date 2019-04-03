# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:13:51 2019

@author: User
"""
import serial

def loop():
    ser = serial.Serial("COM5",9600)
    while (1):
        data = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(data)
    
loop()