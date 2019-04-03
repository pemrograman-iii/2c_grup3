# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:50:35 2019

@author: Frnn
"""

import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data ada yang salah")
    except:
        print("Terjadi sebuah kesalahan")

tryExceptError()