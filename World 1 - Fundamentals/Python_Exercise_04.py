#Python Exercise 04

#Make a program that reads anything typed and displays its primitive type and all possible information about it on the screen.
val = input('Enter anything: ')
print(f'Value type is: {type(val)}')
print(f'Only spaces? {val.isspace()}')
print(f'Is it a number? {val.isnumeric()}')
print(f'Is it alphabetic? {val.isalpha()}')
print(f'Is it alphanumeric? {val.isalnum()}')
print(f'Is it Uppercase? {val.isupper()}')
print(f'Is it Lowercase? {val.islower()}')
print(f'Is it Title? {val.istitle()}')
