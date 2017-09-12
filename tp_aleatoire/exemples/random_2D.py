#!/usr/bin/python3
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random



def bunch_of_random_real(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.uniform(param_min,param_max))

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
        input_N          = input("Number of values to generate ? ")
        input_min_value  = input("Minimum value from range ? ")
        input_max_value  = input("Maximum  value from range ? ")


        N =int(input_N)
        min_value =int(input_min_value)
        max_value =int(input_max_value)
                        
        x      = bunch_of_random_real(int(min_value),int(max_value),int(N))
        y      = bunch_of_random_real(int(min_value),int(max_value),int(N))

        number_of_bar = (max_value-min_value)
        # Display
        plt.plot(x,y,'*')
        plt.show()



        plt.hist2d(x,y,bins=40)
        plt.colorbar()
        plt.show()


        input_mean_value  = input("Mean position of gauss distribution ? ")
        input_sigma_value  = input("Width of gauss distribution ? ")

        g_x = bunch_of_gauss_random(int(input_mean_value),int(input_sigma_value),int(N))
        g_y = bunch_of_gauss_random(int(input_mean_value),int(input_sigma_value),int(N))

        plt.plot(g_x,g_y,'*')
        plt.show()

        
        plt.hist2d(g_x,g_y,bins=40)
        plt.colorbar()
        plt.show()



        
