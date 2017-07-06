#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
def rectangle(f,a,b,n):
   h=(b-a)/n
   s=0.
   for i in range(n):
      x  = a+(i)*h
      s += f(x)
   s *=h
   return s

def trapeze (f,a,b,n):
   h=(b-a)/n
   s=0.
   for i in range(n-1):
      x  = a+(i+1)*h
      s += f(x)
   s *=2
   s +=f(a)+f(b)
   s *=h*0.5
   return s

def simpson(f,a,b,n):
   h=(b-a)/n
   s=0.
   s = f(a+0.5*h)*2
   for i in range(n-1):
      x  = a+(i+1)*h
      s += f(x) + 2*f(x+0.5*h)
   s *= 2
   s += f(a)+f(b)
   s *= h/6
   return s

def simpsonExtndd(f,a,b,n):
   if n<9 : return 0.
   h=(b-a)/n
   s=0.
   for i in range(n-7):
      x  = a+(i+4)*h
      s += f(x) 
   s *= 48
   s += 17*(f(a)+f(b))
   s += 59*(f(a+h)+f(b-h))
   s += 43*(f(a+2*h)+f(b-2*h))
   s += 49*(f(a+3*h)+f(b-3*h))
   s *= h/48.
   return s


def GLparams():
   pj=[[0],
       [-np.sqrt(1./3),np.sqrt(1./3)],
       [0,-np.sqrt(3./5),np.sqrt(3./5)],
       [-np.sqrt(3./7.-2./7*np.sqrt(6./5.)),np.sqrt(3./7.-2./7*np.sqrt(6./5.)),
        -np.sqrt(3./7.+2./7*np.sqrt(6./5.)),np.sqrt(3./7.+2./7*np.sqrt(6./5.))],
       [0,
        -np.sqrt(5-2*np.sqrt(10./7.))/3.,np.sqrt(5-2*np.sqrt(10./7.))/3.,
        -np.sqrt(5+2*np.sqrt(10./7.))/3.,np.sqrt(5+2*np.sqrt(10./7.))/3.]]
   wj=[[2],
       [1.,1.],
       [8./9.,5./9.,5./9.],
       [(18.+np.sqrt(30.))/36.,(18.+np.sqrt(30.))/36.,
        (18.-np.sqrt(30.))/36.,(18.-np.sqrt(30.))/36.],
       [128./225.,(322+13*np.sqrt(70))/900.,(322+13*np.sqrt(70))/900.,
        (322-13*np.sqrt(70.))/900.,(322-13*np.sqrt(70.))/900.]]
   return pj,wj

def GL(f,a,b,n,m):
   pj,wj=GLparams()
   h=(b-a)/n
   hd=h/2.
   s=0.
   for i in range(n):
      x=a+i*h
      for j in range(m):
         s += wj[m-1][j]*f(x+hd*(1+pj[m-1][j]))
   s *= hd
   return s
       


def GL1(f,a,b,n):
    return GL(f,a,b,n,1)
def GL2(f,a,b,n):
    return GL(f,a,b,n,2)
def GL3(f,a,b,n):
    return GL(f,a,b,n,3)
def GL4(f,a,b,n):
    return GL(f,a,b,n,4)
def GL5(f,a,b,n):
    return GL(f,a,b,n,5)



def testIntegration(integrateur,f,F,a,b,nmin,nmax):
   ln   = []
   lint = []
   n = nmin
   while n < nmax :
      ln.append(n)
      lint.append(abs(integrateur(f,a,b,int(n))-F(b)+F(a)))
      n *= np.sqrt(3.)
   return ln,lint

m=2





ln,lrec = testIntegration(rectangle,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,ltra = testIntegration(trapeze,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,lsim = testIntegration(simpson,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
lnSimEx,lsimex = testIntegration(simpsonExtndd,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),8,20000)

ln,lgl1 = testIntegration(GL1,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,lgl2 = testIntegration(GL2,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,lgl3 = testIntegration(GL3,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,lgl4 = testIntegration(GL4,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)
ln,lgl5 = testIntegration(GL5,np.exp,np.exp,np.sqrt(2.),np.sqrt(7.),2,20000)



plt.loglog(ln,lrec,label="rectangle")
plt.loglog(ln,ltra,label="Trapeze")
lnSim=[n*3 for n in ln]
plt.loglog(lnSim,lsim,label="Simpson")
plt.loglog(lnSimEx,lsimex,label="Simpson extended")
lngl1=[n*1 for n in ln]
plt.loglog(lngl1,lgl1,label="GL1")
lngl2=[n*2 for n in ln]
plt.loglog(lngl2,lgl2,label="GL2")
lngl3=[n*3 for n in ln]
plt.loglog(lngl2,lgl3,label="GL3")
lngl4=[n*4 for n in ln]
plt.loglog(lngl3,lgl4,label="GL4")
lngl5=[n*5 for n in ln]
plt.loglog(lngl5,lgl5,label="GL5")

plt.legend()

plt.show()









