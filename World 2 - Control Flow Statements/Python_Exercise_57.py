#Python Exercise 57

#Make a program that reads a person's gender, but only accepts the M or F values. 
#If it's wrong, retype it again until you get a correct value.
gender = str(input('Enter your gender:[M/F]\n')).upper().strip()[0]
while gender != 'M' and gender != 'F':
    print('[ERROR] Invalid option!')
    gender = str(input('Enter your gender:[M/F]\n')).upper().strip()[0]
print(gender)
