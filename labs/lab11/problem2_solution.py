"""
problem2.py
====

Author:  
  

Write a program similar to the one from problem 1. This version
of the program should simulate rolling of two six-sided dice and display
number of times and percentage of time that each of the 11 possible outcomes
was generated (an outcome in this experiment is the sum of values rolled on
the two dice). 

WARNING: it is not enough to generate random numbers from 2 to 12. 

EXTRA CHALLENGE: add the code that shows the plot of this probability distribution 

-------------
Here is a sample run of the program: 

How many times should I roll the die? 
100000
Rolling 100000 times.
2 was rolled 0.02743 many times (2.743% of times)
3 was rolled 0.05613 many times (5.6129999999999995% of times)
4 was rolled 0.08319 many times (8.319% of times)
5 was rolled 0.11037 many times (11.036999999999999% of times)
6 was rolled 0.13878 many times (13.877999999999998% of times)
7 was rolled 0.16739 many times (16.739% of times)
8 was rolled 0.14098 many times (14.097999999999999% of times)
9 was rolled 0.11023 many times (11.023% of times)
10 was rolled 0.0819 many times (8.19% of times)
11 was rolled 0.05596 many times (5.596% of times)
12 was rolled 0.02764 many times (2.7640000000000002% of times)




==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""


import matplotlib.pyplot as plt
import random

num_of_repeats = int(input("How many times should I roll the die? \n"))
num_of_sides  = 6 
num_of_outcomes = 11

print("Rolling", num_of_repeats, "times.")

outcomes = list(range(2,13,1) )
# initialize counts to zero 
counts = [0]*num_of_outcomes

# simulate rolling the die 
for i in range(num_of_repeats) :
    # roll two virtual dice
    die1 = random.randint(1,num_of_sides) 
    die2 = random.randint(1,num_of_sides) 
    # increment appropriate count
    counts[die1+die2-2] += 1 


# print the report 
for i in range(num_of_outcomes) :
    #calculate fraction of rolls for each value 
    counts[i] = counts[i]/num_of_repeats
    #print the results 
    print(i+2, " was rolled ", counts[i], " many times (", 
            counts[i]*100, "% of times)", sep = "")
    
print (outcomes)
print(counts)

plt.plot(outcomes, counts)
axes = plt.gca()
axes.set_ylim([0,1]) 
plt.show()