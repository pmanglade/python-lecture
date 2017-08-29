#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random
import math
import numpy as np

def distance(x1,y1,x2,y2):
    distance = 0
    dx = (x2-x1)
    dy = (y2-y1)
    distance = math.sqrt(dx*dx + dy*dy)

    return distance


def move(x1,y1):

    next_x  = 0
    next_y  = 0
    
    delta_x = random.randint(-1,1)
    delta_y = random.randint(-1,1)

    # print(delta_x)
    # print(delta_y)
    
    next_x = x1 + delta_x
    next_y = y1 + delta_y

    return next_x,next_y
    

if __name__ == "__main__":

    debug = True
    

    if debug:
        print("***************************")
        print("* Welcome in monte_carlo  *")
        print("***************************\n")
        
        

    for it in range(10):

        x_end = random.randint(-5,5)
        y_end = random.randint(-5,5)
        
        x_init = random.randint(-5,5)
        y_init = random.randint(-5,5)
        
        current_distance = distance(x_end,y_end,x_init,y_init)
        
        tmp_distance = current_distance
        
        
        print("init position is  : {},{}".format(x_init,y_init))
        print("final position is : {},{}".format(x_end,y_end))
        print("Distance betwwen localisation is : {}".format(distance(x_end,y_end,x_init,y_init)))
        
        x = []
        y = []
        x.append(x_init)
        y.append(y_init)
        
        x_current = x[-1]
        y_current = y[-1]
        nb_step   = 0
        
        
        while tmp_distance != 0: 
            print("current position is  : {},{}".format(x_current,y_current))
            tmp_x = 0
            tmp_y = 0
        
            
            #while tmp_x > 6 or tmp_x < -6 or tmp_y > 6 or tmp_y < -6:
            tmp_x,tmp_y = move(x_current,y_current)
            if tmp_x > 6 or tmp_x < -6:
                tmp_x = x_current
            if tmp_y > 6 or tmp_y < -6:
                tmp_y = y_current
            
            tmp_distance = distance(tmp_x,tmp_y,x_end,y_end)
            
            #if tmp_distance < current_distance:
            nb_step += 1
            x.append(tmp_x)
            y.append(tmp_y)
            x_current = x[-1]
            y_current = y[-1]
            current_distance = tmp_distance
            
            


        print("Nb of step is {}".format(nb_step))
        fig, ax = plt.subplots()
        ax.set_xticks(range(-10,10))
        ax.set_yticks(range(-10,10))
        
        plt.grid()
        plt.axis([-10,10,-10,10])
        plt.plot(x,y,'.-',zorder=2)
        plt.scatter(x,y,c= range(len(x)), marker = '.', s=200,zorder=1)
    plt.show()
    
