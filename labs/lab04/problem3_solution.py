"""
problem3.py
====

Author:  




You just got a summer job offer. The only things strange about it
is the pay structure. It seems that the deal your boss is offering
is not that grate. Here is the offer: 
    the first day, you will make 1 cent 
    the second day, the amount will be doubled
    the third day, you will get twice as many cents as on day 2
    the fourth day, ...
You should see the pattern by now. Every day, the number of cents 
that you earn is twice the number of the day before. 

Will you take this job for thirty days? 

Write a program that helps you decide. The program should print (in dollars, not cents)
how much the pay is on each of the days 1 through 30. 
Your program should also display the total amount earned below the table. 
 
   
==============
Output of this program (shortened and with values hidden - your output
should contain all of the values):
    
day     pay
-------------------
1        $0.01
2        $0.02
3        $0.04
4        $0.08
5        ...
...
29       ...
30       ...
In 30 you earn $...


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
num_of_days = 30

print("day\tpay")
print("-------------------")
pay = 1
day = 1
total_pay = pay 
print(day,"\t $", pay/100, sep="")
for day in range(2,num_of_days+1):
    pay = pay*2
    total_pay = total_pay + pay
    print (day,"\t $", pay/100, sep="")
print ("In ", num_of_days, " days you will earn $", total_pay/100, ".", sep="")      
