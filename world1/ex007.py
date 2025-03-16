#ex007 - Desenvolva um programa que leia a nota de um aluno e a calcule a sua media
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
# Devido a ordem de precedencia, necessario incluir os parenteses, para que a divisao seja realizada primeiro.
m = (n1 + n2) / 2
#Usando as regras algebrecas de arredondamento esta sendo utilizado apenas um campo apos a virgula para termos o resultado 1.75 virar 1.80 e caso seja necessario e possivel alterar para duas casas decimais.
print('A media entre {:.1f} e {:.1f} e igual a {:.1f}'.format(n1, n2, m))
