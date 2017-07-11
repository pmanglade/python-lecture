#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

 

print("***************************")
print("* Welcome in plus_moins   *")
print("***************************\n")


mystery_value = 666
proposed_value= 0


while proposed_value != mystery_value:
     
    proposed_value = input("Enter a number between 0 and 1000 :")
    proposed_value = int(proposed_value)
    
    
    if proposed_value < mystery_value:
        print("Too small !\n")
 
    elif proposed_value > mystery_value:
        print("Too large !\n")
        
    else:
        print("You've got it !!!\n")


print("Done")
