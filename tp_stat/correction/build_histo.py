#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



 
import matplotlib.pyplot as plt

      
my_file = open('data.dat', 'r')

input_min_value = input("Enter the minimal value to build your histogramm : ")
input_max_value = input("Enter the maximal value to build your histogramm : ")
input_nb_bin    = input("Enter the number of bin to your histogramm : ")

int_min     = int(input_min_value)
int_max     = int(input_max_value)
int_nb_bin = int(input_nb_bin)


bin_width   = (int_max-int_min) / int_nb_bin

print("build histo from {} to {} using {} bins".format(int_min,int_max,int_nb_bin))

histo_bins = [0] * int_nb_bin


for a_line in my_file.readlines():
      float_value = float(a_line)
      for i in range(int_nb_bin):
          if float_value > (int_min+i*bin_width) and float_value < (int_min+(i+1)*bin_width):
              histo_bins[i] = histo_bins[i] + 1

      #      print(float_value)

plt.step(range(int_nb_bin),histo_bins)
plt.show()
      
      

