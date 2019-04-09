# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:50:45 2019

@author: Frnncss
"""

def PeringatanError():
    try:
        from matplotlib import pyplot as plt
    except SyntaxError:
        print("Ada kesalahan dalam penulisan Syntax")
    except NameError:
        print("Variable yang dimasukkan tidak ada")
    except TypeError:
        print("Ada yang salah pada type data")
    except:
        print("Sedang terjadi sebuah kesalahan")

PeringatanError()