# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo e calcule e mostre o comprimento da hipotenusa.
from math import hypot
adj = float(input('Qual o comprimento do cateto adjacente? '))
ops = float(input('Qual o valor do cateto oposto? '))
hipo = (adj ** 2 + ops ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipo))
#Using import method
hipoi = hypot(adj, ops)
print('The result using the library math. The hypot is {:.2f}'.format(hipoi))
