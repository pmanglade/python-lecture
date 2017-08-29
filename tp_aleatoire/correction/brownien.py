#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random
import math
import numpy as np


def distance(x1,y1,x2,y2):
    dx = (x2-x1)
    dy = (y2-y1)
    tmp_distance = math.sqrt(dx*dx+dy*dy)
    return tmp_distance
    
def move(x,y,delta_x,delta_y):

    next_x  = 0
    next_y  = 0
    
    next_x = x + delta_x
    next_y = y + delta_y

    return next_x,next_y

def choose_direction():

    tmp_value = None
    list_of_direction = ['W','S','E','N']
    tmp_value = random.choice(list_of_direction)
    return tmp_value

def prepare_mouvement(a_direction):

    if a_direction == 'N':
        delta_x = 0
        delta_y = +1
    elif a_direction == 'S':
        delta_x = 0
        delta_y = -1
    elif a_direction == 'E':
        delta_x = 1
        delta_y = 0
    elif a_direction == 'W':
        delta_x = -1
        delta_y = 0
    else:
        delta_x = 0
        delta_y = 0

    return delta_x,delta_y
    

def simulate(tmp_x, tmp_y,tmp_it):

    current_x = tmp_x
    current_y = tmp_y
    a_x = []
    a_y = []
    
    for it in range(tmp_it):
        the_direction        = choose_direction()
        dx,dy                = prepare_mouvement(the_direction)
        current_x,current_y  = move(current_x,current_y,dx,dy)
        a_x.append(current_x)
        a_y.append(current_y)

    return a_x,a_y

        

if __name__ == "__main__":

    debug = False
    

    if debug:
        print("************************")
        print("* Welcome in brownien  *")
        print("************************\n")

    random.seed(None)
    x_init = 0
    y_init = 0

    current_x = x_init
    current_y = y_init

    
    nb_of_iteration = 2000
    
    final_distance   = []
    nb_simulation    = 1000



    for it in range(nb_simulation):
        x                = []
        y                = []

        x,y = simulate(x_init,y_init,nb_of_iteration)
        final_distance.append(distance(x_init,y_init,x[-1],y[-1]))

        
        if debug :
            print("Distance from initial position is : {}".format(final_distance[-1]))
            plt.grid()
            plt.scatter(x,y,c= range(len(x)), marker = '.', s=200,zorder=1)
            plt.show()

        
    print("mean distance for {} iterations after {} simulations : {}".format(nb_of_iteration,nb_simulation,np.mean(final_distance)))


    plt.hist(final_distance)
    plt.show()
