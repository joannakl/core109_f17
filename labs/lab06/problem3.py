"""
problem3.py
====

Author:  



Write a program that allows the user to figure out when their initial investment 
into a savings account would double.

The program should prompt the user for the value of the investment 
and the interest rate (expressed as a percentage). 
You can assume that the interest rate is componded yearly (i.e., the interest 
amount is added to the principal at the end of each year).

The program should display the balance in the savings account at the end of each year
for as many years as it takes for the balance to at least double the initial
deposit. 

The program should validate that the deposit value is a positive number and that the 
interest rate is a number between 0 and 100. In both cases, you should be working with 
floats (not ints). 

Use format(balance,'.2f') to display the value of the balance with two decimal places. 


==============
Here are a few sample runs of your program:
    


Enter the initial deposit: 1000.00

Enter the interest rate (as a percentage): 3.00

year    balance
1       $1030.00
2       $1060.90
3       $1092.73
4       $1125.51
5       $1159.27
6       $1194.05
7       $1229.87
8       $1266.77
9       $1304.77
10      $1343.92
11      $1384.23
12      $1425.76
13      $1468.53
14      $1512.59
15      $1557.97
16      $1604.71
17      $1652.85
18      $1702.43
19      $1753.51
20      $1806.11
21      $1860.29
22      $1916.10
23      $1973.59
24      $2032.79

===

Enter the initial deposit: 500.00

Enter the interest rate (as a percentage): 10.0

year    balance
1       $550.00
2       $605.00
3       $665.50
4       $732.05
5       $805.26
6       $885.78
7       $974.36
8       $1071.79


 ----------
number of grades:  0

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

