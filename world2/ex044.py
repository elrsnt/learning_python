'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preco normal e condicao de pagamento.
- A vista dinheiro/cheque: 10% desconto
- A vista no cartao: 5% de desconto.
- em ate 2x no cartao preco normal
- 3x ou mais no cartao 20% de juros

'''
print('{:=^40}'.format(' Lojas do Elismar '))
price = float(input('Qual o valor total da compra? R$'))
print('''
[ 1 ] - A vista dinheiro/cheque: 10% desconto
[ 2 ] - A vista no cartao: 5% de desconto.
[ 3 ] - em ate 2x no cartao preco normal
[ 4 ] - 3x ou mais no cartao 20% de juros
''')
option = int(input('Qual a opcao? '))
if option == 1:
    total = price - (price / 100 * 10 )
elif option == 2:
    total = price - (price / 100 * 5)
elif option == 3:
    total = price
    split = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}, Sem juros'.format(split))
elif option == 4:
    total = price + (price / 100 * 20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f}, Com juros de 20%'.format(totparc, parcela))
else:
    total = price
    print('Opcao invalida de pagamento tente novamente.')
print('Sua compra no valor total de R${:.2f} vai custar R${:.2f}'.format(price, total))
