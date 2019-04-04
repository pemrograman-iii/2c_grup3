import serial

def ReadSerial():
    ser = serial.Serial("COM5",9600)
    read = ser.readline().decode("utf-8").strip('\n').strip('\r')
    print(read)
    
ReadSerial()


import csv

def write():
    with open("1174084.csv", mode='w') as nama_file:
        tulis_file = csv.writer(nama_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ser = serial.Serial("COM7",9600)
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        tulis_file.writerow([read])
        
write()
