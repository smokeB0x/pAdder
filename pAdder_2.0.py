#!/usr/bin/env python

import itertools

def capitalize_password():
    """
    Function to return two versions of each password. One capitalized and one uncapitalized
    """
    capitalized_passwords = []
    with open('passwords.txt', 'r', encoding='utf-8-sig') as file_passordliste:
        for line in file_passordliste:
            newline = line.strip()
            capitalized = newline.capitalize()
            lower_case = newline.lower()
            capitalized_passwords.append((lower_case, capitalized))
    return capitalized_passwords            

    

def add_numbers(password):
    """
    Function to add the numbers in the list to each password
    """
    digits = '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '123', '1234'
    passwords_with_numbers = []
    for c in itertools.product(digits, repeat=1):
        number = ''.join(i for i in c)
        passwords_with_numbers.append((password[0] + number, password[1] + number))
    return passwords_with_numbers

def add_symbols(password):
    """
    Function to add the symbols in the list to each password
    """
    symbol_list = '', '!', '#', '%', '&', '/', '*', '.', ',', '-', '?', '+', '@', '='
    passwords_with_symbols = []
    for c in itertools.product(symbol_list, repeat=1):
        number = ''.join(i for i in c)
        passwords_with_symbols.append((password[0] + number, password[1] + number))
    return passwords_with_symbols

def main():
    passwords = capitalize_password()
    final_passwords = []

    for password in passwords:
        # Generate passwords with numbers added
        passwords_with_numbers = add_numbers(password)
        
        # Generate passwords with symbols added
        for password_with_numbers in passwords_with_numbers:
            passwords_with_symbols = add_symbols(password_with_numbers)
            final_passwords.extend(passwords_with_symbols)
            
    # Write the final list of passwords to a file named "final_passwords.txt"
    with open("final_passwords.txt", "w", encoding="utf-8-sig") as file:
        for password in final_passwords:
            file.write(password[0] + "\n")  # Write the lowercase version
            file.write(password[1] + "\n")  # Write the capitalized version



if __name__ == "__main__":
    main()    
