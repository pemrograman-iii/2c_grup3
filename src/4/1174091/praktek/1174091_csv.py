# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:28:43 2019

@author: User
"""

#jawaban 1

import csv
def ModeList():
    with open('mahasiswa.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row[0],row[1],row[2])

#jawaban 2

def ModeDict():
    with open('employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'],row['nama'],row['kelas'])