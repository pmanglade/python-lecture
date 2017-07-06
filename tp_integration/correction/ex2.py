#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def rectg(f,a,b,h):
    s=0.
    n=int((b-a)/h)+1
    h=(b-a)/n
    for i in range(n):
       x = a+i*h
       s += f(x)*h
    return s

def rectd(f,a,b,h):
    s=0.
    n=int((b-a)/h)+1
    h=(b-a)/n
    for i in range(n):
       x = a+(i+1)*h
       s += f(x)*h
    return s

# This function compute (almost) bondaries to the integral of f over [a,b]
# Coding style is tuned for best readability
def rectencadrement(f,a,b,h):
    sp=0.
    sm=0.
    n=int((b-a)/h)+1
    h=(b-a)/n
    for i in range(n):
       xm = a+i*h
       xp = xm+h
       fm = f(xm)
       fp = f(xp)
       if fp > fm :
          sm += fm
          sp += fp
       else :
          sm += fp
          sp += fm
    sm *=h
    sp *=h
    return sm,sp

#comparaison des intégrations sur des fonctions monotones
rd = rectd(np.cos,0,np.pi/2.,0.1)
rg = rectg(np.cos,0,np.pi/2.,0.1)
ex = np.sin(np.pi/2)
print("minoration : ",rd)
print("~exact     : ",ex)
print("majoration : ",rg)
rd = rectd(np.exp,0,np.pi/2.,0.1)
rg = rectg(np.exp,0,np.pi/2.,0.1)
ex = np.exp(np.pi/2)-1.
print("minoration : ",rg)
print("~exact     : ",ex)
print("majoration : ",rd)

#Utilisation de la fonction d'encadrement
print("\nThe next result is supposed to mimic the previous")
sm,sp = rectencadrement(np.cos,0,np.pi/2.,0.1)
ex = np.sin(np.pi/2)          
print("minoration : ",sm)
print("~exact     : ",ex)
print("majoration : ",sp)
sm,sp = rectencadrement(np.exp,0,np.pi/2.,0.1)
ex = np.exp(np.pi/2)-1          
print("minoration : ",sm)
print("~exact     : ",ex)
print("majoration : ",sp)         

print("\nTry on something bigger")
sm,sp = rectencadrement(np.cos,0,np.pi*2.,0.1)
ex = np.sin(np.pi*2)
print("minoration : ",sm)
print("~exact     : ",ex)
print("majoration : ",sp)         





