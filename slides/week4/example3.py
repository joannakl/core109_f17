# -*- coding: utf-8 -*-
# electric bill 

import numpy as np
import matplotlib.pyplot as plt

# let's try to plot the values of our electric bill from Lane
# Electric b(k)=0.082 * k + 12.00

# we want the plot for number of kilo-watt-hours ranging from 0 to 1000,
# in increments of 20 kilo-watt-hours (so we need 51 points between 0 and 1000) 
k = np.linspace(0, 1000.0, 51)

# we calculate the corresponding bill amount 
b = 0.082 * k + 12 

#finally, plot the graph and show it 
plt.plot(k, b, 'b')   # plot a blue line 
plt.plot(k, b, 'r.')  # mark each point with a red dot 
plt.show()