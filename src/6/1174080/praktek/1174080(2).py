# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:33:02 2019

@author: HP
"""

def tryExceptError():
    try:
        from 1174080_bar import pasti as bar
    except SyntaxError:
        print("Terjadi Kesalahan Penulisan")

tryExceptError()