#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

debug = True

if debug:
    print("************************")
    print("* Welcome in write_file *")
    print("************************\n")


advice = "Do. Or do not. There is no try!"
author = "Yoda"


# Open the file in write mode
my_file = open('quote_file.dat', 'w')


# write string 1
my_file.write("1 ")
# write string contain in advice 
my_file.write(advice)
# write a newline in the text at this point
my_file.write("\n")
# write string contain in author
my_file.write(author)


# Close the file
my_file.close()




