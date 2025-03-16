#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Por quantos dias o carro foi alugado? dias'))
kms = int(input('Quantos quilomentros foram rodados? kms'))
custo_dia = dias * 60
custo_km = float(kms * 0.15)
print('O valor do aluguel do carro por {} e {} possuem o custo de R${:.2f}'.format(dias, kms, custo_dia + custo_km))
