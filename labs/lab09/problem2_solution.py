"""
problem2.py
====

Author:  
    



Write a program that modifies a given list of numbers if the following way:
    - if the element is negative, it is multiplied by -1
    - if the element is positive and a multiple of 3, it should be set to three
    - if the element is positive and a multiple of 5, it should be set to five
    - if the element is positive and a multiple of 3 and 5, it should be set to 15 
(all other values should be unchanged). 

The program below has a few definitions of specific lists called numbers
but your program should work even if the code is edited to change the 
content of that list to an arbitrary list of numbers. 

The program should print the list of numbers before and after all mofications are done. 

==============
Here are a few sample runs of your program:
    
initial list: 
[1, -3, 5, -17, 13, 72, -98, 615]
changed list: 
[1, 3, 5, 17, 13, 3, 98, 15]

--

initial list: 
[3, 5, 15, -8, 43, 78, -9]
changed list: 
[3, 5, 15, 8, 43, 3, 9]

--                

initial list: 
[5, 2, 3, -1, -2]
changed list: 
[5, 2, 3, 1, 2]

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

# numbers = [1, -3, 5, -17, 13, 72, -98, 615]

# numbers = [3, 5, 15, -8, 43, 78, -9]

numbers = [5, 2, 3, -1, -2]


print('initial list: ', numbers, sep='\n') 
 
for index in range ( len(numbers) ): 
    if numbers[index] < 0 : 
        numbers[index] = -1 * numbers[index]
    elif numbers[index] % 3 == 0 and numbers[index] % 5 == 0 :
        numbers[index] = 15
    elif numbers[index] % 3 == 0 :
        numbers[index] = 3
    elif numbers[index] % 5 == 0: 
        numbers[index] = 5

print('changed list: ', numbers, sep='\n') 