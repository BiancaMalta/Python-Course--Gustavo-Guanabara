#Python Exercise 35

#Develop a program that reads the length of three straight lines and tells the user whether or not they can form a triangle.
print('Input the length of three straight lines: ')
l1 = float(input('First > '))
l2 = float(input('Second > '))
l3 = float(input('Third > '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('The above segments CAN form a triangle!')
else:
    print('The above segments CANNOT form a triangle!')
    
