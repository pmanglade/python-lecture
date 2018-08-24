#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017


def main():
    debug = True

    if debug:
        print("***********************")
        print("* Welcome in exo_list *")
        print("***********************\n")


        my_list_of_heroes = ['Spider-Man','Daredevil','Iron Man','Flash','Wonder Woman']

        print(my_list_of_heroes)

        # Un héros est ajouté à la fin de la "list"
        my_list_of_heroes.append("Hulk")
        print(my_list_of_heroes)

        # Le héros 'Wonder Woman' sera supprimé de la "list"
        my_list_of_heroes.remove("Wonder Woman")

        # Le héros à la première position sera supprimé de la "list"
        del my_list_of_heroes[0]

        print(my_list_of_heroes)


        for hero in my_list_of_heroes:
            print ("my current hero is {}".format(hero))



        my_second_list_of_heroes = ["À Dèle Blanc-Sec","Ma Ya l'abeille","Yaka Rit Jaune"]
        my_list_of_heroes.extend(my_second_list_of_heroes)
        print("Finished...")
        return


main()
