import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde
from numpy import linspace

# grades = [65, 70, 75, 80, 85, 90, 95, 75, 80, 85]  
grades = [73, 79, 97, 98, 78, 92, 72, 87, 69, 83, 12, 10, 20]  
# grades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
# grades = [45, 65, 48, 62, 55, 55, 56, 54, 50, 60]  

grades.sort() 

#plot the histogram of the grades 
hist, bins, patcs = plt.hist(grades, range=(0,105), bins=20,color='blue' ) 

plt.xticks(np.arange(0,100,5))
plt.grid(color='gray', which='both', linestyle=':', linewidth=0.25)

mean = np.mean(grades) 
median = np.median(grades)
std = np.std(grades) 

print("mean: ", mean)
print("median: ", median)
# print("std: ", std)

plt.show() 
