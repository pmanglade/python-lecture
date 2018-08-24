#!/usr/bin/env python

# A list can contain objects of any type,
# for instance another list...
l=[1,2,3]
m=[10,20,30]
lm=[l,m]
print(lm)

# Accessing elements can be done this way
for i in lm:
   for j in i :
      print("i=",i,"j=",j)


# Accessing elements by position can be done this way
for i in range(len(lm)):
   for j in range(len(lm[i])) :
      print("position in lm : ",i,j,"element : ", lm[i][j])
