"""
problem1.py
====

Author:  


The following program begins by defining a variable called text that contains
the first few paragraphs of the Little Red Riding Hood. 

Write the program that determines the number of words and the counts of each of the following
punctuation marks: periods, question marks, exclamation marks, commas, colons, semicolons, single
quotes, double quotes. 
 
Note, your program should still work if the text variable is changed to some other text. 

==============
Here is a run of this program:
    
Text has 170 words.
Text has 10 periods.
Text has 0 question marks.
Text has 0 exclamation marks.
Text has 5 commas.
Text has 0 colons.
Text has 1 semicolons.
Text has 1 single quotes.
Text has 2 double quotes.

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

text="""There was once a sweet little maid who lived with her father and 
mother in a pretty little cottage at the edge of the village. At the
further end of the wood was another pretty cottage and in it lived her
grandmother.

Everybody loved this little girl, her grandmother perhaps loved her
most of all and gave her a great many pretty things. Once she gave her
a red cloak with a hood which she always wore, so people called her
Little Red Riding Hood.

One morning Little Red Riding Hood's mother said, "Put on your things
and go to see your grandmother. She has been ill; take along this
basket for her. I have put in it eggs, butter and cake, and other
dainties."

It was a bright and sunny morning. Red Riding Hood was so happy that
at first she wanted to dance through the wood. All around her grew
pretty wild flowers which she loved so well and she stopped to pick a
bunch for her grandmother."""

words = text.split()

print("Text has", len(words), "words.")


dots = text.split(".")
print("Text has", len(dots)-1, "periods.") 

question_marks = text.split("?")
print("Text has", len(question_marks)-1, "question marks.")

exclamation_marks = text.split("!")
print("Text has", len(exclamation_marks)-1, "exclamation marks.")

commas_count = text.count(",")
print("Text has", commas_count, "commas.")  

colons_count = text.count(":")
print("Text has", colons_count, "colons.")  

semicolons_count = 0 
single_quotes_count = 0 
double_quotes_count = 0

for c in text: 
    if c == ';' :
        semicolons_count += 1
    elif c == "'" :
        single_quotes_count += 1
    elif c == '"' :
        double_quotes_count += 1 

print("Text has", semicolons_count, "semicolons.")  

print("Text has", single_quotes_count, "single quotes.")

print("Text has", double_quotes_count, "double quotes.")  

