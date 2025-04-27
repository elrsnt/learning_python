'''
A confederacao Nacional de Natacao, precisa de um rograma que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

- Ate 9 Anos: mirim
- Ate 14 anos: Intantil
- Ate 19 anos: Junior
- Ate 20 anos: Senior
- Acima: Master  
'''
age = int(input('Qual a sua idade? '))
if age <= 9:
    print("O Atleta possui {} anos de idade e fará parte do grupo Mirim!".format(age))
elif age < 14:
    print("O atleta possui {} anos de idade e fará parte do grupo Infantil".format(age))
elif age >= 15 and age <= 19:
    print("O atleta possui {} anos de idede e fará parte do grupo Junior".format(age))
else:
    #age => 20
    print("O Atleta possui {} e está acima de vinte anos e seu grupo é Master".format(age))
