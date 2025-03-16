'''ex033
faca um programa que leia tres numeros e mostre qual e o maior e qual eh o menor
'''
number_one = int(input('Qual é o primeiro numero? '))
number_two = int(input('Qual é o segundo numero? '))
number_tree = int(input('Qual é o terceiro número? '))
#Checking which one is lower
lower = number_one
if number_two < number_one and number_two < number_tree:
    lower = number_two
if number_tree < number_one and number_tree < number_two:
    lower = number_tree
print('The lowest number is {}'.format(lower))
#Checking whick one is higher
higher = number_tree
if number_one > number_tree and number_one > number_tree:
    higher = number_one
if number_two > number_tree and number_two > number_one:
    higher = number_two
print('The highest number is {}'.format(higher))
