

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde
from numpy import linspace
# 
# grades = [23, 79, 67, 98, 78, 92, 12, 87, 89, 73, 98, 79, 97, 55, 4, 92,
#     56, 79, 73, 95, 71, 46, 87, 29, 41, 97, 88, 86, 90, 95, 100, 94 ]
grades = [23, 79, 67, 98, 38, 52, 32, 87, 63, 73, 17, 59, 67, 55, 44, 92,
    56, 69, 82, 25, 61, 46, 57, 49, 41, 97, 35, 86, 28,  9, 80, 51 ]
# grades = [23, 79, 47, 98, 38, 32, 32, 87, 79, 83, 71, 39, 77, 45, 44, 92,
#     46, 79, 83, 25, 71, 36, 47, 49, 41, 70, 75, 43, 15, 60, 34, 80]
# grades = [79, 46, 52, 77, 79, 65, 68, 30, 68, 96, 70, 76, 82, 24, 63, 78, 
#     71, 57, 51, 74, 93, 67, 81, 82, 85, 74, 61, 72, 89, 82, 77, 9]  

grades = [23, 79, 97, 98, 78, 92, 12, 87, 89, 73]  

grades.sort() 

# plt.plot(grades) 
# plt.show()

#plot the histogram of the grades 
hist, bins, patcs = plt.hist(grades, range=(0,100), bins=20,color='blue' ) 


# this create the kernel, given an array it will estimate the probability over that values
kde = gaussian_kde( grades )
# these are the values over wich your kernel will be evaluated
dist_space = linspace( 0,100, 100 )
# plot the results
kde_vals = kde(dist_space)
kde_vals = max(hist)/max(kde_vals) * kde_vals 
plt.plot( dist_space, kde_vals, color='green'  )

plt.xticks(np.arange(0,100,5))
plt.grid(color='gray', which='both', linestyle=':', linewidth=0.25)

mean = np.mean(grades) 
median = np.median(grades)
std = np.std(grades) 

print("mean: ", mean)
print("median: ", median)
print("std: ", std)

plt.axvline(x=mean,ymax=0.3, color='orange', label="mean="+str(mean) ) 
for i in [-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5] :
    val = mean + i*std 
    if (val > 0 and val < 100 ) : 
        plt.axvline(x=val, ymax=0.2, linestyle='--', color='orange') 

plt.axvline(x=median,ymin=0.7, color='red', label="median="+str(median)) 
for i in [-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5] :
    val = median + i*std 
    if (val > 0 and val < 100 ) : 
        plt.axvline(x=val, ymin=0.8, linestyle='--', color='red') 
plt.legend() 

plt.show() 
