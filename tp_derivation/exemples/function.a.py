#!/usr/bin/env python
import numpy as np
# Example of a function (f2) using an other function as argument.
def f2(f,x):
   fx   = f(x)             # Compute the value of function f at point x 
                           # (this require that the argument f is a function and x an argument to this function).
   xp   = x+np.pi          # Compute the value xp. 
                           # Since np.pi = 3.14... x must be something that can be additioned to a float
   fxp  = f(xp)            # Compute the value of function f at point xp = x+np.pi.
   result = fx+fxp          
   return result


def main():
   # Example of f2 usage with the function sin from numpy package. 
   # The function f2 will be used at three values of x : 1, 2, and 3.
   fval = f2(np.sin,1.)          # get the value of f2 with argument np.sin and 1
   str_fval = str(fval)          # convert the result into a string
   message="x=1, f2="+str_fval   # make the string message by concatenating the previous string with a prefix : x=1, f2=
   print(message)                # print the string message
   fval = f2(np.sin,2)
   str_fval = str(fval)
   message="x=1, f2="+str_fval
   print(message)
   fval = f2(np.sin,3.)
   str_fval = str(fval)
   message="x=1, f2="+str_fval
   print(message)

#call the main function to demonstrate the use of this program
main()
