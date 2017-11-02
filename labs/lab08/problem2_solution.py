"""
problem2.py
====

Author:  
    


Write a program that counts the #'s of vowels (A,E,I,O,U,Y) in a string entered by the user. 
Display the results for each vowel

==============
Here is a sample run of your program:

enter your string: It's a dangerous business, Frodo, going out your door. You step 
onto the road, and if you don't keep your feet, there's no knowing where you might 
be swept off to.

A:  4
E:  14
I:  6
O:  20
U:  8
Y:  5    


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

phrase = input("enter your string: " )

countA = 0
countE = 0
countI = 0
countO = 0
countU = 0
countY = 0

for c in phrase :
    if c.lower() == 'a' :
        countA +=1
    elif c.lower() == 'e' :
        countE +=1
    elif c.lower() == 'i' :
        countI +=1
    elif c.lower() == 'o' :
        countO +=1
    elif c.lower() == 'u' :
        countU +=1
    elif c.lower() == 'y' :
        countY +=1
        
print ("A: ", countA) 
print ("E: ", countE) 
print ("I: ", countI) 
print ("O: ", countO) 
print ("U: ", countU) 
print ("Y: ", countY) 

