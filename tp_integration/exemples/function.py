#!/usr/bin/env python
import numpy as np
# Example of a function (f2) using an other function as argument
def f2(f,x):
   return f(x)+f(x+np.pi)



# Example of f2 usage whith the function sin from numpy package
print("x=1 ","f2=",f2(np.sin,1.))
print("x=2 ","f2=",f2(np.sin,2.))
print("x=3 ","f2=",f2(np.sin,3.))
