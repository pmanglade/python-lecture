#!/usr/bin/env python

l = ['bla', 'lab', 'bal', 'alb']
# Access list elements by position
for i in range(4):
   print(l[i])

# Get the number of elements in a list
print(len(l))

# DO NOT duplicate a list this way
m=l
m[1]='mbc'
print(l) # otherwise you'll get this SURPRISE

# Prefer this method
n=l[:]
n[1]='lab'
print(n)
print(l)
