#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:48:55 2024

@author: siobhanie
"""

from numpy import *

def newtons_method(x):
    
    for i in range(10):
        x = x - f(x)/fprim(x)
        
        
    return x


def f(x):
    return sin(x)

def fprim(x):
    return cos(x)


zero1 = newtons_method(1) 