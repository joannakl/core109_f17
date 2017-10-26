"""
problem3.py
====

Author:  


The Moon has much smaller gravitation than Earth. The consequence of this is that
a weight of a person on the Moon is smaller than the weight of the same person
on the Moon. Well, that is true for any object, not just people. 
Jupiter's gravitation is much larger than Earth's. So the weight on Jupiter is 
larger than the weight on Earth. 

The conversion formulas are

  weight_on_Moon = 1.622 * (weight_on_Earth / 9.81)
  weight_on_Jupiter = 24.79 * (weight_on_Earth / 9.81)
  
Write a program that canculates Moon's and Jupiter's weights for objects
whose weight on Earth ranges from 100 to 200 pounds in increments of 10 pounds.

Restriction: use a while loop (even though the for loop is a bit easier
and more appropriate here) .  

To find out weights on other celestial bodies, take a look at
https://www.exploratorium.edu/ronh/weight/  

==============
Here is the output that should be generated by your program:
    
Weight conversions: 
------------------------
Earth   Moon    Jupiter
------------------------
100     16      252
110     18      277
120     19      303
130     21      328
140     23      353
150     24      379
160     26      404
170     28      429
180     29      454
190     31      480
200     33      505

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

weight_on_Earth = 100
print ("Weight conversions: ")
print ("--------------------")
print ("Earth\tMoon\tJupiter")
print ("--------------------")
while weight_on_Earth <= 200 :
    weight_on_Moon = 1.622 * (weight_on_Earth / 9.81)
    weight_on_Jupiter = 24.79 * (weight_on_Earth / 9.81)
    print ( int(weight_on_Earth), int(weight_on_Moon), int(weight_on_Jupiter), sep='\t') 
    weight_on_Earth += 10