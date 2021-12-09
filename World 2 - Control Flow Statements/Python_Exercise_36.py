#Python Exercise 36

#Write a program to approve the bank loan for a home purchase.
#The program will ask the value of the house, the buyer's salary and in how many years he will pay.
#Calculate the amount of the monthly payment knowing that it cannot exceed 30% of the salary or else it will be denied. 
print ('Welcome to the bank loan simulator!')
house_price = float (input('Enter house price: $'))
years = float (input ('How many years do you pretend to divide:'))
salary = float (input('Enter your salary:'))
payment = house_price / (years * 12)

if payment >= (salary * 0.3):
      print ('Sorry, unfortunately your loan was denied!')
else:
      print (f'Congratulations! Your loan has been approved with the monthly payment of ${payment:.2f} ')
