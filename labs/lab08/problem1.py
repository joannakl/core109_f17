"""
problem1.py
====

Author:  



Write a program that asks the user to enter a username and select a password
for it. 

The program the should _validate_ the password using the following rules
    * the password cannot contain the username as its substring
    * the password cannot contain the string `password` as its substring
    * the password has to contain at least one digit
    * the password has to contain at least one upper case and one lower case character
    
If the password is valid, the program should print "OK". If it is not,
the program should print "Invalid!" and follow it by the reason why the password is invalid. 

==============
Here are a few sample runs of your program:
    
username: joanna
password: joannaklukowska

Invalid!
passwords cannot contain usernames

-- 
username: joanna
password: 123klukowska

Invalid!
passwords have to contain at least one uppercase letter

--

username: joanna
password: Banana123Pumpkin

OK!

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
