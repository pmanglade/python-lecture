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
        
        
        my_list_of_character = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']
        
        print(my_list_of_character)
        
        #Un heros est ajouter à la fin de la list
        my_list_of_character.append("Hulk")
        print(my_list_of_character)
        
        #Le heros 'Wonder Woman' sera supprimé de la list
        my_list_of_character.remove("Wonder Woman")
        
        #Le heros à la première position sera supprimé de la list
        del my_list_of_character[0]
        
        print(my_list_of_character)
        
        
        for heros in my_list_of_character:
            print ("my current heros is %s" % heros)



        my_second_list_of_character = ["Adèle Blanc-Sec","Maya l'abeille","Yakari"]
        my_list_of_character.extend(my_second_list_of_character)
        print("Finished...")
        return


main()
           
