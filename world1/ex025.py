# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
name = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in name.lower ()))
