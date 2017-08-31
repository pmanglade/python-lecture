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
        
        
        my_list_of_characters = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']
        
        print(my_list_of_characters)
        
        #Un héros est ajouté à la fin de la "list"
        my_list_of_characters.append("Hulk")
        print(my_list_of_characters)
        
        #Le héros 'Wonder Woman' sera supprimé de la "list"
        my_list_of_characters.remove("Wonder Woman")
        
        #Le héros à la première position sera supprimé de la "list"
        del my_list_of_characters[0]
        
        print(my_list_of_characters)
        
        
        for hero in my_list_of_characters:
            print ("my current hero is {}".format(hero))



        my_second_list_of_characters = ["À Dèle Blanc-Sec","Ma Ya l'abeille","Yaka Rit Jaune"]
        my_list_of_characters.extend(my_second_list_of_characters)
        print("Finished...")
        return


main()
           
