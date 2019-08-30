# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:11:28 2019

@author: Dave
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.1)
sindata = np.sin(x)
cosdata = np.cos(x)
tandata=np.tan(x)

plt.plot(x,sindata, label='Sin(x)')
plt.plot(x,cosdata, label ='Cos(x)')
plt.plot(x,tandata,label='Tan(x)')
plt.title("Cos, Sin, and Tan Graph for 1 cycle")
plt.legend()
plt.show()