#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017



def main():

    debug = True
    
    if debug:
        print("************************")
        print("* Welcome in read_file *")
        print("************************\n")
        
        
        # First method to open the file (read all)
        my_file = open('quote_file.dat', 'r')
        
        text = my_file.read()
        my_file.close()
        
        print ("First method : \n")
        print (text)
        print ("----------------\n")
        
        # Second method to open the file (read line per line)
        my_file = open('quote_file.dat', 'r')
        
        first_line = my_file.readline()
        second_line = my_file.readline()
        my_file.close()
        
        print ("Second method : \n")
        print (first_line)
        print (second_line)
        print ("----------------\n")
        
        
        # Third method to open the file (read  all lines)
        my_file = open('quote_file.dat', 'r')
        
        lines = my_file.readlines()
        print(lines)
        my_file.close()
        
        print ("Third method : \n")
        print (lines[0])
        print (lines[1])
        print ("----------------\n")
        return


main()
