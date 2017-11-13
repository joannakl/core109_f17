'''
cmudict is a pronouncing dictionary for north american english words. 
it splits words into phonemes, which are shorter than syllables (e.g. the word 
'cat' is split into three phonemes: K - AE - T). but vowels also have a "stress 
marker": either 0, 1, or 2, depending on the pronunciation of the word
(so AE in 'cat' becomes AE1). the code in the answer counts the stress markers 
and therefore the number of the vowels - which effectively gives the number of 
syllables 
''' 


from nltk.corpus import cmudict
d = cmudict.dict()
# word = "ASIA" 
# 
# print(d[word.lower()])

def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

word = 'sophisticated' 

if word.lower() in d.keys(): 
    print(nsyl(word))
else:
    print("no such word") 
