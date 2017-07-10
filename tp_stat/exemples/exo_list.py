#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

debug = True

if debug:
    print("*************************")
    print("* Welcome in boucle_for *")
    print("*************************\n")


my_list_of_heros = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']

print(my_list_of_heros)

#Un heros est ajouter à la fin de la list
my_list_of_heros.append("Hulk")
print(my_list_of_heros)

#Le heros 'Wonder Woman' sera supprimé de la list
my_list_of_heros.remove("Wonder Woman")

#Le heros à la première position sera supprimé de la list
del my_list_of_heros[0]

print(my_list_of_heros)


for heros in my_list_of_heros:
    print ("my current heros is %s" % heros)

    
print("Finished...")
        
           
