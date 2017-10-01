# -*- coding: utf-8 -*-
# track rentals - version 2

import numpy as np
import matplotlib.pyplot as plt

# let's try to plot the cost of renting a track from each of the four
# companies - the price is a function of the milage driven  

##################
# the rules change after the first 100 miles
# so we will first do calculations for the 
# first 100 miles and then for the remaining miles
##################

# first 100 miles 

# we want the plot for number of miles ranging from 0 to 100 
num_of_points1 = 101 
miles1 = np.linspace(0, 100, num_of_points1 )

# we calculate the corresponding prices for each company 
watertown1 = 79.0 * np.ones(num_of_points1)
uhal1 = miles1 * 1.39 + 29.95
budget1 = miles1 * 0.99 + 29.95
enterprise1 = 59.95 * np.ones(num_of_points1)

# remaining miles (up to 300)

# we want the plot for number of miles ranging from 101 to 300 
num_of_points2 = 200 
miles2 = np.linspace(101, 300, num_of_points2 )

# we calculate the corresponding prices for each company 
watertown2 = 79.0 * np.ones(num_of_points2)
uhal2 = miles2 * 1.39 + 29.95
budget2 = miles2 * 0.99 + 29.95
enterprise2 = 59.95 + (miles2-100) * 0.59 


# combine results for first 100 and the remaining miles 

miles = np.concatenate((miles1,miles2)) 
watertown = np.concatenate((watertown1, watertown2))
uhal = np.concatenate((uhal1,uhal2))
budget = np.concatenate((budget1,budget2))
enterprise = np.concatenate((enterprise1,enterprise2) )

#finally, plot the graph and show it 
plt.plot(miles, watertown, 'y.', label="Watertown")    
plt.plot(miles, uhal, 'b.', label="U-Hal")    
plt.plot(miles, budget, 'r.', label="Budget")  
plt.plot(miles, enterprise, 'g.', label="Enterprise")  
plt.xlabel('Milage')        # add title to the x-axis
plt.ylabel('Total Cost')    # add title to the y-axis 
plt.legend(loc='upper left')   # create the legend with plot descriptions 


plt.show()

# save plot to file
plt.savefig('/home/asia/Data/NYU_Teaching/core109/code/plotting/CarRental_All.png')