#Python Exercise 63

#Write a program that reads an integer 'x' and displays the 'x' elements of a Fibonacci Sequence on the screen.
n = int(input('Enter how many Fibonacci sequence elements you want:\n'))
stop = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')

while stop != n:
    t = t1 + t2
    print(f' → {t}', end='')
    t1 = t2
    t2 = t
    stop += 1
