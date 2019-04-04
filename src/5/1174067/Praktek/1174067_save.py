import serial

def ReadSerialLoop():
    ser = serial.Serial("COM5",9600)
    while (1):
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(read)
    
ReadSerialLoop()
