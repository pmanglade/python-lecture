#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def at2 (x) : 
   return x - x**3/3.

def at3 (x) :
   return x - x**3/3. + x**5/5.
def at4 (x) :
   return x - x**3/3. + x**5/5. -x**7/7.
def at5(x) :
   return x - x**3/3. + x**5/5. -x**7/7. +x**9/9.
def atn(x,n):
   p=x
   s=p
   k=int((n-1)/2)
   for i in range(k):
      p *= -1*x*x
      s += p/(2*(i+1)+1)
      #print("(n-1)/2-1,i,p,s ", int((n-1)/2)-1,i,p,s)
   return s

def transf(x):
   return x/(1+np.sqrt(1+x*x))

def atn4(x,n):
   X=transf(transf(x))
   return 4*atn(X,n)

def atn4i(x,n):
   if(abs(x) < 1):
      return atn4(x,n)
   else:
      return abs(x)*np.pi/(2*x)-atn4(1./x,n)

# PLOT arctan along with its order 3 to 7 DL
x = np.arange(-1.1,1.1,0.05);
y1 = [at2(v) for v in x]
y2 = [at3(v) for v in x]
y3 = [at4(v) for v in x]
y4 = [at5(v) for v in x]
y5 = [np.arctan(v) for v in x]
plt.plot(x,y1,label="at3")
plt.plot(x,y2,label="at5")
plt.plot(x,y3,label="at7")
plt.plot(x,y4,label="at9")
plt.plot(x,y5,label="arctan")
plt.legend()
plt.show()


# PLOT error of order 3 to 7 DL of arctan
y1 = [abs(at2(v)-np.arctan(v)) for v in x]
y2 = [abs(at3(v)-np.arctan(v)) for v in x]
y3 = [abs(at4(v)-np.arctan(v)) for v in x]
y4 = [abs(at5(v)-np.arctan(v)) for v in x]
plt.plot(x,y1,label="Eat3")
plt.plot(x,y2,label="Eat5")
plt.plot(x,y3,label="Eat7")
plt.plot(x,y4,label="Eat9")

plt.legend()
plt.show()

# PLOT arctan argument reduction formulae
y1 = [v/(1+np.sqrt(1+v*v)) for v in np.arange(-2,2,0.1)]
y2 = [v/2. for v   in np.arange(-2,2,0.1)]

plt.plot(np.arange(-2,2,0.1),y1,label="transf x")
plt.plot(np.arange(-2,2,0.1),y2,label=" x")
plt.show()

# PLOT error of order n DL of arctan
# PLOT error of order 3 to 7 DL of arctan
y1 = [abs(at2(v)-np.arctan(v)) for v in x]
y2 = [abs(atn(v,3)-np.arctan(v)) for v in x]
y3 = [abs(at4(v)-np.arctan(v)) for v in x]
y4 = [abs(atn(v,7)-np.arctan(v)) for v in x]
y5 = [abs(atn(v,15)-np.arctan(v)) for v in x]
y6 = [abs(atn4(v,7)-np.arctan(v)) for v in x]
plt.plot(x,y1,'--',label="Eat3")
plt.plot(x,y2,label="Eatn3")
plt.plot(x,y3,'--',label="Eat7")
plt.plot(x,y4,label="Eatn7")
plt.plot(x,y5,label="Eatn15")
plt.plot(x,y6,label="Eatn4-7")
plt.legend()
plt.show()

# PLOT Transformed DL results on [-7,7]
x = np.arange(-7.1,7.1,0.05);
y6 = [abs(atn4(v,15)-np.arctan(v)) for v in x]
plt.plot(x,y6,label="Eatn4-15")
y5 = [abs(atn4i(v,15)-np.arctan(v)) for v in x]
plt.plot(x,y5,label="Eatn4i-9")

plt.legend()
plt.show()




