#Python Exercise 10

#Create a program that reads how many Reais a person has in their wallet and shows how many Dollars, Euros, Yen and Pound sterling they can buy.
eur = 6.34
dol = 5.61
yen = 0.049
lib = 7.41
c = float(input('How many Reais do you have in your pocket?\nR$ '))
print(f'With R$ {c:.2f} you can buy: \nUSD$ {(c/dol):.2f}'
      f' \nEUR$ {(c / eur) :.2f}'
      f'   \nJPY$ {(c / yen) :.2f}'
      f'  \nGBP$ {(c / lib) :.2f}')
