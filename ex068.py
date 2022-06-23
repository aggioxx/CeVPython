from random import randint
while True:
    esc = str(input('Selecione [P] par ou [I] impar: ')).lower().strip()[0]
    num = int(input('Digite o numero da sua jogada: '))
    pc = randint(0, 10)
    res = num + pc
    if res % 2 == 0 and esc == 'p':
        print(f' Voce selecionou Par e venceu o computador, a soma deu {res}. Parabens')
        break
    elif res % 2 != 0 and esc == 'i':
        print(f'Voce selecionou Impar e venceu o computador, a soma deu {res}. Parabens')
        break
    else:
        print(f'Tomou pau, a soma foi {res}')