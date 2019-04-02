import serial

def CheckSerial():
    ser = serial.Serial('/dev/ttyUSB0') #membuka port serial
    print(ser.name) #mengecek port jika sudah digunakan
    ser.close() #menutup port

CheckSerial()
