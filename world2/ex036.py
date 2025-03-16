'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o Salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestacao mensal, sabendo que nao pode exceder #0% do salario ou entao o emprestimo
sera negado. '''
home_value = float(input('Qual o valor da casa que deseja comprar? R$'))
salary = float(input('Qual o valor do seu salario atual? R$'))
anos = int(input('Em quantos anos voce deseja liquidar o financiamento?' ))
prestacao = home_value / (anos * 12)
mininum = salary * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestacao sera de R${:.2f}'.format(home_value, anos, prestacao))
print('valor da casa {} salario {} periodo de pagamento {} anos'.format(home_value, salary, anos))
if prestacao <= mininum:
    print('O emprestimo pode ser Concedido!')
else:
    print('O Emprestimo sera negado!')