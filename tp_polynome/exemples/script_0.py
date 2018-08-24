#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017
# Ceci est un commentaire inutile

print("*********************************")
print("* Welcome in this Python script *")
print("*********************************\n")


print("The script's name is: {} \n" .format( __file__))


a = 42
b = 3.14
c = "It is a mistake to think you can solve any major problems just with potatoes."
d = True

print (a)
print (b)
print (c)
print (d)
print ("\n\n")

print ("Value a is equal to: {:f}".format(a))
print ("Value b is equal to: {:d}".format(d))  # Pour afficher un nombre reel, utilisez {:f}
print ("Sentence from The Hitchhiker's Guide to the Galaxy : \n {:s}".format(c))



# Note
# :d for decimal
# :f for float
# :s for string
