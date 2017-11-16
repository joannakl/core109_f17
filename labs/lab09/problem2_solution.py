"""
problem2.py
====

Author:  
    
In this program you will be reading data from the web. You can go through the 
module that covers that topic at https://cs.nyu.edu/elearning/CSCI_UA_0002/module09.php 
The class slides for this week also have instructions on how to do this. 

Write a Python program that asks the user to type in a word in English. 
Determine if that word is one of the most 100 popular English words. 
Here is a link to a data file on the web which contains this information:
    https://joannakl.github.io/core109_f17/slides/week10/popular_words_English.txt 
The words in this file are sorted in alphabetical order.

Here's how to get started:

* Read in the data and print it out (use the sample code above to get started) - use the 
 code from the slides to read the text of the file from the url above.
* Next, split the data using the correct separator character (hint: there is a 
line break between each word).
* Finally, use appropriate built-in functions and list methods to determine if the 
user's word is contained in the list that you generated in the previous step.


Restriction:
    You are not allowed to use any loops!!!!!

==============
Here are a few sample runs of your program:
    
What word would you like me to search for? 
here
Your word is one of the 100 most popular words!

--

What word would you like me to search for? 
college
Sorry, your word is not one of the most popular words.

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""
import urllib.request

# where should we obtain data from?
url = "https://joannakl.github.io/core109_f17/slides/week10/popular_words_English.txt"

# initiate request to URL
response = urllib.request.urlopen(url)

# read data from URL as a String, making sure
# that the String is formatted as a series of ASCII characters
data = response.read().decode('utf-8')
    
# let's split our data into a list
split_data = data.split("\n")

# get the user to pick a word
word = input("What word would you like me to search for? ")

# determine if user's word is in our list or not
if word in split_data:
    print("Your word is one of the 100 most popular words!")

else:
    print("Sorry, your word is not one of the most popular words.")
