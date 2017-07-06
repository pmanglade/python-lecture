#!/usr/bin/env python
a=1
b=-2
c=3
d=-4
e=5
#### p1 and p2 are the same polynome
#### computation of p1 is much longer than that of p2
import numpy as np
import matplotlib.pyplot as plt
def p1(x):
   return a*x**4+b*x**3+c*x**2+d*x+e
def p2(x):
   return (((a*x+b)*x+c)*x+d)*x+e

# p3 and p4 gives also the same result
# in a MORE GENERAL way since they use lists
coef=[e,d,c,b,a]
def p3(x):
   p=0
   t=1
   for i in range(5):
      p += coef[i]*t
      t *= x
   return p

coef=[a,b,c,d,e]
def p4(x):
   p=coef[0]
   for i in range(4):
      p = p*x+coef[i+1]
   return p

x = np.arange(-1,1,0.1)
y1= [p1(v) for v in x]
y2= [p1(v) for v in x]
y3= [p1(v) for v in x]
y4= [p1(v) for v in x]
plt.plot(x,y1,label="p1")
plt.plot(x,y2,label="p2")
plt.plot(x,y3,label="p3")
plt.plot(x,y4,label="p4")
plt.legend()
plt.show()
