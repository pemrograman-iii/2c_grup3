# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:40:19 2019

@author: User
"""

import serial

def error():
    try:
        ser = serial.Serial('COM5',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("syntax yang anda tulis salah")
    except NameError:
        print("nama yang dimasukkan tidak ada")
    except TypeError:
        print("tipe data salah")
    except:
        print("terjadi kesalahan")