#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt


debug = True


if debug:
    print("************************")
    print("* Welcome in random_0  *")
    print("************************\n")



data = [0,7,2,5,1,3,5,6,3,4,1,8,9,1,4,2,6,3,8,4,5,3,]
plt.hist(data,normed=1)
plt.show()
