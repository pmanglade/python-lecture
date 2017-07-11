#!/usr/bin/env python
from numpy import *
import matplotlib.pyplot as plt
def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)



def main():

   xv = []
   d  = []
   
   n=100
   I=range(n)
   for i in I:
      tmp_xv = i * 2*pi/(n-1)
      tmp_d = deriv1(cos,0.1,tmp_xv)

      xv.append(tmp_xv)
      d.append(tmp_d)
      
   ref = -sin(xv)

   print(ref)
   plt.plot(xv, d)
   plt.plot(xv, ref)
   
   plt.show()
   return

main()

