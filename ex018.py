import math
ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo {} tem o seno {:.2f}, o coseno {:.2f} e sua tangente {:.2f}'.format(ang, seno, coseno, tang))

