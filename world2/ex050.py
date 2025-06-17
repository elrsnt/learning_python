'''Desenvolva um programa que leia seis numeros inteiros e mostre a some apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o'''
cont = 0
sum = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '.format(c)))
    if num % 2 == 0: #valida se o numero eh par
        sum += num # identado a esquerda para entrar dentro do laco.
        cont += 1
print('Voce informou {} numeros pares e a soma entre eles foi {}'.format(cont, sum))
