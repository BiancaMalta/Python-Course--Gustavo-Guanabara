#Python Exercise 48

#Write a program that calculates the sum of all odd numbers that are multiples of three and that identifies itself in the range from 1 to 500.
from time import  sleep
sum = 0
count = 0
r = str(input('''Would you like see all the odd numbers that are multiples of three
in 1 to 500 and the sum of them?[Y/N]''')).strip().upper()[0]

if r == "Y":
    for c in range(3, 501, 2):
        if c % 3 == 0:
            print(c, end=' ')
            sleep(0.1)
            sum += c
            count += 1
    print(f"\nThere are {count} numbers\n"
          f"and the sum is {sum}")
else:
    print("Ok,I won't show.")
    
