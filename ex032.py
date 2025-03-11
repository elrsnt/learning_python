'''ex032
faça um programa que leia um no qualquer e mostre se ele Bissexto'''
from datetime import date
year = int(input('Qual ano você quer analisar? '))
if year == 0:
    year = date.today().year
if year  % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))
