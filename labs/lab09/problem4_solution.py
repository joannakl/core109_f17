"""
problem4.py
====

Author:  


Write a program that performs the Dale-Chall Readability Test on a given text. 

Recall that for this test you will need 
* the list of 3000 'easy' words
* the total number of words in the text
* the total number of sentences in the text 

(See this week's slides for the formula.)

You can read the file containing all of the easy words at 
https://joannakl.github.io/core109_f17/slides/week10/easy_words.txt

The program below starts with several url's for books. 
Your program should run with one of those url's at a time. 
(Feel free to add your own as well.)  


==============
Here are a few sample runs of your program:
    


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

import urllib.request

# read the text 

# War and Peace
url = "http://www.gutenberg.org/files/2600/2600-0.txt"
response = urllib.request.urlopen(url)
# read data from URL as a String, making sure
# that the String is formatted as a series of ASCII characters
data = response.read().decode('utf-8')
book_words = data.split() 

# read the easy words 
url_words = "https://joannakl.github.io/core109_f17/slides/week10/easy_words.txt"
response = urllib.request.urlopen(url_words)
easy_words_text = response.read().decode('utf-8')

easy_words = easy_words_text.split() 


# count total number of words 
words_total = len(book_words)

# count hard words 
hard_words_total = 0
for word in book_words:
    if not easy_words.find(word) :
        hard_words_total += 1 
        
# count sentences
data = data.replace("! ", ". ")
data = data.replace("? ", ". ")
data = data.replace("? ", ". ")
book_sentences = data.split(".") 

