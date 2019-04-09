# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:17:24 2019

@author: COMPAQ
"""

from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3]
        y=[5,2,4]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Wrong syntax")
    except NameError:
        print("There is no variable data")
    except TypeError:
        print("Wrong data type")
    except:
        print("There is a trouble in your face")
        
tryExceptError()