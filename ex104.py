def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg)) 
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO, DIGITE UM NÚMERO')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')