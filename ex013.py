#ex013 - Faça um algoritmo que leia o salário de um funcionario e mostre seu no salário com um aumento de 15%
salario_base = float(input('Qual seu salario atual? '))
portagem_aumento = salario_base / 100 * 15
print('Com o salario {} aplicando 15% de aumento o novo salario sera de {}'.format(salario_base, salario_base + portagem_aumento))
