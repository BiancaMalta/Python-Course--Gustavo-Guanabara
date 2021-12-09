#Python Exercise 40

#Create a program that reads two grades from a student and calculates their average, showing:
# Average below 5.0: FAILED
# Average between 5.0 and 6.9: RECOVERY
# Average 7.0 or above: APPROVED
print('Enter the student grades:')
n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
average = (n1 + n2) / 2

if average < 5:
    print('FAILED')
elif average >= 5 and average < 6.9:
    print('RECOVERY')
else:
    print('APPROVED')
