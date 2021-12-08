#Python Exercise 01

#Write a program that reads a person's full name and displays the first and last name.
name = str(input('What is your name? ')).strip().split()
print(f'Nice to meet you! \n'
      f'Your first name is {name[0]} and your last name is {name[len(name) - 1]}')
