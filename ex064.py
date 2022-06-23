num = int(input('Digite um numero inteiro [999] para parar: '))
soma = 0
ndigitados = 0
while num != 999:
    soma += num
    ndigitados += 1
    num = int(input('Digite outro inteiro [999] para parar: '))
print('Voce digitou {} numeros e a soma de todos os numeros foi {}'.format(ndigitados, soma))
