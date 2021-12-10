#Python Exercise

#Write a program that reads an integer and tells you whether or not it's a prime number.
number = int(input('Enter a number: '))
total = 0

for c in range(1, number+1):
    if number % c == 0:
        total += 1
if total == 2:
    print(f"It's a prime number.")
else:
    print(f"It's not a prime number.")
