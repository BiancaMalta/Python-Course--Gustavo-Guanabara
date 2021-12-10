#Python Exercise 51

#Develop a program that reads the first term and reason of a PA. At the end, show the first 10 terms of this progression.
n1 = int(input('Enter a number: '))
reason = int(input('Reason of a PA: '))
nf = n1 + (10 - 1) * reason

for c in range(n1, nf + reason, reason):
    print(c, end = " ")
