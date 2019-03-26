# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:04:16 2019

@author: HP
"""

import csv

def modelistcsv():
    with open('databaca.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])
            
def modediccsv():
    with open('databaca.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['tanggal lahir'])

def menuliscsv():
    data = {
    ('Bobi', 'D4TI2C', 90),
    ('Handi','D4TI2C',90)
    }
    data_file = open('datatulis_csv.csv', 'w')
    w = csv.writer(data_file)
    w.writerow(('Nama','Kelas','Nilai'))
    for s in data:
        w.writerow(s)