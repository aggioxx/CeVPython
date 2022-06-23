import math


def fatorial(n, show):
    """"
    Recebe seu número e faz o fatorial
    :param n: Número a ser calculado
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O resultado de fatorial de N
    """
    global num
    cont = num - 1
    res = math.factorial(num)
    print(f'{num}', end=' ')
    while cont > 0:
        if esc == 1:
            show = True
            print(f'x {cont}', end=' ')
        cont -= 1
    print('=', end =' ')
    return res


num = int(input('Digite o número que será fatorado: '))
esc = str(input('Deseja mostrar o cálculo? [S/N]: ')).strip().lower()[0]
if esc == 'n':
    esc = 0
else:
    esc = 1

print(fatorial(num, esc))

