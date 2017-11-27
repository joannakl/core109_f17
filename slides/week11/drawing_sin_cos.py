
# https://trinket.io/python/d4c8bc7dcf
 
import math
import turtle

# resize the screen for drawing of trigonometric funtions 
wn = turtle.Screen()
wn.setworldcoordinates(-1,-2,8,2)

#setup the turtle to draw the sin() function
fred = turtle.Turtle()
fred.pencolor('green')
fred.shape("turtle")
fred.penup()

#setup the turtle to draw the cos() function
jack = turtle.Turtle()
jack.pencolor('blue')
jack.shape("turtle")
jack.penup()

#draw the two functions 
for x in range(360):
    x = math.radians(x)
    y1 = math.sin(x)
    y2 = math.cos(x)
    fred.goto(x, y1)
    jack.goto(x, y2)
    fred.pendown()
    jack.pendown()
