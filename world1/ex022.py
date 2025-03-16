#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1 - O nome com todas as letras mausculas
#2 - O nome com todas letras minusculas
#3 - Quantas letras ao todo (sem considerar espacos)
#4 - Quantas letras tem o primeiro nome
n = str(input("Qual e' o seu nome? ")).strip()
print("Analisando seu nome...")
print("Seu nome em letras mausculas".format(n.upper()))
print("Seu nome em letras minusculas".format(n.lower()))
print("O seu nome possui {} letras".format(len(n) - n.count(' ')))
s = n.split()
print("Seu primeiro nome e' {} e contem {} letras".format(s[0], len(s[0])))
