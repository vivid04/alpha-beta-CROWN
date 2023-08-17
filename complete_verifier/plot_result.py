# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:48:59 2023

@author: hsc
"""


import glob
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker

import os

plt.close('all')
a=map(lambda x: x*0.01+0.01, range(3))
eps = list(a)
Acc=[0.97,0.66,0.04]

fig, ax=plt.subplots()
#color = 'tab:red'


lines=ax.plot(eps,Acc,'*-r', label='BaB-RLM')
lines=ax.plot(eps,[i+0.1 for i in Acc],'*-r', label='BaB-SR')
ax.set_xlabel('epsilon')
ax.set_ylabel('Verified Accuracy')
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=1))
lgends = plt.legend()
plt.show()


   # fig, ax1 = plt.subplots()

   
  #  ax1.set_xlabel('The size of state set')
    # ax1.set_ylabel('Policy average performance(reward)', color=color)
    # ax1.plot(x, y1 ,'r')
    # #ax1.plot(x,y1 ,'rs',label='Performance')


    # ax1.tick_params(axis='y', labelcolor='m')
    
    # ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
     
    # ax2.plot(x, y2, 'b', label="Learning efficiency" )
    # ax2.tick_params(axis='y', labelcolor='c')
    
 