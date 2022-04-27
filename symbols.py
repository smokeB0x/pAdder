#!/usr/bin/env python

#The script takes each word in passordliste.txt and adds the symbols in this script.  
#The output is saved to a file named passord_temp1.txt
import itertools

#Add your digits to this list (leave the first one emty to also include one word without numbers)
digits = '', '!', '#', '%', '&', '/', '*', '.', ',', '-', '?', '+', '@', '='
with open('passord_temp1.txt') as file1:
    for line in file1:
        for c in itertools.product(digits, repeat=1):
            number = ''.join(i for i in c)
            print(''.join([line.rstrip(), number]))