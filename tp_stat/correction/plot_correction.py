#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017


import matplotlib.pyplot as plt
import numpy as np

debug = True

if debug:
    print("*******************")
    print("* Welcome in plot *")
    print("*******************\n")


x = range(10)
y = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y2,'o-',color="green")
plt.plot(x,y,'o-',color="red")

plt.xlabel('abscisse')
plt.ylabel('ordonnée')
plt.title('Un joli titre')
plt.axis([0, 12, -3, 3])
plt.grid(True)


plt.show()
