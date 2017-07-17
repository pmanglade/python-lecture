#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017



print("***************************")
print("* Welcome in boucle_for_3 *")
print("***************************\n")


N      = input("Enter a positive integer : ")
parity = input("Would you like calculate even or odd values ? (even-2 or odd-1) ")


if int(parity) == 2:
    my_file = open('even_file.dat', 'w')
    for i in range(int(N)):
        my_file.write("%d \n"%(2*i))
        
elif int(parity) == 1:
    my_file = open('odd_file.dat', 'w')
    for i in range(int(N)):
        my_file.write("%d \n"%((2*i)+1))
else:
    print ("unknow option")

print ("Done")
my_file.close()
