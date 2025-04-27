'''
Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma
mensagem no final, de acordo com a media atingida

- Media abaixo de 5.0: Reprovado
- Media entre 5.0 e 6.9: Em recupacao.
- Media 7.0 ou superior: Aprovado
'''
first = float(input('Digite a sua primeira nota: '))
second = float(input('Digite a segunda nota: '))
media = (first + second) / 2
print('Com a primeira nota sendo {:.1f}, e a segunda nota sendo {:.1f}, a média do aluno é {:.1f}'.format(first, second, media))
if media < 5.0:
    print('O Aluno reprovado, pois a média de notas coma seguinte pontuação {:.1f}. Reprovado!'.format(media))
elif media == 5.0 or media < 6.9:
    print('O aluno em recuperação, pois obteve a média de notas coma seguinte pontuação {:.1f}. Recuperação!'.format(media))
else:
    media >= 7
    print('O aluno está aprovado, pois obteve a média de notas com seguinte pontução {:.1f}. Parabéns!!! você está aprovado'.format(media))
