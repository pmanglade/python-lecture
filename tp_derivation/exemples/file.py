#!/usr/bin/env python
import numpy as np
# Example of file Manipulation

############################## WRITING DATA ###############################
def write_data():
   # Let's start by creating some data
   x = np.arange(0,1,0.11)[:]
   y = np.exp(x)
   # Now let's write the data into a file
   wf = open("exp.dat","w")  #open the file "exp.dat" in writing mode
   for i in range(len(x)):   #let's loop over as much element as there is in x
      wf.write('{} {}\n'.format(x[i],y[i])) 
   wf.close()                #close the file "exp.dat" associated with the object wf
   #alternatively the same data could have been generated and written this way
   wf=open("exp2.dat","w")
   for l in np.arange(0,1,0.11):
      wf.write("%f %f \n" % (l,np.exp(l))) 
   wf.close()

############################## READING DATA ###############################  
def read_data():
   rf = open("exp.dat","r")      # open the file "exp.dat" in reading mode
   lines = rf.readlines()        # read the whole file and put the content in the liste lines
   x = []                        #
   y = []                        # create list x and y 
   for line in lines:            # loop over each element of the file associated with rf
      p = line.split()           # split a line
      first_value  = float(p[0]) # NOTE that number are read as string and must be converted
      second_value = float(p[1])          
      x.append(first_value)      # append the first element of the line to x AFTER conversion to float
      y.append(second_value)     # append the second ...
   rf.close()                    # close the file
   print(np.log(y))

def main():
   write_data()
   read_data()
   return

main()
