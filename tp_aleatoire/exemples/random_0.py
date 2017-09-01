#!/usr/bin/python3
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random



def bunch_of_random_integer(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.randint(param_min,param_max))

    return tmp_list


def bunch_of_random_real(param_min,param_max,number_of_sample):
    tmp_list = []
    for i in range(number_of_sample):
        tmp_list.append(random.uniform(param_min,param_max))

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
        N          = input("the number value expected ? ")
        min_value  = input("Minimum value from range ? ")
        max_value  = input("Maximum  value from range ? ")
        

        data = bunch_of_random_integer(int(min_value),int(max_value),int(N))

        # Display
        plt.hist(data,20, facecolor='g', alpha=0.75)
        plt.show()
    
        data = []
        data = bunch_of_random_real(int(min_value),int(max_value),int(N))

        # Display
        plt.hist(data,20, facecolor='r', alpha=0.75)
        plt.show()
    

        



