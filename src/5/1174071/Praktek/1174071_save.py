# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:37:48 2019

@author: COMPAQ
"""

import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()