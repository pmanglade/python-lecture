#!/usr/bin/env python

a=1; b=2

##################
# IF
if a > b :
   print("a est le plus grand\n")

##################
# IF ELSE
if a > b :
   print("b est le plus petit\n")
else :
   print("a est le plus petit\n")

##################
# IF ELIF ELSE
if a > b:
   print("a n'est pas le plus petit\n")
elif a==b: ###### WARNING USE == not = to test EQUALITY
   print("Égalité\n")
else :
   print("C'est b qui l'emporte\n")

##################
# AND OR
if a==b or a > b and b < a :
   print("ok")
else :
   print("not ok")
