l1 = float(input('Digite o lado 1 do triangulo: '))
l2 = float(input('Digite o lado 2 do triangulo: '))
l3 = float(input('Digite o lado 3 do triangulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguementos acima podem formar um triangulo\n')
else:
    print('Os seguementos nao podem formar um triangulo')

if l1 == l2 and l1 == l2 and l2 == l3:
    print('E essas medidas formam um triangulo equilatero (todos os lados iguais)')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('E essas medidas formam um triangulo isoceles (2 lados iguais e 1 diferente)')
else:
    print('E essas medidas formam um triangulo escaleno (todos os lados diferentes)')
