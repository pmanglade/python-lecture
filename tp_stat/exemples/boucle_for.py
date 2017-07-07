#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("*************************")
print("* Welcome in boucle_for *")
print("*************************\n")


my_list_of_heros = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']

print(my_list_of_heros)

iterator = 0
for heros in my_list_of_heros:
    print (iterator)
    print ("my current heros is %s" % heros)
    iterator = iterator + 1
    
print("Finished with %d heros "%iterator)
print("Finished with %d heros "%len(my_list_of_heros))


iterator = 0
for heros in my_list_of_heros[2:]:
    print (iterator)
    print ("my current heros is %s" % heros)
    iterator = iterator + 1

print("Finished with %d heros "%iterator)
print("Finished with %d heros "%len(my_list_of_heros))
    


