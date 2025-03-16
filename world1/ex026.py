# Faca um programa que leia uma frase pelo teclado e mostre:
#1 - Quantas vezes a letra "A" aparece.
#2-  Em que posicao ela aparece pela primeira vez.
#3 - Em que posicao ela aparece pela ultima vez
name = str(input('Qual o seu nome? ')).strip()
print(len(name))
print('O seu nome possui {} vezes a letra a'.format(name.count('a')))
print('A primeira vez que a letra a aparece e na posicao {}'.format(name.find('a')))
print('A ultima vez que a letra a aparece e na posicao {}'.format(name.rfind('a')))