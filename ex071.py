print('-='*20)
print('Esse sistema já é melhor que o do BB')
print('-='*20)
ced50=ced20=ced10=ced1 = 0
saque = int(input('Digite o valor de seu saque: '))
while True:
    while saque - 50 >= 0:
        ced50 += 1
        saque -= 50
    while saque - 20 >= 0:
        ced20 += 1
        saque -= 20
    while saque - 10 >= 0:
        ced10 += 1
        saque -= 10
    while saque - 1 >= 0:
        ced1 += 1
        saque -= 1
        break  
    print(f'Seu saque tem {ced50} notas de R$50, {ced20} notas de R$20, {ced10} notas de R$10 e {ced1} notas de R$1')
    esc ='a'
    while esc not in 'sn':
        esc = str(input('Deseja fazer mais um saque? [S/N]')).lower().strip()[0]
    if esc == 'n':
        break