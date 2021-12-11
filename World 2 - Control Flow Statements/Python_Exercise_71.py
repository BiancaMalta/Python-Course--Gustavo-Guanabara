#Python Exercise 71

"""
Create a program that simulates the operation of an ATM.
In the beginning, ask the user what will be the amount to be withdrawn (integer) 
and the program will inform how many bills of each amount will be delivered.
Note: Consider that the cashier has bills of 50, 20, 10, and 1.
"""
money = int(input('How much do you want to withdraw? $'))
total = money
bill = 50
total_bills = 0
while True:
    if total >= bill:
        total -= bill
        total_bills += 1
    else:
        if total_bills != 0:
            print(f'{total_bills} bills of {bill}')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        total_bills = 0
        if bill == 0:
            break
                  
