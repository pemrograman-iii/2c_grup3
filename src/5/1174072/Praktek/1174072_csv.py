# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:51:52 2019

@author: Frnn
"""

import csv

def bacaCsv():
    with open('1174087.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])