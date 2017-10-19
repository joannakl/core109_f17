"""
problem1.py
====

Author:  


Write a program that asks the user to enter a positive odd integer. If the 
user does not, they should be re-prompted for a correct value.

The program should calculate the sum of all the odd numbers between 0 and
the value provided by the user.

USE THE WHILE LOOP! 



==============
Here are a few sample runs of your program:
    
Enter a positive odd integer: 15
The sum of all the odd numbers from 0 to 15 is 64

--

Enter a positive odd integer: 64

Sorry, this is not a valid value. Try again: 65
The sum of all the odd numbers from 0 to 65 is 1089

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

num = int(input("Enter a positive odd integer: "))

while num <= 0 or num%2 == 0 :
    num = int(input("Sorry, this is not a valid value. Try again: "))

value = num     
sum = 0;
while num > 0 :
    sum = sum + num
    num = num - 2

print ("The sum of all the odd numbers from 0 to", value, "is", sum)           
