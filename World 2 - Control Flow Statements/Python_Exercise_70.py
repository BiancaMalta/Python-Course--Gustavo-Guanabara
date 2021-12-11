#Python Exercise 70

"""
Create a program that reads the name or price of various products. The program should ask if the user will continue and display:
a) What is the total purchase expense.
b) How many products cost more than $1000.
c) What is the name of the cheapest product.
"""
total = products_1000 = 0
cheapest = ' '
prices = []
while True:
    product = str(input('Enter the product: ')).strip()
    price = float(input('Enter the price: $'))
    prices.append(price)
    total += price
    if min(prices) == price:
        cheapest = product
    if price >= 1000:
        products_1000 +=1
    contin = ' '
    while contin not in 'YN':
        contin = str(input('Want to continue? [Y/N] ')).strip().upper()[0]
    if contin == 'N':
        break
print(f'''The total purchase price was: ${total:.2f}
Amount of products more expensive than $1000.00: {products_1000}
The cheapest product is: {cheapest} 
             that costs: ${min(prices):.2f}''')
