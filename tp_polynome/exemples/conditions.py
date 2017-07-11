#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017


 

print("************************")
print("* Welcome in condition *")
print("************************\n")

name = input("What's your name? ")
print("Nice to meet you " + name + "!\n")



number = input("Please, give me an integer : ")
print("Your favorite number is " + number + "\n")

# print (type(name))
# print (type(number))

converted_number = int(number)

# print (type(converted_number))


another_number = input("Please, give me a greater integer : ")


if int(another_number) > int(number):
    print("Right, %s is greater than %s \n"%(another_number,number))
elif  int(another_number) < int(number):
    print("You're wrong, %s is not greater than %s \n"%(another_number,number))
else:
    print("You entered two times the same values...\n")


if int(another_number) >= 0 and int(number) >= 0:
    print("the product of values will be positive! \n")
elif int(another_number) >= 0 and int(number) <= 0:
    print("the product of values will be negative! \n")
elif int(another_number) <= 0 and int(number) >= 0:
    print("the product of values will be negative! \n")
else:
    print("unknown case \n")
    





