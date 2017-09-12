#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.07, 5, 0.1*np.sqrt(2)) # First create a list for the abcissas.
y = np.sin(x)            # Then compute the list of ordinates.
                         # Notice how all points in the list are computed through a single instruction.

plt.plot(x, y)           # Then plot all this
plt.show()               # AND display the plot

plt.loglog(x,abs(y))     # Make a loglog plot now
plt.show()               # AND display the plot


# It is possible to have multiple plots
plt.plot(x,y)
plt.plot(x+0.5,y)
plt.plot(x,-y)
plt.plot(x,y*1.3)
plt.show()

# And in this case it is better to label them:
plt.plot(x,y,label="P1")
plt.plot(x+0.5,y,label="P2")
plt.plot(x,-y,label="P3")
plt.plot(x,y*1.3,label="P4")
plt.title("Four plots")         # Set a title
plt.xlabel("Angles [radians]")  # Label axis x
plt.ylabel("y [a.u.]")          # Label axis y
plt.axis([np.pi/2,np.pi*3/2,-1,0])# Choose the displayed part
plt.grid(True)                  # display a grid



plt.legend()
plt.show()
