#Python Exercise 15

#Write a program that asks how many miles a rental car has traveled and how many days it has been rented. 
#Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.
print('Rented car!')
days = int(input('For how many days the car has been rented?\n'))
km = float(input('How many kilometers traveled:\n'))
print(f'The total to pay is ${((days * 60) + (km * 0.15)):.2f}')
