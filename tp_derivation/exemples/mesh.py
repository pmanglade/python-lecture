#!/usr/bin/env python
import numpy as np

# ways to explore a regular mesh on [a,b]
n=6
a=1. ### WARNING if neither a nor b is a float, it won't work !!!!!
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


print("\nThird method: using numpy arange function")
epsilon=0.01
for x in np.arange(a, b+epsilon, (b-a)/(n-1)):
   print(x)


print("\nFourth method: using numpy arange function to create a new list")
epsilon=0.01
X=np.arange(a, b+epsilon, (b-a)/(n-1))[:] ### WARNING using X=np.arange(...) without [:] would be a bad idea
print(X)

print("\nFifth method : generating a list with an inner loop")
X = [((b-a)*i) / (n-1) + a for i in range(n)]
print(X)
### Many other combinations of the previous examples exist
