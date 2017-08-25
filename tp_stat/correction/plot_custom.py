#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017


import matplotlib.pyplot as plt


debug = True

if debug:
    print("*******************")
    print("* Welcome in plot *")
    print("*******************\n")

my_file = open('carte.dat', 'r')
my_second_file = open('river.dat', 'r')

lines = my_file.readlines()
x=[]
y=[]

for element in lines:
    val = element.split()
    x.append(val[0])
    y.append(val[1])

lines=[]    
lines = my_second_file.readlines()
r_x=[]
r_y=[]

for element in lines:
    val = element.split()
    r_x.append(val[0])
    r_y.append(val[1])
    

my_file.close()
my_second_file.close()

plt.plot(x,y,'k,')
plt.plot(r_x,r_y,'r,')

#Ajout des titres du graphe
plt.xlabel('')
plt.ylabel('')
plt.axis('off')


plt.title('Carte de france')

#Ajustement des echelles
plt.axis([-5, 10, 42, 51])
#Préparation d'une grille
plt.grid(False)

#Affichage de la fenetre contenant le graphe
plt.show()
