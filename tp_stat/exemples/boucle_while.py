#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("***************************")
print("* Welcome in boucle_while *")
print("***************************\n")


N = None
iterator = 0

while N != "42":
    N = input("Enter the answer to life, the universe and everything")
    iterator=iterator+1


print("You tried %d times"%iterator)



