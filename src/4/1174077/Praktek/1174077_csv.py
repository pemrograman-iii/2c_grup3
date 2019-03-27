# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:59:10 2019

@author: ASUS
"""

import csv

#Jawaban No. 1
def openModeListCsv():
    with open('cocol.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def openModeDictCsv():
   with open('cocol.csv', mode='r') as csv_file:
       csv_reader = csv.DictReader(csv_file)
       for row in csv_reader:
           print(row['nama'], row['jenis kelamin'], row['umur'])

def writeCsv():
    with open('cobanulis.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174077', 'nama': 'Alvan Alvanzah', 'kelas': 'D4 TI 2C', 'tanggal lahir': '01/08/1999'})
        writer.writerow({'npm': '1174088', 'nama': 'Budi Doremi', 'kelas': 'D4 TI 2C', 'tanggal lahir': '11/7/1999'})