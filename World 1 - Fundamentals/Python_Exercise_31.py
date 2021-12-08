#Python Exercise 31

#Develop a program that asks the distance of a trip in km. 
#Calculate the price of the ticket, charging R$ 0.50 per km for trips of up to 200 km and R$ 0.45 for longer trips.
dist = float(input('Enter the distance in kms of the trip: '))

if dist <= 200:
    print(f'The ticket will be R${(dist * 0.50):.2f}')
else:
    print(f'The ticket will be R${(dist * 0.45):.2f}')
