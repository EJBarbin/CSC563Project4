#!/usr/bin/env python 
import sys
#--- get all lines from stdin --- 
# ` ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } \ | ; : ' " , . < > / ? "
for line in sys.stdin:
    #--- remove leading and trailing whitespaces ---
    line = line.strip()
    #--- split the line into words ---
    words = line.split()
    #--- output tuples [word, 1] in tab-delimited format ---
    for word in words:
        # remove symbols at the beginning or at the end of the word
        stripped = word.strip('`~@$%*()-_=+[]\{\}|;:,.<>?!#^&\'\"\\/')
        if stripped != "":
            print('%s\t%s' % (stripped , "1"))
            