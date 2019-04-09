# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:46:19 2019

@author: Engkay Rokayah
"""

def tryExceptError():
    try:
        from 1174075_bar import batang as bar
    except SyntaxError:
        print("Terjadi kesalahan penulisan")

tryExceptError()