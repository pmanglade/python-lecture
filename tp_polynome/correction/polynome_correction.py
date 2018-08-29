#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

from numpy import *
#import numpy as np

def main():

    print("*************************")
    print("* Welcome in polynome   *")
    print("*************************\n")
    
    debug = True
    

    print("Compute the root(s) x of the a*x^2+b*x+c=0 equation")

    input_param_a = input("Please, give me a value for a : ")
    input_param_b = input("Please, give me a value for b : ")
    input_param_c = input("Please, give me a value for c : ")

    a = float(input_param_a)
    b = float(input_param_b)
    c = float(input_param_c)
    
    if debug == True:
        print ("param a  is    : %d" % a)
        print ("param b  is    : %d" % b)
        print ("param c  is    : %d" % c)


    delta = (b*b)-4*(a*c)
    
    if delta > 0:
        print("Two real roots")
        x1= (-b-sqrt(delta))/(2*a)
        x2= (-b+sqrt(delta))/(2*a)
        print("x1 = %f"%x1)
        print("x2 = %f"%x2)
        
    elif delta == 0:
        print("Only one real root")
        x1= (-b)/(2*a)
        print("x1 = %f"%x1)
    
        
    elif delta < 0:
        print("Two complex roots")
        
        

    
        
    return 
    
    
main()
