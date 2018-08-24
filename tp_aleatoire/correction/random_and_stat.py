#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import numpy as np
import matplotlib.pyplot as plt
import random



def bunch_of_random_integer(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.randint(param_min,param_max))

    return tmp_list


## Ceci est le programme principal
if __name__ == "__main__":

    debug = True
    

    if debug:
        print("*******************************")
        print("* Welcome in random_and_stat  *")
        print("*******************************\n")

        #random.seed(1)
        random.seed(None)


        
        print("Define the expected random distribution")
        input_N          = input("the number value expected ? ")
        input_min_value  = input("Minimum value from range ? ")
        input_max_value  = input("Maximum  value from range ? ")


        N =int(input_N)
        min_value =int(input_min_value)
        max_value =int(input_max_value)

        expected_mean = (max_value + min_value) / 2
        print("Expected mean value is {}".format(expected_mean))
        
        mean_sample   = N / ((max_value - min_value)+1)
        print("Expected mean sample per value is {}".format(mean_sample))

        
        data      = bunch_of_random_integer(min_value,max_value,N)
        print("Mean value obtained using randint function : {}".format(np.mean(data)))


        diff_mean = np.mean(data) - mean_sample

        print("Expected mean - Obtained mean  : {}".format(diff_mean))

        
        
        
     
