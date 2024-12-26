#nome = input('Qual eh o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma {}, o produto eh {} e a divisao eh {:.3f}'.format(s, m ,d), end=' ')
print('Divisao inteira {} e pontencia {:.3f}'.format(di, e))
