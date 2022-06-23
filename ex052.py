tot = 0
num = int(input('Digite um numero inteiro: '))
for c in range (1, num + 1):
    if num % c == 0:
       tot += 1
if tot > 1 and tot == 2:
    print('O numero {} è primo'.format(num))
else:
    print('O numero {} nao è primo'.format(num))