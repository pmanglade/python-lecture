#!/usr/bin/env python3
import numpy as np
# various ways to create and go through a regular mesh on [a,b]
n=6
a=1.
b=3.
print("First method: simple loop")
for i in range(n):
   x = ((b-a)*i) / (n-1) + a
   print(i, x);
print("\nSecond method: loop creating a list")
X=[]
for i in range(n):
   X.append(((b-a)*i) / (n-1) + a)
print(X)
print("\nThird method : generating a list with an inner loop")
X = [((b-a)*i) / (n-1) + a for i in range(n)]
print(X)
# Methods out of the scope of those lectures : using numpy ndarray
print("Fourth method: using numpy linspace function")
X = np.linspace(a,b,n)
print(X)
print("\nFifth method: using numpy arange function")
epsilon=0.01
for x in np.arange(a, b+epsilon, (b-a)/(n-1)):
   print(x)
print("\nsixth method: using numpy arange function to create a new list")
epsilon=0.01
X=np.arange(a, b+epsilon, (b-a)/(n-1))[:]
print(X)


