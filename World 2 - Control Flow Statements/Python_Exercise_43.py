#Python Exercise 43

"""Develop a program that reads a person's weight and height, calculates their BMI 
and displays their status, according to the table below:
- Below 18.5: Under Weight;
- Between 18.5 and 25: Ideal weight;
- 25 to 30: Overweight;
- 30 to 40: Obesity;
- Over 40: Morbid obesity."""
print('Enter your height and weight.')
h = float(input('Height: '))
m = float(input('Weight: '))
bmi = m / h ** 2

print(f'BMI = {bmi:.2f}Kg/m²', end=' ')

if bmi < 18.5:
    print('UNDER WEIGHT')
elif 18.5 <= bmi < 25:
    print('IDEAL WEIGHT')
elif 25 <= bmi < 30:
    print('OVERWEIGHT')
elif 30 <= bmi < 40:
    print('OBESITY')
else:
    print('MORBID OBESITY')
