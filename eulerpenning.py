"""
The code below was written by @author: https://github.com/DianaNtz and is an 
implementation of the Euler method. It solves in particular the coupled system 
of the ordinary differential equations obtained from the Lorentz force of a 
Penning trap.
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import os
import imageio
filenames = []
#some initial values
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
#starting loop for time iteration
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
    if(i%5000==0):
       fig = plt.figure()
       ax = p3.Axes3D(fig)
       x=np.cos(wm*t[:i])+0.15*np.cos(t[:i]*wc_mod)
       y=np.sin(wm*t[:i])+0.15*np.sin(t[:i]*wc_mod)
       z=0.7*np.cos(wz*t[:i])
       ax.plot(x, y, z,color='skyblue',linewidth=2)
       ax.plot(x1[:i], y1[:i],z1[:i],color='deeppink',linestyle='-.',linewidth=2)
       ax.set_xlim(-1.1,1.1)
       ax.set_ylim(-1.1,1.1)
       ax.set_zlim(-1.1,1.1)
       ax.set_xlabel("x(t)",fontsize= 15,labelpad=10)
       ax.set_ylabel("y(t)",fontsize= 15,labelpad=10)
       ax.set_zlabel("z(t)",fontsize= 15,labelpad=10)
       ax.zaxis.set_tick_params(labelsize=13)
       ax.yaxis.set_tick_params(labelsize=13)
       ax.xaxis.set_tick_params(labelsize=13)
       ax.set_xticks([-1,-0.5,0,0.5,1.0])
       ax.set_yticks([-1,-0.5,0,0.5,1.0])
       ax.set_zticks([-1,-0.5,0,0.5,1.0])
       ax.view_init(10, 210)
       #ax.view_init(90, 210)   #top view
       filename ='bla{0:.0f}.png'.format(i/5000)
       #append file name to the list filename
       filenames.append(filename)    
       #save the plot
       plt.savefig(filename,dpi=150)
       plt.close()    
#build the gif
with imageio.get_writer('analyvsnumeric.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)       
#remove saved figures 
for filename in set(filenames):
    os.remove(filename)  