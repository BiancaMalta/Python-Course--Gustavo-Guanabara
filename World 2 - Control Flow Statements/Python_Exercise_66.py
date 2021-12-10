#Python Exercise 66

#Create a program that reads several integers, shows how many numbers were entered and its sum.
sum = cont = 0
n = True
while n:
    n = int(input('Enter a number: [enter 999 to stop]\n'))
    if n == 999:
      break
    sum += n
    cont += 1
print(f'The sum of the {cont} numbers typed is {sum}.')
