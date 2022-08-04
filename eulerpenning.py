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
def fx(x,ydot):
    return wz**2/2*x-wc*ydot
def fy(y,xdot):
    return wz**2/2*y+wc*xdot
def fz(z):
    return -wz**2*z
#Starting loop for time iteration
for i in range(0,timesteps):    
    t[i]=tn
    x1[i]=x1n
    x2[i]=x2n
    y1[i]=y1n
    y2[i]=y2n
    z1[i]=z1n
    z2[i]=z2n       
    z1n=z1n+dt*z2n
    z2n=z2n+dt*fz(z1n)   
    x1n=x1n+dt*x2n
    y1n=y1n+dt*y2n
    x2n=x2n+dt*fx(x1n,y2n)
    y2n=y2n+dt*fy(y1n,x2n)     
    tn=tn+dt