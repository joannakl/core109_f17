"""
problem4.py
====

Author:  


Write a program that counts occurrences of all letters in a book. You should NOT be 
keeping counters for every letter. Instead, you should work with two lists: one that contains the letters and one 
that contains the counts. Your `for` loops will need to iterate over indexes in these two arrays.

The program should open a book given a specific URL (some example URL's are
listed below). It should produce the results with counts of all of the letters 
as well as the sum of all the letters (this does not include the spaces, punctuation marks, 
digits or any other non-letter characters). Make sure that both upper and lowercase letters are
counted. 
    


==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

import urllib.request

# read the text 


# Romeo and Juliet (English) 
# url="http://www.gutenberg.org/cache/epub/1513/pg1513.txt" 

# Romeo and Juliet (Polish) 
# url="http://www.gutenberg.org/files/27062/27062-0.txt" 

# Romeo and Juliet (German) 
# url="http://www.gutenberg.org/cache/epub/6996/pg6996.txt" 

# Romeo and Juliet (Tagalog) 
# url="http://www.gutenberg.org/cache/epub/15418/pg15418.txt" 


response = urllib.request.urlopen(url)
# read data from URL as a String, making sure
# that the String is formatted as a series of ASCII characters
data = response.read().decode('utf-8')
data = data.lower()

# list of all letters initialized to zero counts 
letters = [0] *( ord('z') - ord('a')+1)


for let in data:
    if let.isalpha():
        ind = ord(let)-ord('a') 
        
        #print (ind, let)
        if ind < len(letters):
            letters[ind] =letters[ind] + 1;   

total =  sum(letters)
print ("Total number of letters:", sum(letters) )


for index in range( len(letters)) :
    print ( chr(ord('a')+index), ": ", letters[index], sep="") 
    
