# -*- coding: UTF-8 -*-
"""
problem5.py
====

Author:  




Write a program that determines the user's salary at the end of each year
from year 1 to 10. 
Your program should prompt the user for the initial salary and for the percent
increasy that is going to be applied at the end of each year (same
for all of the years).

Hint: For dollar amounts we want to limit the number of decimal places to just two
(we are not going to be listing fractions of a cent). 
To do so, you can use the format() function as follows:
    assume that that variable salary is equal to 10.038791
        format (salary, '.2f') 
    returns a string  "10.03"
Try to use this function in your pgoram to print the dollar amounts with two decimal
places. 
   
==============
Possible interaction: 
    
    
Enter your initial salary: 50000

Enter the percent increase at the end of each year [2, for 2%, for example]: 2

year    salary
1       $51000.00
2       $52020.00
3       $53060.40
4       $54121.61
5       $55204.04
6       $56308.12
7       $57434.28
8       $58582.97
9       $59754.63
10      $60949.72

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
    
#set the number of years to be used 
num_of_years = 10

#prompt the user for initial salary and percentage increase 
salary0 = float ( input ("Enter your initial salary: "))
percent_increase = float(
     input ("Enter the percent increase at the end of each year [2, for 2%, for example]: "))

#print the table header 
print("year\tsalary") 

#calculate salary at the end of each year 
for year in range(1,num_of_years+1):
    salary = salary0 * ( (1+percent_increase/100)**year )
    print (year, "\t$", format(salary, ".2f"), sep="")
   
