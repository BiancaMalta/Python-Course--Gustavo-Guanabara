#Python Exercise 55

#Make a program that reads the weight of five people and shows which was the highest and lowest weight read.
weight_list = []
for c in range(1, 6):
    weight = float(input(f'What is the weight of person {c}?'))
    weight_list.append(weight)
print(f'The heaviest is = {max(weight_list)}')
print(f'The lightest is = {min(weight_list)}')
