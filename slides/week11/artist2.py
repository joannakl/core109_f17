
'''
https://trinket.io/python/a1a282b662

This program recreates the fractal art produced 
by Hamid Naderi Yeganeh. 

''' 


import turtle
import math

artist = turtle.Turtle()
artist.speed(0)
artist.pensize(.1) 
artist.hideturtle()

count = 6000
scale = 100

for i in range(count) :
  x1 = math.sin(28*math.pi*i/count)
  y1 = math.cos(14*math.pi*i/count)
  x2 = math.sin(48*math.pi*i/count)
  y2 = math.cos(24*math.pi*i/count)
  print(i)
  artist.penup()
  artist.goto(x1*scale, y1*scale)
  artist.pendown()
  artist.goto(x2*scale, y2*scale)
  
