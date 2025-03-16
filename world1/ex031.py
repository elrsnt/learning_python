'''ex031
Desenvolva um programa que pergunte a distancia de uma viagem em km calcule o preco da passagem,
cobrando R$0,50 por km para viagens 200km e R$0.45 para viagens longas
'''

distance = int(input('Qual a distância percorrida durante a viagem? '))
if distance <200:
    print('O custo da distância é R${}'.format(distance * 0.50))
else:
    print('O custo da distância foi superior a 200 há um desconto de 5% no valor final de R${}'.format(distance * 0.45))
