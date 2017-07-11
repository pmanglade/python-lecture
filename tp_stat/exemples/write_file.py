#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017


def main():
    
    debug = True
    
    if debug:
        print("************************")
        print("* Welcome in write_file *")
        print("************************\n")
        
        
    advice = "Do. Or do not. There is no try!"
    author = "Yoda"


    
    my_file = open('quote_file.dat', 'w')       # Open the file in write mode

    my_file.write("1 ")                         # write string 1
    my_file.write(advice)                       # write string contain in advice 
    my_file.write("\n")                         # write a newline in the text at this point
    my_file.write(author)                       # write string contain in author


    my_file.close()                             # Close the file


    return

main()

