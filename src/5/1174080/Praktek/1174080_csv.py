# -*- coding: utf-8 -*-
import csv

def bacacsv():
    with open('hasil.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row[0])
            
bacacsv()