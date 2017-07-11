#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

from math import *
#import math as my_mathematics
#import matplotlib.pyplot as plt
#from time import *


def main():
    print("***************************")
    print("* Welcome in scientifique *")
    print("***************************\n")
    
    debug = True

    my_value      = -1024
    my_abs_value  = fabs(my_value)
    my_sqrt_value = sqrt(my_abs_value)
    
    
    
    if debug == True:
        print ("My initial value  is    : %d" % my_value)
        print ("My square root value is : %d" % my_sqrt_value)

    return


main()
