#!/usr/bin/env python
from numpy import *
import matplotlib.pyplot as plt

def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

def msin(x):
   return -sin(x)

def ecart(f,df,h,n):
   sumDif=0.;
   for i in range(n):
      x=(i*2*pi/n)
      d=deriv1(f,h,x)
      a=df(x)
      sumDif+=abs(d-a)      
   return sumDif/n


def main():

   h = 1e-6;
   listeError=[]
   listeh=[]
   for i in range(25) :
      input_function = cos
      deriv_function = msin
      
      listeError.append(ecart(cos,msin,h,1000))
      listeh.append(h)
      h *= 2**(1./2)
   
   print(listeh,listeError)
   plt.loglog(listeh, listeError)
   plt.show()
   
   plt.plot(listeh, listeError)
   
   plt.show()
   return

main()

