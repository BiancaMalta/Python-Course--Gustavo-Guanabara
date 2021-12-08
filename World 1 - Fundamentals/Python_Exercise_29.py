#Python Exercise 01

#Write a program that reads the speed of a car.
#If he goes over 80km/h, show a message saying he was fined. 
#The fine will cost R$7.00 for each Km over the limit.
s = float(input('Enter car speed [Km/h]: '))

if s > 80:
    print(f'You were fined!\n'
          f'You have to pay a ${((s - 80) * 7):.2f} fine!')
print('Have a good day! Drive carefully!')
