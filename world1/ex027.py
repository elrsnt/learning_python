# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguinda o primeiro e o ultimo nome separadamente
# Ex: Ana Maria de Souza R = (primeiro = Ana, ultimo = Souza)
#Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
name = str(input('Qual o seu nome completo? ')).strip()
divide = name.split()
print('O primeiro nome eh igual a {}'.format(divide[0]))
print('O seu ultimo nome eh {}'.format(divide[len(divide)-1]))
