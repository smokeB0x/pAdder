#!/usr/bin/env python

#The script takes each word in passord_temp0.txt and adds the numbers in this script.  
#The output is saved to a file named passord_temp0.txt.txt
import itertools

#Add your digits to this list (leave the first one emty to also include one word without numbers)
digits = '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '123', '1234'
with open('passord_temp0.txt') as file1:
    for line in file1:
        for c in itertools.product(digits, repeat=1):
            number = ''.join(i for i in c)
            print(''.join([line.rstrip(), number]))
