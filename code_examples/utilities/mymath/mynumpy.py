#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:45:14 2018
Example of function using numpy.
@author: Michael
"""
def plotting():
# Plotting using numpy and matplotlib
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    N = 20
    θ = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    
    ax = plt.subplot(111, polar=True)
    bars = ax.bar(θ, radii, width=width, bottom=0.0)
    
    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)
    
    plt.show()