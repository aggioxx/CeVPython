soma = ndigitados =0
while True:
    num = int(input('Digite um inteiro [999] para parar: '))
    if num == 999:
        break
    soma += num
    ndigitados += 1
print(f'Voce digitou {ndigitados} numeros e a soma de todos os numeros foi {soma}')
