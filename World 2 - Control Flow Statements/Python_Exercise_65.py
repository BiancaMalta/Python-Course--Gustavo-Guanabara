#Python Exercise 65

#Create a program that reads several numbers, displays the mean, highest and lowest values.
nlist = []
c = 'Y'
while c == 'Y':
    n = int(input('Enter a number: '))
    c = input('What to continue [Y/N]? ').upper().strip()[0]
    while c not in "YN":
        c = input('What to continue [Y/N]? ').upper().strip()[0]
    nlist.append(n)

print(f'The average of the {len(nlist)} numbers typed is {sum(nlist)/len(nlist)}')
if max(nlist) != min(nlist):
    print(f'The better is {max(nlist)} the lower is {min(nlist)}.')
else:
    print(f'The numbers are the same.')
    
