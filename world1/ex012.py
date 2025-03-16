#ex012 - Faça um algoritmo que leia o preço de um produto e mostre o preço com 5 por cento de desconto.
preco = float(input('Qual o preco do produto? R$'))
valor_final = preco - (preco / 100 * 5)
print('O valor era de {:.2f}, com 5% de desconto passa para {:.2f}'.format(preco, valor_final))
