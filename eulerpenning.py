"""
@author: Diana Nitzschke
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import os
import imageio
#Some initial values
wc=28
wz=6.77 
wm=wc/2-np.sqrt(wc**2/4-wz**2/2)
wc_mod=wc/2+np.sqrt(wc**2/4-wz**2/2)
dt=0.005711986642890533*10**-3
tfinal=2*np.pi/np.abs(wm)
t0=0
timesteps=int((tfinal-t0)/dt)
x10=np.cos(wm*t0)+0.15*np.cos(t0*wc_mod)
y10=np.sin(wm*t0)+0.15*np.sin(t0*wc_mod)
z10=0.7*np.cos(wz*t0)
x20=(-np.sin(wm*t0)*wm-0.15*np.sin(t0*wc_mod)*wc_mod)
y20=(np.cos(wm*t0)*wm+0.15*np.cos(t0*wc_mod)*wc_mod)
z20=-0.7*np.sin(wz*t0)*wz
t=np.empty(timesteps, dtype='double')
tn=t0
x1=np.empty(timesteps, dtype='double')
x1n=x10
x2=np.empty(timesteps, dtype='double')
x2n=x20
y1=np.empty(timesteps, dtype='double')
y1n=y10
y2=np.empty(timesteps, dtype='double')
y2n=y20
z1=np.empty(timesteps, dtype='double')
z1n=z10
z2=np.empty(timesteps, dtype='double')
z2n=z20
