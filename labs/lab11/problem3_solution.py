"""
problem3.py
====

Author:  

Snake Eyes

Write a program that simulates rolling 2 6-sided dice repeatedly. 
The goal is to keep rolling until the result on both dice is 1 (snake eyes). 
The program should count the number of rolls it took to get snake eyes.

WARNING: it may take a long time for this program to finish sometimes

-------------
Here is a sample run of the program: 

3        4
1        3
2        2
3        2
1        6
1        6
4        5
4        2
2        3
5        1
3        2
1        1

12  rolls to snake eyes


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
import random 

count = 1
die1 = random.randint(1,6)
die2 = random.randint(1,6)
print ( die1, "\t", die2) 

while not(die1 == 1 and die2 == 1) :
	count += 1
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	print ( die1, "\t", die2) 

print ("\n\n", count, " rolls to snake eyes") 



