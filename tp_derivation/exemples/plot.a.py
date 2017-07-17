#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.07, 5, 0.1*np.sqrt(2))[:] # First create a list for the abcissas.
y = np.sin(x)            # Then compute the list of ordonate.
                         # Notice how each point is coputed in a single instruction.

plt.plot(x, y)           # Then plot all this
plt.show()               # AND display the plot

ay = abs(y)
plt.loglog(x,ay)         # Make a loglog plot this time
plt.show()               # AND display the plot


# It is possible to have multiple plots
plt.plot(x,y)
xp = x+0.5
plt.plot(xp,y)
my = -y
plt.plot(x,my)
ym = 1.3*y
plt.plot(x,ym)
plt.show()

# And in this case it is better to label them:
plt.plot(x,y,label="P1")
plt.plot(x+0.5,y,label="P2")
plt.plot(x,-y,label="P3")
plt.plot(x,y*1.3,label="P4")
plt.title("Four plots")         # Set a title
plt.xlabel("Angles [radians]")  # Label axis x
plt.ylabel("y [a.u.]")          # Label axis y
a=np.pi/2.
b=3*a
c=-1
d=0
plt.axis([a,b,c,d])  # Choose the displayed part x in [a,b], y in [c,d]
plt.grid(True)       # Display a grid
plt.legend()         # Choose to display the legend 
plt.show()

