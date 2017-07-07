#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("************************")
print("* Welcome in write_file *")
print("************************\n")


advice = "Do. Or do not. There is no try!"
author = "Yoda"


my_file = open('quote_file.dat', 'w')
# Open the file

my_file.write("1 ")
my_file.write(advice)
my_file.write("\n")
my_file.write(author)
# write the file

my_file.close()
#Close the file


