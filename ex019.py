# Um professor quer soterar um dos seus alunos para apagar o quadro.
# Faca um programa que ajude ele, lendo o nome dele e escrevendo o nome do escolhido.
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(lista))
