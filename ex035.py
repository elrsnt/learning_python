'''ex035
Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao
formar um triangulo. '''
print('\033[7;30;47m-=\033[m' * 30,)
print('Analisando seguimentos de triangulos')
print('\033[0;31m-=\033[m' * 30)
r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triangulos!')
else:
    print('Os seguimentos acima não podem formar um tringulo')
