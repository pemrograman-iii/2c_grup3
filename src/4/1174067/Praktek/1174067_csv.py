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

def Write():
    with open('employee_file2.csv', mode='w') as csv_file:
        namakolom = ['emp_name', 'dept', 'birth_month']
        writer = csv.DictWriter(csv_file, fieldnames=namakolom)
    
        writer.writeheader()
        writer.writerow({'emp_name': 'Kaka Kamaludin', 'dept': 'IT', 'birth_month': 'Sep'})