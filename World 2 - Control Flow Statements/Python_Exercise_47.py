#Python Exercise 47

#Create a program that displays all the even numbers in the range from 1 to 50 on the screen.
from time import sleep

r= str(input('Would you like see all even numbers from 1 to 50?[Y/N]')).strip().upper()[0]
if r == "Y":
  for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.25)
else:
  print("Ok,I won't show.")
print('\nAnd that is it...')
