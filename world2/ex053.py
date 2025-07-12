'''Crie um programa que leia uma frase qualquer e diga ela eh um
palindromo, desconsiderando os espacos e acentos.
OBS: Palidromo e uma palavra que tem a mesma escrita para direita e da direita para
esquerda.

Ex:
Apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o lobo
anotaram a data da maratona
'''
word = str(input('Digite uma frase: ')).strip().upper()
words = word.split()
together = ''.join(words)
'''print('Você digitou a frase {}'.format(word))'''
reverse = ''
for letra in range(len(together) - 1, -1, -1):
    reverse += together[letra]
print('O inverso de {} é {}'.format(together, reverse))
if reverse == together:
    print('\nTemos um palindromo')
else:
    print('\nNão é um palindromo')
