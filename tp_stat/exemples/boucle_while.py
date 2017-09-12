#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017

def main():


    debug = True
    if debug:
        print("***************************")
        print("* Welcome in boucle_while *")
        print("***************************\n")


    N = None
    iterator = 0

    # Tant que l'utilisateur ne rentre pas la valeur textuelle '42', le question sera posée de nouveau
    while N != "42":
        N = input("Enter the answer to Life, the Universe and Everything: ")
        iterator=iterator+1


    print("You tried {} times.".format(iterator))

main()
