#para importar uma biblioteca inteira usamos o "import lib"
#para importar somente o que precisamos usar de uma biblioteca usa se "from lib import 'funcionalidade necessaria'"
# Exemplo
# "import math" vai importar toda a biblioteca completa
# funcionalidade
# ceil, (para arrendodar para cima).
# floor (arrendondar para baixo).
# trunc (truncate para quebrar o numero da virgula para direita)
# pow (potencia funciona de forma semelhante as duas ** que faz a pontencia)
# sqrt (raiz quandrada)
# factorial (calculo fatoria)
# nesse caso o import math vai incluir todos estes operadores.
# from math import srqt
# Para importar duas funcionalidades eh possivel utilizar
# from math import sqrl, ceil
from math import sqrt, floor
num = int(input(' Digite um numero: '))
raiz = sqrt(num)
print('A rais de {} e igual a {}'.format(num, floor(raiz)))
