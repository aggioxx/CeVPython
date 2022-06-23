print('='*20)
print('Lula store')
print('='*20)
total = caro = barato = cont = 0
nbarato = 'a'
while True:
    prod = str(input('Digite o nome de seu produto: '))
    preco = float(input('Digite o preco do produto: '))
    cont +=1
    total += preco

    if cont == 1:
        barato = preco
        nbarato = prod
    else:
        if preco < barato:
            barato = preco
            nbarato = prod
    if preco >= 1000:
        caro += 1
    esc = 'a'
    while esc not in 'sn':
         esc = str(input('Quer continuar? [S/N]')).lower().strip()
    if esc == 'n':
        break
print(f'O total da compra foi R${total}\n{caro} produtos custam mais que R$1000\nO produto mais barato é {nbarato}')