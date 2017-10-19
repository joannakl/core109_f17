"""
problem4.py
====

Author:  



Write a program that asks the user to continually enter student grades. 

To indicate the end of the list, the user will enter "-1" 
for the grade. 

Your program should validate that the grades are within a valid range of 0 to 100. 

Calculate the following information based on the data:

- number of students who took the exam

- average grade on the exam 

- lowest grade on the exam

- highest grade on the exam  




==============
Here are a few sample runs of your program:
    
Enter the grades one at a time. Enter -1 to indicate the end.

next grade: 90

next grade: -7
invalid score, not counted

next grade: 70

next grade: 85

next grade: -1

 ----------
number of grades:  3
average score:     81.66666666666667
lowest score:      70
highest score:     90

===

Enter the grades one at a time. Enter -1 to indicate the end.

next grade: -1

 ----------
number of grades:  0

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

     
print ('Enter the grades one at a time. Enter -1 to indicate the end.')

grade = 0
count = 0
total = 0
low = 101
high = -1 

while grade != -1 :
    grade = int(input("next grade: " )) 
    if grade < -1 or grade > 100 :
        print ("invalid score, not counted")
    elif grade != -1 :
        total = total + grade
        count = count + 1
        if low > grade : 
            low = grade 
        if high < grade:
            high = grade 
print('\n', '-'*10)
print ('number of grades: ', count )
if count > 0 :
    print ('average score:    ', total / count )
    print ('lowest score:     ', low)
    print ('highest score:    ', high)