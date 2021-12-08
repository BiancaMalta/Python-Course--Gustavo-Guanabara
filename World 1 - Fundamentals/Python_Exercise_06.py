#Python Exercise 06

#Create an algorithm that reads a number and shows its double, triple and the square root.
n = float(input('Insert any number: '))
print(f'The double of {n:.2f} is {(n * 2):.2f} \n'
      f'The triple is {(n * 3):.2f} \n'
      f'And the square root is {(n ** (1/2)):.2f}')
