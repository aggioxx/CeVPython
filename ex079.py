list = []
cont = 1
while True:
    num = int(input(f'Digite o {cont}º valor: '))   
    if num in list:
        print('Esse valor já está na lista campeão')
    else: 
        list.append(num)
        cont += 1
    esc = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if esc != 's':
        break
list.sort()
print(f'A lista foi finalizada com {cont} valores, os números digitados em ordem crescente foram: \n{list}')