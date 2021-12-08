#Python Exercise 01

#Create a program that reads the name of a city and tells you whether or not it starts with the name "SANTO".
city = str(input('What city are you live? ')).strip().upper()
print(f'The name of your city starts with the word "SANTO"? {"SANTO" in city[0:6]}')
