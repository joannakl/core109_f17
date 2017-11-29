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



