'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda nao atingiram a maioridade
e quantas ja sao maiores
OBS: Condirar a maior idade de 21 anos
'''
from datetime import date
nowadays = date.today().year
totmaior = 0
totmenor = 0
for person in range(1, 8):
    nasc = int(input('Qual ano que a {} pessoa nasceu? '.format(person)))
    age = nowadays - nasc
    if age >= 21:
        totmaior += 1
    else:
        totmenor +=1
print('{} São menores de idade'.format(totmenor))
print('{} são maiores de idade'.format(totmaior))
