#calculo hiopotenusa
import math
co = float(input('Insiraa o comprimento do cateto oposto (em cm): '))
ca = float(input('Insira o comprimento do cateto adjascente (em cm): '))
calc = (co ** 2) + (ca ** 2)
res = math.sqrt(calc)
#hi = math.hypot(ca, co)
print('A hipotenusa tem {}cm'.format(res))

