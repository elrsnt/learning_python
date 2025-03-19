'''
Escreva um progrma que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor e maior
- O segundo valor e maior
- Nao existe valor maior, os dois sao iguais. 
'''
first = int(input('Insira um valor: '))
second = int(input('Insira outro valor: '))
if first > second:
    print('O primeiro valor "{}" é maior que o segundo valor "{}"'.format(first ,second))
elif second > first:
    print('O segundo valor "{}" é maior que o primeiro valor "{}"'.format(second, first))
else:
    first == second
    print('O primeiro valor {} é igual ao segundo valor {}'.format(first, second))
