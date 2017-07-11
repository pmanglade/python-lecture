#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017


 

print("************************")
print("* Welcome in condition *")
print("************************\n")

name = input("What's your name? ")
print("Nice to meet you " + name + "!\n")



input_number = input("Please, give me an integer : ")
print("Your favorite number is " + input_number + "\n")

# print (type(name))
# print (type(number))

number = int(input_number)

# print (type(converted_number))


input_another_number = input("Please, give me a greater integer : ")

another_number = int(input_another_number)

if another_number > number:
    print("Right, %s is greater than %s \n"%(another_number,number))
elif another_number < number:
    print("You're wrong, %s is not greater than %s \n"%(another_number,number))
else:
    print("You entered two times the same values...\n")


if another_number >= 0 and number >= 0:
    print("the product of values will be positive! \n")
elif another_number >= 0 and number <= 0:
    print("the product of values will be negative! \n")
elif another_number <= 0 and number >= 0:
    print("the product of values will be negative! \n")
else:
    print("unknown case \n")
    

    



