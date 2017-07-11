#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# Lemiere Yves
# Juillet 2017




## Ceci est la définition de la fonction calculate_polynome
def calculate_polynome(a_,b_,c_,x_, debug_="None"):

   result = a_*(x_*x_)+b_*(x_)+c_
   if debug_:
      print("Result is : %f"%result)
      
   return result
   

## Ceci est le programme principal
if __name__ == "__main__":
   debug = True
   
   if debug:
      print("*************************")
      print("* Welcome in function_1 *")
      print("*************************\n")
      
      
      param_a = 1
      param_b = 2
      param_c = 3
      x_value = 0
      
      y_result = calculate_polynome(param_a,param_b,param_c,x_value,debug)
      print("f(%d) = %f"%(x_value,y_result))
            
            
      x_value=1
      y_result = calculate_polynome(param_a,param_b,param_c,x_value,debug)
      print("f(%d) = %f"%(x_value,y_result))
