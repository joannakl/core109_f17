"""
problem4.py
====

Author:  


Write a program that plays a lottery.
The user is asked to pick 4 numbers for the game. 
The numbers should be between 1 and 10 (your program should verify this). 

The program should generate its own list of 4 random lucky numbers and it
should display the results that state how many out of the lucky numbers
the user got. 

----
Here are some sample runs of the program:

Pick four numbers from 1 to 100 as your lottery choices.

Enter your number 1: 9

Enter your number 2: 8

Enter your number 3: 7

Enter your number 4: 6

CONGRATULATIONS: you picked 3 of the four lucky numbers: [9, 1, 7, 8]    
 

-- 

Pick four numbers from 1 to 100 as your lottery choices.

Enter your number 1: 1

Enter your number 2: 6

Enter your number 3: 3

Enter your number 4: 8

CONGRATULATIONS: you picked 1 of the four lucky numbers: [4, 8, 8, 2]     
 

-- 

Pick four numbers from 1 to 100 as your lottery choices.

Enter your number 1: 1

Enter your number 2: 7

Enter your number 3: 2

Enter your number 4: 9

Sorry, you did not get any lucky numbers   
        
 


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)           
                    
"""

import random

print("Pick four numbers from 1 to 100 as your lottery choices.\n")
val = [] 
val = val + [int(input("Enter your number 1: " ) )]
val = val + [int(input("Enter your number 2: " ) )] 
val = val + [int(input("Enter your number 3: " ) ) ]
val = val + [int(input("Enter your number 4: " ) ) ]

# roll pick the lottery numbers
lucky=[]
high = 10 
lucky = lucky +[ random.randint(1,high) ]
lucky = lucky +[ random.randint(1,high) ]
lucky = lucky +[ random.randint(1,high) ]
lucky = lucky +[ random.randint(1,high) ]

# count number of user values in the lucky numbers 
count = 0
for value in val : 
    if value in lucky : 
        count += 1

if count > 0 :
    print ("\nCONGRATULATIONS: you picked", count, "of the four lucky numbers:", lucky)
else:
    print ("\nSorry, you did not get any lucky numbers") 


