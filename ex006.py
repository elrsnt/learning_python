#ex006 - Faça um programa que leia o numero e mostre o seu dobro e triplo e a sua raiz quadrada
n1 = int(input('Digite um número: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)
print('O dobro do valor {}, é {}.'.format(n1, n2))
print('O triplo de {} vale {}. \nA raiz de {} é  igual a {:.2f}.'.format(n1, n3, n1, n4))
