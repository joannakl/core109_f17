"""
problem1.py
====

Author:  


Write a program that accepts a potential DNA string from the user.
The program should verify if the string is a valid strand or not. The 
valid DNA strands have to satisfy the following conditions:
- the only legal characters are A, T, C, G (upper and lower case)
- the strand has to start with a start codon ATG (upper or lower case) 
- the strand has to end with one of the stop codons TAA, TGA, TAG 
(upper or lower case)
- the strand's length has to be a multiple of 3 
 

==============
Here are a few sample runs of this program:

Enter the DNA strand: atgctatag
This strand is VALID.

---

Enter the DNA strand: acgtagtag
This is not a valid strand. Valid strands have to start with ATG.

---

Enter the DNA strand: atgctaa
This is not a valid strand. Length of a valid strand should be a multiple of 3.    

---    

Enter the DNA strand: ATGcactgaCGC
This is not a valid strand. Valid strands have to end with TAA or TGA or TAG.

==============

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name at the top of your
  file (above these instructions)
"""

strand = input("Enter the DNA strand: ")

strand = strand.lower() 

lenght = len(strand)

if lenght%3 != 0:
    print ("This is not a valid strand. Length of a valid strand should be a multiple of 3.")
elif strand[0:3] != 'atg':
    print ("This is not a valid strand. Valid strands have to start with ATG.") 
elif not( strand[lenght-3:] == 'taa' or  strand[lenght-3:] == 'tga' or  strand[lenght-3:] )== 'tag' :
    print ("This is not a valid strand. Valid strands have to end with TAA or TGA or TAG.")
else:
    valid = True 
    for c in strand:
        if c not in "atcg":
            valid = False 
            break; 
    if not valid : 
        print ("This is not a valid strand. Valid strands should contains only characters A, T, C, and G.")
    else:
        print("This strand is VALID.")
        
