#Python Exercise 26

#Make a program that reads a sentence and displays:
# How many times does the letter "A" appear.
# In which position it appears the first time.
# In which position it appears the last time.

a = str(input('Enter a phrase: ')).strip().upper()
print(f'This phrase has {a.count("A")} letters "A". \n'
      f'The first "A" is in the position {a.find("A") + 1} and lasts at {a.rfind("A") + 1}.')
