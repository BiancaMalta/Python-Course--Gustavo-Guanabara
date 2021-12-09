#Python Exercise 44

"""
Develop a program that calculates the amount to be paid for a product, considering its normal price and payment terms:
- cash/check: 10% discount
- cash on the card: 5% discount
- up to 2x on the card: regular price
- 3x or more on the card: 20% interest
"""
price = float(input('Enter the product costs: $'))
form = int(input('''Choose the form of payment:
[1] Cash/check
[2] Credit Card
'''))

if form == 1:
    price -= price * 0.1
    print(f'Price: ${price:.2f}')
elif form == 2:
    installment = int(input('''Choose the installment:
    [1] In Cash 
    [2] Up to 2x
    [3] Up to 3x or more
    '''))
    if installment == 1:
        price -= price * 0.05
        print(f'Price: ${price:.2f}')
    elif installment == 2:
        print(f'Price: ${price:.2f} (${price / 2:.2f} per month)')
    elif installment == 3:
        price += price * 0.2
        time = int(input('For how many months? '))
        if time > 2:
            print(f'Price: ${price:.2f} (${price / time:.2f} per month during {time} months)')
        else:
            print('[ERROR] 3x or more !')
    else:
        print('[ERROR] Only 1, 2 or 3!')
else:
    print('[ERROR] Only 1 or 2!')
