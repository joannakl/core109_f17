"""
problem2.py
====

Author:  


Module 3 (https://cs.nyu.edu/elearning/CSCI_UA_0002/module03.php) contained some 
discussion about generating random numbers.

Read and understand the code of a program. The program uses random numbers to 
simulate rolling of a six-sided die. 

Answer the questions below the program and change the code according to instructions
in the last question. 


    
"""

import random

num_of_repeats = int(input("How many times should I roll the die? \n"))
num_of_sides  = 6 

print("Rolling", num_of_repeats, "times.")

# initialize counts to zero 
counts = [0]*num_of_sides

# simulate rolling the die 
for i in range(num_of_repeats) :
    # roll the virtual die
    die = random.randint(1,num_of_sides+3) 
    # increment appropriate count
    counts[(die-1)%num_of_sides] += 1 


# print the report 
for i in range(num_of_sides) :
    print(i+1, " was rolled ", counts[i], " many times (", 
            counts[i]/num_of_repeats*100, "% of times)",
    sep = "")
    
'''
How many times does the program have to roll a die to get almost the 
same number of rolls of each value (the percent should be the same, except for the
fraction part)? 

ANSWER:
    
    
    
    

What do you need to change in the above program so that it simulates
rolling of a 5-sided die? (Show the modified lines as part of your answer.)

ANSWER: 
    
    
    
    
What do you need to change in the above program so that it does not simulate a fair die, 
but instead the values of 1, 2 and 3 are twice as likely as the values of 4, 5, and 6?
Make the changes in the program and submit a mofied version. 
The output of your mofied program should be similar to:
-----    
How many times should I roll the die? 
1000000
Rolling 1000000 times.
1 was rolled 222099 many times (22.209899999999998% of times)
2 was rolled 221374 many times (22.1374% of times)
3 was rolled 222807 many times (22.2807% of times)
4 was rolled 111084 many times (11.1084% of times)
5 was rolled 111599 many times (11.1599% of times)
6 was rolled 111037 many times (11.1037% of times)
-----



'''