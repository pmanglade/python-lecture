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


## Ceci est le programme principal
if __name__ == "__main__":

    debug = True
    

    if debug:
        print("************************")
        print("* Welcome in random_0  *")
        print("************************\n")

        #random.seed(1)
        random.seed(None)


        
        print("Define the expected random distribution")
        input_N          = input("the number of values expected ? ")
        input_min_value  = input("Minimum value (a) ? ")
        input_max_value  = input("Maximum value (b) ? ")


        N =int(input_N)
        min_value =int(input_min_value)
        max_value =int(input_max_value)
                        
        
        data      = bunch_of_random_integer(int(min_value),int(max_value),int(N))
        tmp_value = 0
        
        for element in data:
            tmp_value = tmp_value + element

            
        # Display
        plt.hist(data,N, facecolor='g')
        plt.show()
    
        
