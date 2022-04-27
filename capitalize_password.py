#script to take a list of alfanumeric words and add 
#a capitalized version and a lower case version

#!/usr/bin/env python

file_passordliste = open('passordliste.txt', 'r')           #The file you want to read

for line in file_passordliste:                              #Reads every line of the list
    newline = line.strip()                                  #Remove newlines from each word
    capitalized = newline.capitalize()                      #Capitalize each word
    lower_case = newline.lower()                            #Lower case each word
    
    print(f"{lower_case} \n{capitalized}")                  #Print a lower case and upper case version of the word
    
#To print the output to a file use: 
#<python3 capitalize_password.py > new_passordliste.txt>
