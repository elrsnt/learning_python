#Faca um programa que leia um angulo qualquer e mostre na tela o seno cosseno e tange desse angulo.
from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))
