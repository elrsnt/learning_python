#ex010 - Crie um programa que leia quantos dinheiro a pessoa tem na carteira e mostre quandos dolares ela pode comprar considere U$$1.00=R$3.27
amount = float(input("Quanto dinheiro vc tem na carteira para comprar dollar? R$"))
quot = float(input("Qual a cotacao atual do dollar? U$"))
dollar_qt = amount / quot
print("Com o {:.2f} voce pode comprar {:.2f} dolares".format( amount, dollar_qt))
