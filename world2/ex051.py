'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA (Progressa Aritimetica).
No final, mostre os 10 primeiros termos dessa progressa.
'''
first = int(input('Digite um termo: '))
second = int(input('Digite a razao: '))
decimo = first + (10 - 1) * second
for c in range(first, decimo + second, second):
    print("{}".format(c), end='-> ')
print('Acabou!')
