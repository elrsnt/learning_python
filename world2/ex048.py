'''Faca um programa que calcule a soma entre todos os numeros pares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500'''
soma = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados tem o total de {} como soma'.format(cont, soma))
