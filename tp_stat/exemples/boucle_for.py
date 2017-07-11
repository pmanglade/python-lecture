#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

def main():
    
    debug = True
    
    if debug:
        print("*************************")
        print("* Welcome in boucle_for *")
        print("*************************\n")
        
        #Ceci est une liste de chaine de caractère
        my_list_of_character = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']
        print(my_list_of_character)
        
        
        #La variable 'heros' prendra tour à tour chaque valeur de la liste my_list_of_heros
        iterator = 0
        for heros in my_list_of_character:
            print (iterator)
            print ("my current heros is %s" % heros)
            iterator = iterator + 1
            
            
            
        print("Finished with %d heros "%iterator)
        print("Finished with %d heros "%len(my_list_of_character))
            
        
        #Cette boucle ne commence qu'à partir du second element de la list
        iterator = 0
        for heros in my_list_of_character[2:]:
            print (iterator)
            print ("my current heros is %s" % heros)
            iterator = iterator + 1
            
        print("Finished with %d heros "%iterator)
        print("Finished with %d heros "%len(my_list_of_character))
    
        return


main()

