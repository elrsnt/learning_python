#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tua sua porcao inteira.
# Ex: digite um numero 6.127 o numero tem a portacao inteira 6
from math import trunc
number = float(input('Digite um numero: '))
print('O numero digitado foi {:.3f} e a sua porcao inteira {}'.format(number, trunc(number)))
#Or use that way
print('O numero digital {} corresponde a porcao de {} "using default functions" '.format(number, int(number)))
