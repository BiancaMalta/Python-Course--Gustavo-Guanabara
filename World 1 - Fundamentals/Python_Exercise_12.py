#Python Exercise 12

#Make an algorithm that reads the price of a product and shows its new price, with x% off.
p = float(input('Enter the product\'s price: \n$  '))
dis = float(input('How many % os discount you get?\n'))
print(f'The new price is {(p - p * (dis/100)):.2f}')
