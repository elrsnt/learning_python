'''escreva um programa que escreva o salario de um funcionario e calcule o valor do seu aumento
Para salarios superiores a aR$1250, calcule aumento de 10%.
Para salarios inveriores o aumento eh de 15%. '''
salary = float(input('Qual o seu salário? R$'))
if salary >= 1250:
    incresedten = (salary // 100) * 10
    print('Com 10% de aumento do R${:.2f} o salário passará a ser de R${:.2f}'.format(salary,(salary + incresedten)))
else:
    salary <= 1250
    increasefiften = (salary // 100) * 15
    print('Com aumento de 15% do R${:.2f} o salário passará a ser de R${}'.format(salary, (salary + increasefiften)))
