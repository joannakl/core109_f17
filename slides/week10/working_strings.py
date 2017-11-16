'''

''' 
#exceprt from Little Red Riding Hood
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

word_list = text.split() #splits the text using spaces 

sentence_list = text.replace("\n", " ").split(".")

#print the fiftieth word 
print (word_list[50])

#print the fifth sentence 
print (sentence_list[5].strip()) 