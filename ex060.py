#import math
#num = int(input('Digite um numero para calcular seu fatorial: '))
#print(math.factorial(num))\

num = int(input('Digite um numero para calcular seu fatorial: '))
a = num
fac = 1 
while a > 0:
    fac *= a
    a -= 1
print(fac)
