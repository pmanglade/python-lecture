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


def myf(x):
   return np.cos(np.sin(x*x)*x+2*np.cos(x+1))
   

wf = open("function.dat","w")
for x in np.arange(0.1,5,0.01):
   wf.write(str(x)+" "+str(myf(x))+"\n")     ## deprecated mostly
   ##wf.write('{} {}\n'.format(x,myf(x)))    ## more 'modern'

wf.close()

rf = open("function.dat","r")
lines = rf.readlines()
x = []
y = [] 
for line in lines:
    p = line.split()    
    x.append(float(p[0]))
    y.append(float(p[1]))
rf.close()


j=0
der = [None] * len(x) # so that der has the size of x
for i in range(len(x)-2) :
   j=i+1
   der[j] = (y[j+1]-y[j-1])/(x[j+1]-x[j-1])

der[0] = (-3*y[0]+4*y[1]-y[2])/(x[2]-x[0])
j=(len(x)-1)
der[j] = (-3*y[j]+4*y[j-1]-y[j-2])/(x[j-2]-x[j])

plt.plot(x,y)
plt.plot(x,der)
plt.show()


