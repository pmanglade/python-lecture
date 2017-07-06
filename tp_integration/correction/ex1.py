#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def rectanglen(f,a,b,n):
   h=1.*(b-a)/(n)
   integrale = 0.
   for i in range(n):
      x=a+i*h
      integrale+=f(x)*h
   return integrale

def rectangleh(f,a,b,h):
   n=int(1.0*(b-a)/h)+1
   h=1.*(b-a)/(n)
   integrale = 0.
   for i in range(n):
      x=a+i*h
      integrale+=f(x)*h
   return integrale

def testRectangle(f,a,b,N,h):
   lx   = []
   lint = []
   for i in range(N):
      x = a + (b-a)/(N-1)*i
      lx.append(x)
      lint.append(rectangleh(f,a,x,h))
   return lx,lint

def ecart(l1,l2):
   e=0.
   for i in range(len(l1)):
      e += abs(l1[i]-l2[i])
   e /= len(l1)
   return e

################ 1.1 à 1.4
lx,lint=testRectangle(np.cos,0.,np.pi,100,0.01)
plt.plot(lx,lint)
plt.plot(lx,np.sin(lx))
plt.show()

################ 1.5 & 1.6

h=1e-4
g=4
lh = []
le = []
while (h<0.01):
   lx,lint=testRectangle(np.cos,0.,np.pi,100,h)
   le.append(ecart(lint,np.sin(lx)))
   lh.append(h)
   h *= g

plt.loglog(lh,le)
plt.loglog(lh,lh)
plt.show()





