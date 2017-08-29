"""
problem3.py
===


It is interesting when programs behave in a different way in response
to the input provided by the user.

Programming languages always have some way of performing one set of instructions
or another depending on some condition.

Run this program and answer the questions below.

"""


name = input("Hello! What is your name? ")
num_of_languages = input("How many programming languages do you know? ")
num_of_languages = int( num_of_languages )

if ( num_of_languages == 0 ):
    print (name + ", you are about to learn your first programming language!")
else:
    print (name + ", I think you are in a wrong class! Talk to Joanna about this.")



"""

====
QUESTION 1:
Do think that all of the lines of code (lines 17 - 24) are executed by the computer
when you run the program? Explain your answer.

ANSWER 1:



====
QUESTION 2:
Notice that the `print` instructions after the `if ...` and `else ...` lines
are indented. What happens when you try to remove the intent?

ANSWER 2:



====
QUESTION 3:
On line 19, the instruction is:
num_of_languages = int( num_of_languages )
What do you think this does? Does the program behave the same if you remove this line?

ANSWER 3:



====
QUESTION 4:
Users often make mistakes when providing information to the computer. What
happens when you enter a negative number when answering the question about programming
languages? What happens if you enter the number as text, instead of the number?

ANSWER 4:






"""