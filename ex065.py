esc = 's'
cont = 0
soma = 0
maior = 0
menor = 0
while esc == 's':
    num = int(input('Digite um numero inteiro: '))
    esc = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    cont += 1
    soma += num
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num     
print(f'A soma entre todos os valores digitados resulta em: {soma}, o maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
