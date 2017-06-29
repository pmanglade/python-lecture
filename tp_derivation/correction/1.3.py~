#!/usr/bin/env python
from numpy import *

def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

n=1000
for i in range(n):
   x=(i*2*pi/n)
   d=deriv1(cos,0.1,x)
   print(x,d)
