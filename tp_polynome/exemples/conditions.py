#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017


def main():

    print("*************************")
    print("* Welcome in conditions *")
    print("*************************\n")

    name = input("What's your name? ")
    print("Nice to meet you " + name + "!\n")


    input_number = input("Please, give me an integer : ")
    print("Your favorite number is " + input_number + "\n")

    number = int(input_number)

    input_another_number = input("Please, give me a greater integer : ")

    another_number = int(input_another_number)



    if another_number > number:
        print("Right, {} is greater than {} \n".format(another_number,number))
    elif  another_number < number:
        print("You're wrong, {} is not greater than {} \n".format(another_number,number))
    else:
        print("You entered two times the same values...\n")


    if another_number >= 0 and number >= 0:
        print("The product of values will be positive! \n")
    elif another_number >= 0 and number <= 0:
        print("The product of values will be negative! \n")
    elif another_number <= 0 and number >= 0:
        print("The product of values will be negative! \n")
    else:
        print("Unknown case! \n")




main()
