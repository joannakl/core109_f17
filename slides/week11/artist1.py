
'''
https://trinket.io/python/30ecf5204f

This program recreates the fractal art produced 
by Hamid Naderi Yeganeh. 

''' 

import turtle
import math

artist = turtle.Turtle()
artist.speed(0)
artist.pensize(0.01) 
artist.hideturtle()

#artist.tracer(0, 0)

count = 10000
scale = 100

for k in range(count) :
  x = math.cos(14 * math.pi * k / count) * (1 - 3/4 * (math.cos(20*math.pi*k/count)**2))
  y = math.sin(14 * math.pi * k / count) * (1 - 3/4 * (math.cos(24*math.pi*k/count)**2))
  r = 1/200 + 1/10 * (math.sin(54*math.pi*k/count)**6)
  print(k)
  artist.penup()
  artist.setx(x*scale)
  artist.sety(y*scale)
  artist.pendown()
  artist.circle(r*scale)
  
#artist.update()

