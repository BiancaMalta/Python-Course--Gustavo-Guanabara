#Python Exercise 23

#Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.
num = int(input('Input a number between 0 and 9999: '))
print(f'The number place value is: \n'
      f'Unity: {num % 10} \n'
      f'Ten: {num // 10 % 10} \n'
      f'Hundred: {num // 100 % 10} \n'
      f'Thousand: {num // 1000 % 10}')
