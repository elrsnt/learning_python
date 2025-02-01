# O mesmo prograssor. quer sortear a ordem de apresentacao de trabalhos dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacao sera {}'.format(lista))
