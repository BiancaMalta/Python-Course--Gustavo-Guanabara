#Python Exercise 37

#Write a program that reads any integer and asks for the user to choose which conversion base will be:
# 1 for binary
# 2 for octal
# 3 hexadecimal
print('Numeric Base Converter')

number = int(input('Enter an integer for conversion: '))
base = int(input('''Now select your option: 
[1] to binary
[2] to octal
[3] to hexadecimal
 '''))
if base == 1:
    print(f'In binary is {bin(number)[2:]}')
elif base == 2:
    print(f'In octal is {oct(number)[2:]}')
elif base == 3:
    print(f'In hexadecimal is {hex(number)[2:]}')
else:
    print('[ERROR] Invalid values!')

