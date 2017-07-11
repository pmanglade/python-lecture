#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("***************************")
print("* Welcome in boucle_for_2 *")
print("***************************\n")


N = input("Enter a positive integer : ")

fact = 1

for i in range(int(N)):
    print (i)
    fact = fact*(int(i+1))

print ("%d! = %s"%(int(N),fact))    
print ("Done")
