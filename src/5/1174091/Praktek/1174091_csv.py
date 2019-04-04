# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:27:01 2019

@author: User
"""
import csv

def bacaCsv():
    with open('mahasiswa.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['nama'])
            
bacaCsv()