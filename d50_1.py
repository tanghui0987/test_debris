from pylab import *
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
from scipy.interpolate import interp2d
# set parameter


# plot parameter
Dmin = 0.8
Dmax = 0.2
Dclass = 14
ccolor = linspace(Dmax,Dmin,Dclass)
#manual_locations = [(15,15),(30,20),(40, 32),(60, 48),(80,70),(80,65),(90,82),(98,87),(100,90),(70,60),(50,40)]

#load data
origin= 'lower'
x =linspace(xmin,xmax,xnum)
y =linspace(ymin,ymax,ynum)
X = loadtxt("x1.txt")
Y = loadtxt("y1.txt")
Z = zeros(shape=(len(x),len(y)))
Z = loadtxt("parameter.txt")

#refine data
xnew = linspace(xnew_min, xnew_max,xnew_num)
ynew = linspace(ynew_min, ynew_max,ynew_num)
f=interp2d(X,Y,Z,kind='cubic')
Znew=f(xnew,ynew)

#plot data
rc('font',family='Times New Roman')
plt.figure()
ax1= subplot(111)
jet=cm.copper_r
CS = plt.contourf(xnew, ynew, Znew, ccolor,cmap=jet,origin=origin)
CS2 = plt.contour(CS, levels=CS.levels,colors = 'black',origin=origin,hold='on',linewidths=3.5)
#plt.clabel(CS2, inline=1, fontsize=40,manual=manual_locations)
CS.ax.set_ylabel('Distance (m)',fontsize=45,labelpad=10.0,fontname='Times New Roman')
CS.ax.set_xlabel('Distance from Bank (m)',fontsize=45,labelpad=10.0,fontname='Times New Roman')

# We can still add a colorbar for the image, too.
CBI = plt.colorbar(CS, orientation='vertical', shrink=1.0)
CBI.add_lines(CS2)
CBI.ax.set_ylabel('D50 ($\phi$)',fontsize=45,labelpad=20.0,fontname='Times New Roman')
CBI.ax.tick_params(axis='y', labelsize=45,pad=10)
for axis in ['top','bottom','left','right']:
    CBI.ax.spines[axis].set_linewidth(5)

#CBI.ax.set_ylim(0.0,0.30)
ax1.tick_params(axis='x', labelsize=45,pad=10)
ax1.tick_params(axis='y', labelsize=45,pad=10)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(5)
ax1.xaxis.set_tick_params(width=5,length=7)
ax1.yaxis.set_tick_params(width=5,length=7)
show()
