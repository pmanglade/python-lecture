#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def l1():
   liste = []
   for n in range(4):
      liste.append(n)
   return liste

def l2():
   liste1 = [v*0.1 for v in range(5)]
   liste2 = [v*7 for v in range(3)]
   return liste1, liste2


l=l1()
m,n=l2()
print(l,m,n)


