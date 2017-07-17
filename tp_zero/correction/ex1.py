#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
def f(x):
   a = 1
   b = 3
   c = -5
   d = 9
   return (x-a)*(x-b)*(x-c)*(x-d)*0.003

def g(x):
   return np.exp(np.cos(x)+0.5) - 2.*np.exp(np.sin(x/2.)) + np.sin(x)*x


########### TRACÉS DES DEUX FONCTIONS
x  = np.arange(-6.,6.,0.1)
y1 = [f(v) for v in x]
y2 = [g(v) for v in x]
y3 = [0. for v in x]
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()

########################### Dichotomie
def dichotomie(f,a,b,e):
   fa=f(a)
   fb=f(b)
   n=0
   la=[a]
   lb=[b]
   while b-a > e :
      m=(b+a)*0.5
      fm=f(m)
      n+=1
      if fa*fm > 0:
         a=m
         fa=fm
      elif fb*fm > 0:
         b=m
         fb=fm
      else:           #Shall happen only in case where f(m)==0
         a=m;b=m
         fa=fm;fb=fm;
      la.append(a)
      lb.append(b)
   return a,b,n,la,lb

print(dichotomie(f,-np.sqrt(2.),2,0.001))
print(dichotomie(g,-np.sqrt(2.),2,0.001))
print(dichotomie(f,-0,2,0.001))
a,b,n,la,lb=dichotomie(g,-np.sqrt(2.),2,0.00001)
x=[i+1 for i in range(len(la))]
y=[lb[i]-la[i] for i in range(len(la))]
y2=[2**-i for i in x]
plt.semilogy(x,y)
plt.semilogy(x,y2)
plt.show()
