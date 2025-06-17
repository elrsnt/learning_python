'''Refaca o desafio 009, mostrando a tabuade de um numero que o usuario escolher
mas agora utilizando laco for'''
#ex009 - Faça um programa leia um numero inteiro qualquer e imprima a sua tabuada na tela.
n = int(input("Digite um número para a tabuada: "))
print("-" * 12)
for c in range(1, 11):
    print("{} x {:2} = {:2}".format(n, c, n*c))
print("-" * 12)
