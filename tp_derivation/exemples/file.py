#!/usr/bin/env python
import numpy as np
# Example of file Manipulation

# Let's start by creating some data
x = np.arange(0,1,0.11)[:]
y = np.exp(x)

######################################### WRITING DATA ##########################################
# Now let's write the data into a file
wf = open("exp.dat","w")                  #open the file "exp.dat" in writing mode
for i in range(len(x)):                    #let's loop over as much element as there is in x
   wf.write(str(x[i])+" "+str(y[i])+"\n") #write must receive only a single "string" argument
wf.close()                                #close the file "exp.dat" associated with the object wf

#alternatively the same data could have been generated and written this way
wf=open("exp2.dat","w")
for l in np.arange(0,1,0.11):
   wf.write(str(l)+" "+str(np.exp(l))+"\n")
wf.close()


######################################### READING DATA ##########################################
rf = open("exp.dat","r")                # open the file "exp.dat" in reading mode
lines = rf.readlines()                  # read the whole file and put the content in the liste lines
x = []                                  #
y = []                                  # create list x and y 
for line in lines:                      # loop over each element of the file associated with rf
    p = line.split()                    # split a line 
    x.append(float(p[0]))               # append the first element of the line to x AFTER conversion to float
    y.append(float(p[1]))               # append the second ...
                                        # NOTE that number are read as string and must be converted
rf.close()                              # close the file
print(np.log(y))