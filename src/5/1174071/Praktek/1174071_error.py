# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:42:21 2019

@author: COMPAQ
"""

    
import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan pada syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi kesalahan")
        
tryExceptError()