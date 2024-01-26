#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 09:18:40 2024

@author: siobhanie
"""

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt

def f(x):
    return x



xs = linspace(0,1)
ys = [f(x) for x in xs]

plt.plot(xs,ys)