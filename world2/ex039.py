'''
Faca um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idede

- Se ele ainda vai se alistar ao serviço militar
- se e hora de se alistar
- se ja passou do tempo do alistamento

Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
source_year = int(input('Digite o ano do seu nascimento: '))
year = date.today().year
age = year - source_year
print('Quem nasceu em {} tem anos em {}'.format(source_year, age, year))
if age == 18:
    print('Você precisa se alistar neste ano')
elif age < 18:
    amount = 18 - age
    print('Ainda faltam {} oara o alistamento'.format(amount))
else:
    amount = age - 18
    age > 18
    print('Vce ja deveria ter se alistado a {} anos'.format(amount))
