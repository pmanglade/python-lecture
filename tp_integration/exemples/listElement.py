#!/usr/bin/env python
l = ['bla', 'lab', 'bal', 'alb']
# access list elements by position
for i in range(4):
   print(l[i])

# get the number of elements in a list
print(len(l)) 

# DO NOT duplicate a list this way
m=l
m[1]='mbc'
print(l) # otherwise you'll get this SURPRISE

#prefer this method
n=l[:]
n[1]='lab'
print(n)
print(l)

