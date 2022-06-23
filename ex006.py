import math


#2x, 3x e raiz quadrada do valor digitado   
import math
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
rq = math.sqrt(n)
print ('O dobro {}\n o triplo {}\n e a raiz quadrada {}'.format(d, t, rq))
#outras formas de fazer raiz quadrada
    #rq = n ** 0.5
    #rq = math.pow(n, 1/2)