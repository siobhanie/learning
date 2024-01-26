#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:48:55 2024

@author: siobhanie
"""

from numpy import *
import numpy as np

def newtons_method(x):
    
    for i in range(80):
        x = x - f(x)/fprim(x)
        
        
    return x


def f(x):
    return np.sin(x)

def fprim(x):
    return np.cos(x)


x0 = 1.5
zero1 = newtons_method(x0) 
print(zero1)