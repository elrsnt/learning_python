'''
Faca um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos. 
'''
meior = 0
menor = 0
for person in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa? '.format(person)))
    if person == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
