#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017


import matplotlib.pyplot as plt


debug = True

if debug:
    print("*******************")
    print("* Welcome in plot *")
    print("*******************\n")


x = [1,2,3,4,5,6,7,8,9,10]
y = [1.81,1.64,1.48,1.34,1.21,1.10,0.99,0.90,0.81,0.74]


plt.plot(x,y,'o')

plt.xlabel('abscisse')
plt.ylabel('ordonnée')
plt.title('Un joli titre')
plt.axis([0, 12, 0, 2])
plt.grid(True)


plt.show()
