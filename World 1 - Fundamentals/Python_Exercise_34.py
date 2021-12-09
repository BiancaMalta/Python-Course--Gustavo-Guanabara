#Python Exercise 34

#Write a program that asks for an employee's salary and calculates the amount of their raise. 
#For salaries greater than $1250, calculate a 10% raise. For those under and equal, the raise is 15%.
salary = float(input('Enter an employee salary: R$ '))

if salary > 1250.00:
    print(f'The new salary will be R$ {(salary + salary * 0.10):.2f}')
else:
    print(f'The new salary will be R$ {(salary + salary * 0.10):.2f}')
    
