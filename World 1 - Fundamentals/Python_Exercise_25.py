#Python Exercise 25

#Create a program that reads a person's name and tells them if they have "Kyle" in their name.
name = str(input('Enter your full name: ')).strip().upper().split()
print(f'Does your name have "KYLE"? {"KYLE" in name}')
