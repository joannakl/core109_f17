"""
problem1.py
====

Write a program that prompts the user for a current temperature
(in Fahrenheit degrees). 
The program should respond my printing one of the following 
statements:
    
- if temperature is below 0F,
    It is VERY COLD.
- if the temperature is between 0F and 32F (inclusive)
    It's cold, but it could be worse.
- if the temperature is above 32F and below 75F, 
    Great temperature, isn't it?
- if the temperature is above 75F, 
    Hot, hot, hot!

Example interactions:
    
Enter the current temperature: 85
Hot, hot, hot!

--- 
Enter the current temperature: 24
It's cold, but it could be worse.


__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

temp = float(input("Enter the current temperature: "))

if temp < 0:
   print("It is VERY COLD.")
elif temp < 32:
   print("It's cold, but it could be worse.")
elif temp < 75:
   print("Great temperature, isn't it?")
else:
    print("Hot, hot, hot!") 