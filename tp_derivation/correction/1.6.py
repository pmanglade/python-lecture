#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
def deriv1(f,h,x):
   return (f(x+h)-f(x-h))/(2*h)

n=100
I= [i for i in range(n)]
xv = [i * 2*np.pi/(n-1) for i in I]
d = [deriv1(np.cos,0.01,v)+np.sin(v) for v in xv]
ref=np.sin(xv)*0.00001
print(ref)

# plotting

fig, ax = plt.subplots()
ax.xaxis.set_ticks(np.arange(0, 2*np.pi, 0.5))
plt.plot(xv, d)
plt.plot(xv, ref)
plt.show()




