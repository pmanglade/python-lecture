#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

from numpy import *
#import numpy as np



print("***************************")
print("* Welcome in scientifique *")
print("***************************\n")

my_affichage = True

my_value      = -1024
my_abs_value  = fabs(my_value)
my_sqrt_value = sqrt(my_abs_value)

if my_affichage == True:
    print ("[debug] My initial value  is    : {}".format(my_value))
    print ("[debug] My square root value is : {}".format(my_sqrt_value))
