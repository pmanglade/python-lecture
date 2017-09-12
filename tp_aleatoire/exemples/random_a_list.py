#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random



## Ceci est le programme principal
if __name__ == "__main__":

    debug = True


    if debug:
        print("*****************************")
        print("* Welcome in random_a_list  *")
        print("*****************************\n")




        list_of_particles = ['electron', 'muon', 'tau', 'up', 'down', 'charm', 'strange', 'top', 'bottom']


        # shuffle the list
        random.shuffle(list_of_particles)


        answer = input("Would you like select randomly a particle ? (Y or N)\n")

        # choose an element in the list
        random.choice(list_of_particles)
