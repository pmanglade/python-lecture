#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

import matplotlib.pyplot as plt
import random


debug = True


if debug:
    print("************************")
    print("* Welcome in random_0  *")
    print("************************\n")

nombreDeBase=[]
for i in range(100):
    nombreDeBase.append(random.randint(1,10))
    

        
data = []
data.extend(nombreDeBase)
plt.hist(data,50, normed=1, facecolor='g', alpha=0.75)
plt.show()

nombreDeBase=[]

for i in range(100):
    nombreDeBase.append(random.uniform(1,10))


    
data = []
data.extend(nombreDeBase)
plt.hist(data,10, normed=1, facecolor='r', alpha=0.75)
plt.show()



# nombreDeBase=[]

# for i in range(100):
#     nombreDeBase.append(random.randn(1,10))


liste_de_base=['fifi','riri','loulou']
print(liste_de_base)
random.shuffle(liste_de_base)
print(liste_de_base)
print(random.choice(liste_de_base))
print(random.choice(liste_de_base))
print(random.choice(liste_de_base))
    
# data = []
# data.extend(nombreDeBase)
# plt.hist(data,10, normed=1, facecolor='r', alpha=0.75)
# plt.show()


# if random() <= 0.32:
#     print("gagné")
# else:
#     print("perdu")


# un jeu de carte
couleur = ["pique", "coeur", "carreau", "trèfle"]
hauteur = ["As", "Roi", "Dame", "Valet", "Dix", "Neuf", "Huit", "Sept"]

jeu = []
for c in couleur:
    for h in hauteur:
        jeu.append(h+" de "+c)

print("Le jeu neuf :")
print(jeu)

# mélanger
random.shuffle(jeu)
print("Le jeu mélangé")
print(jeu)

# Choisir au hasard le nombre de carte à donner
N = random.randint(3, 10)
print("Je donne "+str(N)+" cartes")

# Donner N cartes
donne = random.sample(jeu, N)
print("Les voilà :")
print(donne)

# Attention les cartes données sont encore dans le jeu
print("Le jeu est-il complet ?")
print(len(jeu))

