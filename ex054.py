from datetime import date
hj = date.today().year
maior = 0
menor = 0
for c in range (1, 8,):
    nasc = int(input('Digite o ano que a {}ª pessoa nasceu: '.format(c)))
    idade = hj - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Nesse grupo tem {} maiores de idade e {} menores de idade'.format(maior, menor))