'''
Desenvolva um programa que leia o nome, idade  e sexo
 de 4 pessoas. No final do programa, mostre:
 1 - A media de idade do grupo.
 2 - Qual o nome do homem mais velho
 3 - Quantas mulheres tem menos de 20 anos.
'''
sumage = 0
media = 0
olderman = 0
oldermanname = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {} Pessoal ------'.format(p))
    name = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo [F/M]? ')).strip()
    sumage += idade
    if p == 1 and sexo in 'Mm':
        olderman = idade
        oldermanname = name
    if sexo in 'Mm' and idade > olderman:
        olderman = idade
        oldermanname = name
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = sumage / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(olderman, oldermanname))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
