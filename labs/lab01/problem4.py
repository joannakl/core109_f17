"""
problem4.py
===

In this course, we want to use programming as tool for quantitative reasoning:
performing calculations, analyzing data, producing graphs, etc.
Python has several packages that help with those tasks.

The program in this problem is much more sofisticated than the ones that we looked
at so far. But it should not be that hard to figure out what it does and make
small changes to it. You will not understand every single instruction here -
we do not expect you to. You should read through the instructions, tough, to notice
the keywords that might give you a hint of what is going on there.

When you run this program, you will not see any output in the console part of the
screen. That is a correct behavior. This program produces an image file that is
saved to the Lab01 folder. Open another tab in your browser and navigate to the Lab01
folder of PythonAnywhere. You should see a new file there called problem4_NY.png.
You can open that file by clicking on the "download" icon next to it (the arrow
that points down). This image was produced by the program when you run it.
(When you make changes to the program and re-generate the image, you may need to refresh
it to see the changes.)

Run this program (if you have not done so already) and answer the questions below.

"""

import matplotlib.pyplot as plt

months = range(1,13)
temperatures_high = [39,42,50,60,71,79,85,83,76,65,54,44]
temperatures_low = [26,29,35,44,55,64,70,69,61,50,41,32]

#show the average high temperatures in red
plt.plot(months, temperatures_high, 'r')
plt.plot(months, temperatures_high, 'ro')
#show the average low temperaturs in blue
plt.plot(months, temperatures_low, 'b')
plt.plot(months, temperatures_low, 'bo')

#set the labels for the horizontal and vertical axis
plt.xlabel('month')
plt.ylabel('temperature')

#change the month labels from numbers to month names
plt.xticks(months, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') )

#set the tile for the graph
plt.title('Average Monthly Temperatures in New York City')

#make the grid visible
plt.grid(True)

#save the graph in an image file
plt.savefig("problem4_NY.png")
plt.show()


"""

====
QUESTION 1:
Which line would you need to change to modify the title of the graph in the image?
(specify the line number)

ANSWER 1:




====
QUESTION 2:
Which line would you need to change to modify the January average low teperature
to 30 (currently it is 26)?

ANSWER 2:




====
QUESTION 3:
Which line would you need to change to change the color for the average high
temperature from red to yellow?

ANSWER 3:




====
QUESTION 4:
What do you think is the purpose of lines that start wiht a # symbol in the program?

ANSWER 4:




====
QUESTION 5:
The data used in this problem for New York City comes from the floowing website
https://goo.gl/OkvTmh
Use the website to figure out the monthly averate temperatures for the city that you
were born in. If you were born in a place for which the website does not have the
relevant data OR if you were born in NYC, find another city and use its data instead.

Change the name of the file in which the graph is saved to problem4_OTHER.png.

Modify the colors of the plots.

Change the title of the graph to show the name of the appropriate city.

If your modified program produces a new image file, you do not need to provide
any answer (leave the changes in this file so that we can generate the same image).
If you run into problems when modifying the program, tell us what went wrong in the
answer section below.

ANSWER 5:










"""
