#!/usr/bin/env python
from numpy import *
import matplotlib.pyplot as plt
def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

n=100
I= [i for i in range(n)]
xv = [i * 2*pi/(n-1) for i in I]
d = [deriv1(cos,0.1,v) for v in xv]
ref=-sin(xv)
print(ref)
plt.plot(xv, d)
plt.plot(xv, ref)

plt.show()


