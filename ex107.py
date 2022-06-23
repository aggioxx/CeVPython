import moeda

num = float(input('Digite um valor: '))
aum = int(input('Digite o aumento percentual: '))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O aumento de {aum}% de {num} é {moeda.aumentar(num, aum)}')
print(f'A diminuição de {aum}% de {num} é {moeda.diminuir(num, aum)}')
