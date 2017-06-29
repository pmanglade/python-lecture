#!/usr/bin/env python
from numpy import *

def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

print(deriv1(cos,0.2,0))
print(deriv1(cos,0.2,3.14/2.))
print(deriv1(cos,0.2,3.14))
