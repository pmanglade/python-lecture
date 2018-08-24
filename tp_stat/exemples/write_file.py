#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017


def main():

    debug = True

    if debug:
        print("*************************")
        print("* Welcome in write_file *")
        print("*************************\n")


    advice = "Do. Or do not. There is no try!"
    author = "Yoda"


    my_file = open('quote_file.dat', 'w')       # Open the file in write mode

    my_file.write("1 ")                         # write in file a string
    my_file.write(advice)                       # write string containing an advice
    my_file.write("\n")                         # write a newline in the text at the current point
    my_file.write(author)                       # write string containing the author's name


    my_file.close()                             # Close the file


    return

main()
