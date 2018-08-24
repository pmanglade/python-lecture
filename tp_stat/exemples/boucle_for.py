#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

def main():

    debug = True

    if debug:
        print("*************************")
        print("* Welcome in boucle_for *")
        print("*************************\n")

        # Ceci est une liste de chaines de caractères:
        my_list_of_heroes = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']
        print(my_list_of_heroes)


        # La variable 'hero' prendra tour à tour chaque valeur de la liste my_list_of_heroes:
        iterator = 0
        for hero in my_list_of_heroes:
            print (iterator)
            print ("my current hero is {}".format(hero))
            iterator = iterator + 1



        print("Finished with {} heroes ".format(iterator))
        print("Finished with {} heroes ".format(len(my_list_of_heroes)))


        # Cette boucle ne commence qu'à partir du second élément de la liste:
        iterator = 0
        for hero in my_list_of_heroes[2:]:
            print (iterator)
            print ("my current hero is {}".format(hero))
            iterator = iterator + 1

        print("Finished with {} heroes ".format(iterator))
        print("Finished with {} heroes ".format(len(my_list_of_heroes)))

        return


main()
