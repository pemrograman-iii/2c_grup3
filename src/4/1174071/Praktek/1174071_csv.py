# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:57:51 2019

@author: COMPAQ
"""

#No1
import csv

def readlist():
    with open('contoh.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])
            
            

readlist()                
    
#No2
def opendictlist():
    with open('contoh.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['nama'], row['kelas'], row['hobi'])



opendictlist()


def create():
    with open('coonto.txt', mode='w') as csv_file:
        fieldnames = ['nama', 'kekuatan', 'isekainame', 'hobi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'nama': 'Da Lopez', 'kekuatan': 'Aliran Pedang', 'isekainame': 'Shinmei', 'hobi': 'Ngerap'})
        writer.writerow({'nama': 'Captain Marvel', 'kekuatan': 'tesseracpower', 'isekainame': 'Captainu Marvelu', 'hobi': 'Ngerapotin'})

            