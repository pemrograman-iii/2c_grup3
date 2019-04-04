# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:40:16 2019

@author: COMPAQ
"""

    
import csv

def readCsv():
    with open('praktek5.txt', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
            
readCsv()