#ex011 - Faça um programa que leia a largura e a altura de uma parede em metros calcule a sua area e a quantidade de tinta que será ultilizada sabendo que cada litro de tinta pinta uma area de 2 metros quadrados.
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
print('Sua parede tem a dimensao de {:.2f}x{:.2f} e a sua area de {:.2f}metros quadrados'.format(largura,altura, area))
tinta = area / 2
print('Pare realizar a pintura voce vai precisar de {}'.format(tinta))
