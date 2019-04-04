# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:06:50 2019

@author: Engkay Rokayah
"""

import csv

def csvlist():
    with open('1174075.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t(0) works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} line. ')
        
def csvdictionary():
    with open('1174075.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["kelas"]} works in the {row["nama"]} tanggal lahir, and was born in {row["tanggal lahir"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')
csvdictionary()
def csvwrite():
    with open('1174075.csv', mode='w') as mhsFile:
        mhs = csv.writer(mhsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        mhs.writerow(['Data1', 'Data2', 'Data3', '22/5/1999'])
        mhs.writerow(['Namjoon', 'Jimin', 'Taeyung', '22/5/1999'])