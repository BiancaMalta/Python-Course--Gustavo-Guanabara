#Python Exercise 42

#Redo EXERCISE 035 adding what kind of triangle will be formed:
 #Equilateral: all sides equal
 #Isosceles: two equal sides
 #Scalene: all different sides
print('Enter the size of three straight lines:')
a = float(input('First straight line: '))
b = float(input('Second straight line: '))
c = float(input('Third straight line: '))

if a + b > c and b + c > a and a + c > b:
    print('The above segments CAN form', end = ' ')
    if a == b == c:
        print('an equilateral triangle.')
    elif a == b or a == c or b == c:
        print('an isosceles triangle.')
    elif a != b and a != c and b != c:
        print('a scalene triangle.')
else:
    print('The above segments CANNOT from a triangle!')
