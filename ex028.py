'''ex0028
Escreava um programa que faca o computador pensar em um numero entre 0 e 5 para
o usuario tentar descobrir qual foi o numero escolhido pelo computador. '''

#Apt
#$sui
#qtum

from random import randint
from time import sleep
computer = randint(0, 5) # exec a randonization between 0 and 5
print('-=-' * 20)
print('Pensando em um numero entre 0 e 5. Adivinhe qual é...')
print('-=-' * 20)
player = int(input('Em qual número eu pensei?' )) # player trying to guess what is the number
print('Processando...')
sleep(3)
if player == computer:
    print('Você acertou')
else:
    print('Você perdeu tente novamente, eu pensei no número {} e não no número {}'.format(computer, player))
