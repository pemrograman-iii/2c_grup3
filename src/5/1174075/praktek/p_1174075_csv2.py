# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 05:42:35 2019

@author: Engkay Rokayah
"""
import csvlist():
    
def csvlist():
    qith open('1174075.csv') as csv_file:
        csv_reade = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if row in csv_reader:
                if line_count == 0:
                    print(f'\t{0} works in the {row[1]}department, and was born in {row[2]}.')
                    line_count += 1
                print(f'processed {line_count} lines.')
                
def csvdictionary():
    with open('1174075.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file,delimitr=':')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'column names are {', ".join(row)}')
                line_count +=1
            print(f'\t{row["npm"]} works in the {row["nama"]} department, and was born in {row[tanggal lahir"]}.')
            line_count += 1
            print(f'processed {line_count} lines.')
csvdictionary()

def csvwrite():
    with open('1174075.csv', mode='w') as mhsFile:
    mhs = csv.write(mhsFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    mhs.writerow(['Data1', 'Data2', 'Data3', '22/5/1999'])
    mhs.writerow(['Namjoon', 'Jimin', 'Taeyung', '22/5/1999'])
#print(CSVModeList())
#CSVModeDict()
#WriteCSV(CSVModeList())