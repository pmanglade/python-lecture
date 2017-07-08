#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
 # Lemiere Yves
 # Juillet 2017

 

print("***************************")
print("* Welcome in meteost@t    *")
print("***************************\n")

my_file = open('meteo.dat', 'r')
results_file = open('stat.dat', 'w')

mean = 0
max  = 0
min  = 10000
sum  = 0
iterator = 0
list_temperature=[]

for a_line in my_file.readlines():
    #print(a_line)
    #print(type(a_line))
    a_list_of_word=a_line.split(" ")
    #print(type(a_list_of_word))
    #print(a_list_of_word)
    print(a_list_of_word[4])
    temp = float(a_list_of_word[4])
    iterator+=1
    if temp > max:
        max = temp
    if temp < min:
        min = temp
    sum += temp
    list_temperature.append(temp)


mean = sum / iterator

print("max: %f"%max)
print("min: %f"%min)
print("mean: %f"%mean)
results_file.write("max = %f \n"%max)
results_file.write("min = %f \n"%min)
results_file.write("mean= %f \n"%mean)
print("done")

print("list      : ")
print(list_temperature)
print("\n")
list_temperature.sort()
print("ascending : ")
print("\n")
print(list_temperature)


my_file.close()
