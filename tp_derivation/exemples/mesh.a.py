#!/usr/bin/env python
import numpy as np

# ways to explore a regular mesh on [a,b]
n=6
a=1. ### WARNING if neither a nor b is a float, it won't work !!!!!
b=3.
h = (b-a)/(n-1) # if a, b, and n were integer h would be an integer also
print("First method: simple loop")
for i in range(n):
   x = h*i + a
   print(i, x);


print("\nSecond method: loop creating a list")
X=[]                # Create an empty list called X.
for i in range(n):
   xi = h*i + a     # Compute a value for xi.
   X.append(xi)     # Append the value of xi at the end of the list X.
print(X)


print("\nThird method: using numpy arange list")
epsilon=0.01
for x in np.arange(a, b+epsilon, (b-a)/(n-1)):
   print(x)


print("\nFourth method: using numpy arange list to create a new list")
epsilon=0.01
X=np.arange(a, b+epsilon, (b-a)/(n-1))[:] ### WARNING using X=np.arange(...) without [:] would be a bad idea 
                                          ### X would appear similar but be a different kind of object. 
                                          ### With the [:] X is a list
print(X)

print("\nFifth method : generating a list with an inner loop")
X = [ (h*i+a) for i in range(n)]
print(X)
### Many other combinations of the previous examples exists
