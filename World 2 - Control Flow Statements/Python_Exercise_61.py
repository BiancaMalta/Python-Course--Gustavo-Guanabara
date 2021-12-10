#Python Exercise 61

#Read the first term and reason from an arithmetic progression and show the first 10 terms of the progression using the while structure.
n1 = int(input('Enter a number: '))
reason = int(input('Reason: '))
nf = n1 + (10 - 1) * reason

while n1 != nf+reason:
    print(f' {n1} ', end='')
    n1 += reason
    
