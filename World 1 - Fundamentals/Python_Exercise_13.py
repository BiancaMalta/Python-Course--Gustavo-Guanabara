#Python Exercise 13

#Make an algorithm that reads an employee's salary and shows their new salary, with a 15% increase.
s = float(input('Please insert the salary?\n$'))
i = float(input('Now insert the percentage of increase?\n'))
print(f'The salary {s:.2f} with the promotion of {i}% will be {(s + s * (i / 100)):.2f}')
