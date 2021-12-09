#Python Exercise 38

#Write a program that reads two whole numbers and compares them, showing on the screen a message: 
#The first value is greater!
#The second value is greater! 
#There is no greater value, both are equal! 
print('Enter two integers:')
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another: '))

if n1 > n2:
    print(f'{n1} is greater!')
elif n1 < n2:
    print(f'{n2} is greater!')
else:
    print('They are the same!')
