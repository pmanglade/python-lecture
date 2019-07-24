#!/usr/bin/env python
# Example of a simple loop
def main():
  n=7000000
  for i in range(5):
    n+=i
    print(i,n) 
  l=range(3) # l is a list
  for x in l:
    print("element",x)
  return

main()
