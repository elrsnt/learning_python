'''ex0029
escreva um programa que leia a velocidade de um carro.
se ele ultrapassr 80kms, mostre uma mensagem dizendo que ele foi multado.
'''
speed = float(input('Qual a velocidade do carro? '))
price  = (speed-80) * 7
if speed <80:
    print('Velocidade compatível com a via')
else:
    print('Veiculo multado em R${:.2f} por estar cima do limite de 80'.format(price))
