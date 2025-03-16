#ex008 - Escreva um programa que leia o valor digitado em metros e em centimetros convertidos.
#kilometros, hectometros, decametros e decimetros
medida = float(input("Digite a distancia que deseseja descobrir: "))
cm = medida * 100
mm = medida * 1000
decimetros = medida * 10
decametros = medida / 10
kilometros = medida / 1000
hectometros = medida / 100

print("A distancia digitada e {}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))
print("A distancia digitada equivale a {} decimetros,\nA distancia digitada a {} decametros,\nA distancia digitada equivale a {} quilometros \ne {} hectometros,".format(decametros, decametros, kilometros, hectometros))
