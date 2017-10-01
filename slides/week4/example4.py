# -*- coding: utf-8 -*-
# track rentals 

import numpy as np
import matplotlib.pyplot as plt

# let's try to plot the cost of renting a track from each of the four
# companies - the price is a function of the milage driven  

# we want the plot for number of miles ranging from 0 to 100 
num_of_points = 101 
miles = np.linspace(0, 100, num_of_points )

# we calculate the corresponding prices for each company 
watertown = 79.0 * np.ones(num_of_points)
uhal = miles * 1.39 + 29.95
budget = miles * 0.99 + 29.95
enterprise100 = 59.95 * np.ones(num_of_points)
 

#finally, plot the graph and show it 
plt.plot(miles, watertown, 'y.')    
plt.plot(miles, uhal, 'b.')    
plt.plot(miles, budget, 'r.')  
plt.plot(miles, enterprise100, 'g.')  
plt.show()


# save plot to file
plt.savefig('/home/asia/Data/NYU_Teaching/core109/code/plotting/CarRental_100.png')