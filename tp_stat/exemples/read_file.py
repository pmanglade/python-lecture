#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("************************")
print("* Welcome in read_file *")
print("************************\n")


#first method 
my_file = open('quote_file.dat', 'r')
# Open the file in read mode

text = my_file.read()

my_file.close()
#Close the file


print ("First method : \n")
print (text)
print ("\n")

#second method 
my_file = open('quote_file.dat', 'r')
# Open the file in read mode

first_line = my_file.readline()
second_line = my_file.readline()

my_file.close()
#Close the file


print ("Second method : \n")
print (first_line)
print (second_line)
print ("\n")



#third method 
my_file = open('quote_file.dat', 'r')
# Open the file in read mode

lines = my_file.readlines()

my_file.close()
#Close the file


print ("Third method : \n")
print (lines)
print ("\n")

print (lines[0])
print (lines[1])

