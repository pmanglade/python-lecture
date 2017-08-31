#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

def main():
    
    debug = True
    
    if debug:
        print("*************************")
        print("* Welcome in boucle_for *")
        print("*************************\n")
        
        #Ceci est une liste de chaines de caractères
        my_list_of_characters = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']
        print(my_list_of_characters)
        
        
        #La variable 'hero' prendra tour à tour chaque valeur de la liste my_list_of_characters
        iterator = 0
        for hero in my_list_of_characters:
            print (iterator)
            print ("my current hero is {}".format(hero))
            iterator = iterator + 1
            
            
            
        print("Finished with {} heroes ".format(iterator))
        print("Finished with {} heroes ".format(len(my_list_of_characters)))
            
        
        #Cette boucle ne commence qu'à partir du second élément de la list
        iterator = 0
        for hero in my_list_of_characters[2:]:
            print (iterator)
            print ("my current hero is {}".format(hero))
            iterator = iterator + 1
            
        print("Finished with {} heroes ".format(iterator))
        print("Finished with {} heroes ".format(len(my_list_of_characters)))
    
        return


main()

