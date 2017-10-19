"""
problem2.py
====

Author:  



You are going to write a program that generates a "hailstone sequence",
see https://plus.maths.org/content/mathematical-mysteries-hailstone-sequences 

The sequence should start with a positive integer specified by the user.
Your program should make sure that the user enters a positive number, and if 
that is not the case, it should prompt the user for a correct value (over and over
again until the proper value is specified).

Once you have the user specified value, the rules of the game are as follows:
    - if the number is even, divide it by 2 
    - if the number is odd, multiply it by 3 and add 1
This gives you the next value in the sequence (the user's input is the first value).
Now, do it again:
    - if the new number is even, divide it by 2 
    - if the new number is odd, multiply it by 3 and add 1
and again:
    - if the new number is even, divide it by 2 
    - if the new number is odd, multiply it by 3 and add 1
and again:
    - if the new number is even, divide it by 2 
    - if the new number is odd, multiply it by 3 and add 1
... until the number calculated reaches 1.     

HINT: you will need two different while loops in this program;
one for validation of user's number, the other for generating the sequence  

==============
Here are a few sample runs of your program:
    
Enter a positive integer to start the sequence: 5
Your sequence is:
5, 16, 8, 4, 2, 1, 

--

Enter a positive integer to start the sequence: 23
Your sequence is:
23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1, 

--                

Enter a positive integer to start the sequence: 150
Your sequence is:
150, 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1, 

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
  

