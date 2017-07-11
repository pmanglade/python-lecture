#!/usr/bin/python3.5
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
    
    # Tant que l'utilisateur ne rentre pas la valeur '42', le question sera posée de nouveau
    while N != "42":
        N = input("Enter the answer to life, the universe and everything")
        iterator=iterator+1
        
        
    print("You tried %d times"%iterator)

