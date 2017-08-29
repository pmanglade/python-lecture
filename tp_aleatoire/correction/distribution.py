#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random
import math

def bunch_of_random_real(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.uniform(param_min,param_max))

    return tmp_list

## Ceci est le programme principal
if __name__ == "__main__":

    debug = True
    

    if debug:
        print("****************************")
        print("* Welcome in distribution  *")
        print("****************************\n")

        #random.seed(1)
    random.seed(None)
    
    print("Define the expected random distribution")
    input_N          = input("the number value expected ? ")
    input_min_value  = input("Minimum value from range ? ")
    input_max_value  = input("Maximum  value from range ? ")
    
    
    N =int(input_N)
    min_value =int(input_min_value)
    max_value =int(input_max_value)
    
    x      = bunch_of_random_real(min_value,max_value,N)
    y      = bunch_of_random_real(min_value,max_value,N)
    
    save_x = []
    save_y = []
    for el in range(N):
        r = math.sqrt(x[el]*x[el]+y[el]*y[el])
        if r < 1:
            save_x.append(x[el])
            save_y.append(y[el])
            
            
            
    plt.axes().set_aspect('equal', 'datalim')
    plt.plot(x, y, '.')
            
    plt.plot(save_x, save_y, '*')
    plt.show()


    print("Total number of value    : {}".format(N))
    print("Selected number of value : {}".format(len(save_x)))
    print("ration Nsel/Ntot         : {}".format(len(save_x)/N))
    print("pi/4                     : {}".format(math.pi/4))
    
    deviation = (math.pi/4 - len(save_x)/N) / (math.pi/4)
        
    print("relative deviation       : {}".format(deviation))
        
