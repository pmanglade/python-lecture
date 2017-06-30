#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
def derivC1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

def derivC2(f,h,x):
   return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

def derivC3(f,h,x):
   return (f(x+3*h)-9*f(x+2*h)+45*f(x+h)-45*f(x-h)+9*f(x-2*h)-f(x-3*h))/(60*h)

def derivF1(f,h,x):
   return (f(x+h)-f(x))/(h)

def derivF2(f,h,x):
   return (-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)

def derivF3(f,h,x):
   return (-15*f(x)+16*f(x+h)-f(x+4*h))/(12*h)



def msin(x):
   return -np.sin(x)

def ecart(deriv,f,df,h,n):
   sumDif=0.;
   for i in range(n):
      x=(i*2*np.pi/n)
      d=deriv(f,h,x)
      a=df(x)
      sumDif+=abs(d-a)      
   return sumDif/n

h=0.001
n=100;
I= [i for i in range(n)]
xv = [i * 2*np.pi/(n-1) for i in I]
dC1 = [derivC1(np.cos,0.001,v)+np.sin(v) for v in xv]
dC2 = [derivC2(np.cos,0.001,v)+np.sin(v) for v in xv]
dC3 = [derivC3(np.cos,0.001,v)+np.sin(v) for v in xv]
dF1 = [derivF1(np.cos,0.001,v)+np.sin(v) for v in xv]
dF2 = [derivF2(np.cos,0.001,v)+np.sin(v) for v in xv]
dF3 = [derivF3(np.cos,0.001,v)+np.sin(v) for v in xv]

plt.plot(xv, dC1)
plt.plot(xv, dC2)
plt.plot(xv, dC3)
plt.plot(xv, dF1)
plt.plot(xv, dF2)
plt.plot(xv, dF3)
plt.show()

h = 1e-3;
listeErrorC1=[]
listeErrorC2=[]
listeErrorC3=[]
listeErrorF1=[]
listeErrorF2=[]
listeErrorF3=[]
listeh=[]
for i in range(20) :
   listeErrorC1.append(ecart(derivC1,np.cos,msin,h,200))
   listeErrorC2.append(ecart(derivC2,np.cos,msin,h,300))
   listeErrorC3.append(ecart(derivC3,np.cos,msin,h,300))
   listeErrorF1.append(ecart(derivF1,np.cos,msin,h,300))
   listeErrorF2.append(ecart(derivF2,np.cos,msin,h,300))
   listeErrorF3.append(ecart(derivF3,np.cos,msin,h,300)) 
   listeh.append(h)
   h *= 2**(1./2)






# plotting

fig, ax = plt.subplots()
ax.xaxis.set_ticks(np.arange(0, 2*np.pi, 0.5))

plt.loglog(listeh, listeErrorC1,label="C1")
plt.loglog(listeh, listeErrorC2,label="C2")
plt.loglog(listeh, listeErrorC3,label="C3")
plt.loglog(listeh, listeErrorF1,label="F1")
plt.loglog(listeh, listeErrorF2,label="F2")
plt.loglog(listeh, listeErrorF3,label="F3")
plt.legend()

plt.show()



