#Crie um programa que leia o nome de uma cidade e diga se ela inicia ou nao com o nome "SANTO"
city = str(input('Em que cidade vc nasceu? ')).strip()
print(city[:5].upper() == 'SANTO')
