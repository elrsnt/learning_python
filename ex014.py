#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Qual a temperatura em celsius? "))
fahrenheit = float(input("Qual a temperatura em fahrenheit? "))
print("A temperatura em graus fahrenheit representa {:.2f}graus fahrenheit".format(( celsius * 9 / 5) + 32))
print("A temperatura em graus celsius representa {:.2f}graus centigrados".format(( fahrenheit - 32 ) * 5 / 9))
