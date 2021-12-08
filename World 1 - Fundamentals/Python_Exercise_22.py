#Python Exercise 22

#Create a program that reads a person's full name and displays:
# The name in all capital letters
# The name with all lowercase.
# How many letters in all (not including spaces)
# How many letters has the first name. 
name = str(input('Enter your full name: ')).strip()
print(f'Your name in uppercase is {name.upper()} and in lowercase is {name.lower()}.\n'
      f'Your full name had {len(name) - name.count(" ")} letters.\n'
      f'And your first name had {len((name.split())[0])} letters on total.')
