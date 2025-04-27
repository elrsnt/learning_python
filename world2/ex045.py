'''
Crie um programa que faca o computador jogar jokenpo com voce
'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opcoes:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
''')
jogador = int(input('Qual e a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
print('##' * 20 )
print('O Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('##' * 20 )
if computador == 0: # Computador jogou pedra
    if jogador == 0: # Jogador jogou Pedra
        print('Empate')
    elif jogador == 1: #jogador jogou Papel
        print('Jogador vence')
    elif jogador == 2: #jogador jogou tesoura
        print('Computador Vence')
    else:
        print('Jogada invalida')
elif computador == 1: #Computador jogou Papel
    if jogador == 0: # Jogador jogou Pedra
        print('Computador vence')
    elif jogador == 1: #jogador jogou Papel
        print('Empate')
    elif jogador == 2: #jogador jogou tesoura
        print('Jogador vence')
    else:
        print('Jogada invalida')
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('Jogador vence')
    elif jogador == 1: #jogador jogou Papel
        print('Computador Vence')
    elif jogador == 2: #jogador jogou tesoura
        print('Empate')
    else:
        print('Jogada invalida')
