'''Crie um programa que leia um numero inteiro e mostra na tela se ele eh par ou impar'''

number = int(input('Digite um número: '))

if (number % 2) == 0:
    print('O número {} é Par'.format(number))
else:
    print('O número {} é Impar'.format(number))
