'''
Refaca o Desafio 035 dos triangules, Acrescentando o recurso de mostrar o tipo de triangulo sera formado.

- Equilatero: Todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 +reta3 and reta3 < reta1 + reta2:
    print('Os seguimentaos acima Podem Formar um Triangulo ', end='')
    if reta1 == reta2 == reta3:
        print('Equilátero!')
    elif reta1 != reta2 != reta3 != reta1:
        print('Escaleno')
    else:
        print('Isóseles')
else:
    print('Os seguimentos acima Não podem formar um triângulo')
