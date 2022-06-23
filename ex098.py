def cont(n1, n2, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'contagem de {n1} até {n2} de {p} em {p}')
    if n1 < n2:
        for c in range(n1, n2, p):
            print(f'{c} ', end='')
        print()
    else:
        for c in range(n1, n2, -p):
            print(f'{c} ', end='')
        print()


cont(1, 10, 1,)
cont(10, 0, 2,)
cont(int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Passo: ')))
