l1 = float(input('Digite o lado 1 do triangulo'))
l2 = float(input('Digite o lado 2 do triangulo'))
l3 = float(input('Digite o lado 3 do triangulo'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguementos acima podem formar um triangulo')
else:
    print('Os seguementos nao podem formar um triangulo')