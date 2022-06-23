matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = maior = col = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha] [coluna] = int(input('Digite um valor: '))
        if matriz[linha] [coluna] % 2 == 0:
            par += matriz[linha][coluna]
for l in range (0, 3):
    col += matriz[l][2]
for d in range (0,3):
    if d == 0:
        maior = matriz[linha][coluna]
    elif matriz[1][d] > maior:
        maior = matriz[1][d]
#soma = matriz[0, 2] + matriz[1, 2] + matriz[2, 2]
print(f'A soma de todos os números pares é {par}')
print(f'A soma dos itens da coluna 3 é {col}')
print(f'O maior valor da segunda linha é: {maior}')