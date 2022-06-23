num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu pela primeira vez na posição {num.index(3)+1}')
else:
    print('Não foi digitado o número 3')
print('Os valores pares digitados foram:')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
