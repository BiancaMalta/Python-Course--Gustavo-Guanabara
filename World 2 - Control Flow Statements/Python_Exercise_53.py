#Python Exercise 53

#Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.
phrase = str(input('Enter a phrase or word and know if it is a PALINDROME:')).strip().upper().split()
phrasetog = ''.join(phrase)
if phrasetog == phrasetog[::-1]:
    print(f'{phrase} is a PALINDROME.')
else:
    print(f'{phrase} is not a PALINDROME.')
