'''Desenvolva uma logica que leia o peso de a altura de uma pessoa, calcule seu IMC e
mostre seu status, de acirdi com a tabela abaixo:

- Abaixo de 18.5: abaixo do Peso
- Entre 18,5 e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obsidade
- AcimA DE 40 obsidade morbida.
'''
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso /  ( altura **2 )
print("Voce possui o peso {} e a altura {} e possui o IMC de {:.1f}, ".format(peso, altura, imc), end='')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Parabéns, voce esta na faixa de peso ideal')
elif 25 <= imc < 30:
    print('Voce esta em Sobreso')
elif 30 <= imc < 40:
    print('Você está em Obsidade')
elif imc >= 40:
    print('Voce esta em Obesidade Mórbida, cuidado!')
