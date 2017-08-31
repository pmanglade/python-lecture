#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017
 

def main():

    print("*********************")
    print("* Welcome in chaine *")
    print("*********************\n")

    begin_sentence  = "On peut tromper une personne mille fois. "
    middle_sentence = "On peut tromper mille personnes une fois. "
    end_sentence    = "Mais on ne peut pas tromper mille personnes, mille fois."

    print(begin_sentence)
    

    up_sentence = begin_sentence.upper()
    print(up_sentence)
    
    sentence = begin_sentence + middle_sentence + end_sentence

    new_sentence = sentence.replace("personne","buse")
    print(new_sentence)

    
    list_of_word = sentence.split()
    print(list_of_word)
    
    tmp_word = "mille"
    print("\nThere's %d times the word '%s' \n"%(sentence.count(tmp_word),tmp_word))
    # Ancienne methode d'affichage
    
    tmp_sentence = "There's {} times the word {!r}"
    print(tmp_sentence.format(sentence.count(tmp_word),tmp_word))
    # Methode moderne d'affichage


    
    tmp_word = "fois"
    if tmp_word in new_sentence:
        print("\nI found the word {!r}".format(tmp_word))
    else:
        print("\nThe word {!r} is missing".format(tmp_word))
        
    return



main()
