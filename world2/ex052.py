'''
Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
OBS: O numero prime e aquele que e divisivel por um e por ele mesmo.
'''
num1 = int(input('Digite um número: '))
tot = 0
for c in range(1, num1 + 1):
    if num1 % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0O número {} foi divisível {} vezes'.format(num1, tot))
if tot == 2:
    print('Por isso é um número PRIMO!')
else:
    print('Não é um número primpo')
    
