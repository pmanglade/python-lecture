#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017
 

def main():

    print("*******************")
    print("* Welcome in chaine *")
    print("*********************\n")

    sentence="On peut tromper une personne mille fois. On peut tromper mille personne une fois. Mais on ne peut pas tromper mille personnes, mille fois"

    up_sentence = sentence.upper()

    print(sentence)
    print(up_sentence)

    list_of_word = sentence.split()
    
    print(list_of_word)

    print(sentence.count("mille"))
    
    print(sentence.replace("personne","buse"))


    return



main()
