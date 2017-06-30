#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
def derivC1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

def dderivC1(f,h,x):
   return (derivC1(f,h,x+h)-derivC1(f,h,x-h))/(2*h)

def dderiv(f,h,x):
   return (f(x+h)+f(x-h)-2*f(x))/(h*h)

def mcos(x):
   return -np.cos(x)

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
dd1 = [dderivC1(np.cos,0.001,v)+np.cos(v) for v in xv]
dd2 = [dderiv(np.cos,0.001,v)+np.cos(v) for v in xv]


plt.plot(xv, dd1)
plt.plot(xv, dd2)
plt.show()

h = 1e-5;
listeErrorC1=[]
listeErrorC2=[]

listeh=[]
for i in range(20) :
   listeErrorC1.append(ecart(dderivC1,np.cos,mcos,h,200))
   listeErrorC2.append(ecart(dderiv,np.cos,mcos,h,200))
   listeh.append(h)
   h *= 2**(1./2)



# plotting
fig, ax = plt.subplots()
ax.xaxis.set_ticks(np.arange(0, 2*np.pi, 0.5))

plt.loglog(listeh, listeErrorC1,label="C1")
plt.loglog(listeh, listeErrorC2,label="C2")

plt.legend()

plt.show()



