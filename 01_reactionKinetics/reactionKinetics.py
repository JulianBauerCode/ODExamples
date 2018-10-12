#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt         # Plotting
import matplotlib

##################################################################
# Simplest example

# Define parameter
k = [0.1, 0.2, 0.3]     # Mol / second

# Define rate as function
def kineticsSimple(t, y):
    '''Pass k into funtcion as global variable'''
    return ( k[0] * y[0]          * np.array([-1.0, 1.0, 0.0]) \
           + k[1] * y[1] * y[2]   * np.array([ 1.0,-1.0, 0.0]) \
           + k[2] * y[1]          * np.array([ 0.0,-1.0, 1.0]) )

# Prepare plotting
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('Simplest example: '+'k = ['+' '.join([str(ki) for ki in k])+']')

# Solve
sol = solve_ivp(
            fun=kineticsSimple,
            t_span=[0, 8],      # Seconds
            y0=[1,2,3],         # Mol
            )
# Plot
for indexComp, comp in enumerate(sol.y):
    ax.plot(sol.t, comp, label='y[{}]'.format(str(indexComp)))

ax.set_ylabel('Concentration')
ax.set_xlabel('Time')
ax.legend()


##################################################################
# Define rate
def kinetics(t, y, k):
    '''Pass k into funtcion as additional parameter'''
    return ( k[0] * y[0]          * np.array([-1.0, 1.0, 0.0]) \
           + k[1] * y[1] * y[2]   * np.array([ 1.0,-1.0, 0.0]) \
           + k[2] * y[1]          * np.array([ 0.0,-1.0, 1.0]) )

##################################################################
# Study integration method

# Define parameter
k = [0.1, 0.1, 0.1] # Mol / second

# Prepare plotting
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('Study integration methods '+'k = ['+' '.join([str(ki) for ki in k])+']')

cmap = matplotlib.cm.get_cmap('Spectral')

methods = ['RK45', 'RK23', 'Radau', 'BDF', 'LSODA']
for index, method in enumerate(methods):
    colorIndex = index / (len(methods)-1)

    # Solve
    sol = solve_ivp(
                fun=lambda t, y: kinetics(t, y, k),
                t_span=[0, 8],      # Seconds
                y0=[1,2,3],         # Mol
                method=method,
                )
    # Plot
    for indexComp, comp in enumerate(sol.y):
        ax.plot(
            sol.t,
            comp,
            label='method = '+method if indexComp == 0 else None,
            color=cmap(colorIndex),
            )

ax.set_ylabel('Concentration')
ax.set_xlabel('Time')
ax.legend()

##################################################################
# Study kinetics parameter

# Prepare plotting
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('Study influence of k')

cmap = matplotlib.cm.get_cmap('Spectral')

# Define parameter
studyK = [
    [0.1, 0.1, 0.1],
    [1.1, 1.1, 1.1],
    [1.1, 0.1, 0.1],    
    [0.1, 1.1, 0.1], 
    [0.1, 0.1, 1.1], 
    ]

for index, k in enumerate(studyK):
    colorIndex = index / (len(studyK)-1)

    # Solve
    sol = solve_ivp(
                fun=lambda t, y: kinetics(t, y, k),
                t_span=[0, 8],      # Seconds
                y0=[1,2,3],         # Mol
                method='RK45',
                )
    # Plot
    for indexComp, comp in enumerate(sol.y):
        ax.plot(    
                sol.t,
                comp,
                label='k = ['+' '.join([str(ki) for ki in k])+']' if indexComp == 0 else None,
                color=cmap(colorIndex),
                )

ax.set_ylabel('Concentration')
ax.set_xlabel('Time')
ax.legend()


##################################################################
# Study initial values

# Prepare plotting
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.set_title('Study influence of y0')

cmap = matplotlib.cm.get_cmap('Spectral')

# Define parameter

k = [0.1, 0.1, 0.1] # Mol / second

studyY0 = [
    [1, 2, 3],
    [1, 1, 1],
    ]

for index, y0 in enumerate(studyY0):
    colorIndex = index / (len(studyY0)-1)

    # Solve
    sol = solve_ivp(
                fun=lambda t, y: kinetics(t, y, k),
                t_span=[0, 8],      # Seconds
                y0=y0,              # Mol
                method='RK45',
                )
    # Plot
    for indexComp, comp in enumerate(sol.y):
        ax.plot(    
                sol.t,
                comp,
                label='y0 = ['+' '.join([str(i) for i in y0])+']' if indexComp == 0 else None,
                color=cmap(colorIndex),
                )

ax.set_ylabel('Concentration')
ax.set_xlabel('Time')
ax.legend()





















plt.show()




