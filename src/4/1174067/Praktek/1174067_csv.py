import csv

def ListMode():
    with open('employee_birthday.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
    
def DictMode():
    with open('employee_birthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
