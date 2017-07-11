#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

debug = True

if debug:
    print("************************")
    print("* Welcome in read_file *")
    print("************************\n")
    

# First method 
# Open the file in read mode
my_file = open('quote_file.dat', 'r')

text = my_file.read()

# Close the file
my_file.close()

print ("First method : \n")
print (text)
print ("\n")

# Second method 
# Open the file in read mode
my_file = open('quote_file.dat', 'r')

first_line = my_file.readline()
second_line = my_file.readline()

#Close the file
my_file.close()


print ("Second method : \n")
print (first_line)
print (second_line)
print ("\n")



# third method 
# Open the file in read mode
my_file = open('quote_file.dat', 'r')

lines = my_file.readlines()

#Close the file
my_file.close()


print ("Third method : \n")
print (lines)
print ("\n")

print (lines[0])
print (lines[1])

