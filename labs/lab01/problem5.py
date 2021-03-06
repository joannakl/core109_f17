"""

Python has many different ways of producing graphics. In this final problem of Lab01,
you will get a chance to instruct the computer in how to draw.

Unfortunately, PythonAnywhere cannot display the results of the drawn canvas in its
console. For this problem you will need to use another web-based Python interpreter
called *Trinket*.

Go to the following URL to see the first program: https://trinket.io/python/ee436f59e1
(open it in a new tab or window, so you can go back and forth between this file and
the program).

You should be able to figure out what this program is doing. If not, you can just
look at the output and see the result.


Another, slightly more interesting program, is at the following URL:
https://trinket.io/python/479520a9d9

Run both programs and answer the questions below.
"""

# #program 1
# import turtle
# 
# turtle.shape("turtle")
# turtle.color("green")
# 
# turtle.circle(50)

#program 2
import turtle

turtle.shape("turtle")
turtle.color("green")

for i in range(5,100,5):
  turtle.circle(i)

turtle.hideturtle()


"""


====
QUESTION 1:
In the second program, what do you think causes turtle to draw repeated circles instead
of just one as in the first program?

ANSWER 1:






====
QUESTION 2:
What happens when you change the values of numbers in the range(5,100,5) instruction?
Try to change each of the numbers to a few other things and describe what the effect is.

ANSWER 2:







"""