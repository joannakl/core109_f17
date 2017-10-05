"""
problem2.py
====

Author:  




Write a program that displays a table of the Celsius temperatures 0 through 30 
(in increments of 2) and their Fahrenheit equivalents. The formula for converting 
a temperature from Celsius to Fahrenheit is 
    
        f = 9/5 * c + 32

where f is the Fahrenheit remperature and c is the Celsius temperature. 
Your program must use a loop to display the results. 
        

==============
Output of this program:
    
Celsius Fahrenheit
-------------------
-10     14.0
-8      17.6
-6      21.2
-4      24.8
-2      28.4
0       32.0
2       35.6
4       39.2
6       42.8
8       46.4
10      50.0
12      53.6
14      57.2
16      60.8
18      64.4
20      68.0
22      71.6
24      75.2
26      78.80000000000001
28      82.4
30      86.0
32      89.6
34      93.2
36      96.8
38      100.4
40      104.0

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""


print("Celsius\tFahrenheit")
print("-------------------")
for c in range(-10, 41, 2):
    f = 9/5*c+32
    print (c, f, sep="\t")    
