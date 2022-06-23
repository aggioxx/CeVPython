while True:
    num = int(input('Digite um valor inteiro (digite um valor negativo para sair): '))
    if num >= 0:
        print('ablue baleur')
        cont = 0
        while cont < 10:
            cont += 1
            print(f'{num} x {cont} = {num * cont}')
    else:
        break
