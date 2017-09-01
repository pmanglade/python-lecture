#!/usr/bin/python3
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random
import time 


def bunch_of_random_real(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.uniform(param_min,param_max))

    return tmp_list




def bunch_of_triangular_random(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.triangular(param_min,param_max))

    return tmp_list




def bunch_of_gauss_random(param_mu,param_sigma,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.gauss(param_mu,param_sigma))

    return tmp_list




## Ceci est le programme principal
if __name__ == "__main__":

    debug = True
    

    if debug:
        print("************************")
        print("* Welcome in random_0  *")
        print("************************\n")

        random.seed(1)

        print("Define the expected random distribution")
        input_N          = input("the number value expected ? ")
        input_min_value  = input("Minimum value from range ? ")
        input_max_value  = input("Maximum  value from range ? ")

        N =int(input_N)
        min_value =int(input_min_value)
        max_value =int(input_max_value)

        number_of_bar = (max_value-min_value)


        
        ### Distribution #1
        tps1 = time.clock()
        data      = bunch_of_random_real(min_value,max_value,N)
        tps2 = time.clock()
        dt = tps2 - tps1
        print("Time to generate {} value is : {} second".format(N,dt))
        plt.hist(data,number_of_bar, facecolor='g')
        plt.show()

        ### Distribution #2
        data = []
        tps1 = time.clock()
        data = bunch_of_triangular_random(min_value,max_value,N)
        tps2 = time.clock()
        dt = tps2 - tps1
        print("Time to generate {} value is : {} second".format(N,dt))
        plt.hist(data,number_of_bar, facecolor='b')
        plt.show()




        ### Distribution #3
        input_mean_value  = input("Mean position of gauss distribution ? ")
        input_sigma_value  = input("Width of gauss distribution ? ")
        data = []
        tps1 = time.clock()

        data = bunch_of_gauss_random(int(input_mean_value),int(input_sigma_value),N)
        tps2 = time.clock()
        dt = tps2 - tps1
        print("Time to generate {} value is : {} second".format(N,dt))
        plt.hist(data,50, facecolor='r')
        plt.show()
        
