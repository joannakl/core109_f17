'''
To lern from the documentation for the turtle package
you can use the official Python 3 documentation:
    https://docs.python.org/3.2/library/turtle.html
There are some good examples (like the one below) and detailed
descriptions of all of the functions


trinket.io link
https://trinket.io/python/ce301e7e94

'''

import turtle

bob = turtle.Turtle(); 
bob.speed(0)
bob.color('red', 'yellow')
bob.begin_fill()
for i in range(37):
    bob.forward(200)
    bob.left(170)
bob.end_fill()
bob.done()