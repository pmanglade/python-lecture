#!/usr/bin/env python
from numpy import *

def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

n=1000
sumDif=0.;
h=0.1
for i in range(n):
   x=(i*2*pi/n)
   d=deriv1(cos,h,x)
   a=-sin(x)
   sumDif+=abs(d-a)
   print(x,d,sumDif)

sumDif /= n
print("ecart moyen pour h=",h," : ",sumDif)


