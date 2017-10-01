import numpy as np
import matplotlib.pyplot as plt

# let's try to plot a quadtratic funciton
# y = (x-3)^2 - 25 

# first let's get some points for the x axis 
# np.linspace works similar to the range()
# function, but 1) both end points are included, 
# 2) the last parameter states
# how many values we want, not the interval
x = np.linspace(0, 10.0, 6)

# now we calculate the corresponding y values 
y = (x-3)**2 - 25 

#finally, plot the graph and show it 
plt.plot(x, y)
plt.show()