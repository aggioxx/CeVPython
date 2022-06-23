n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
print('Analisando')

#maior
if n1 > n2 and n1 > n3:
    print('{} maior'.format(n1))
else:
    if n2 > n3:
        print('{} maior'.format(n2))
    else: 
        print('{} maior'.format(n3))

#menor
if n1 < n2 and n1 < n3:
    print('{} menor'.format(n1))
else:
    if n2 < n3:
        print ('{} menor'.format(n2))
    else:
        print('{} menor'.format(n3))
