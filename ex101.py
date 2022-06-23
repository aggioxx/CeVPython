def voto(ano):
    from datetime import date
    hoje = date.today().year
    a = hoje - nasc
    if a < 16:
        return f'Vc tem {a} anos, seu título foi negado fio, vai trocar a fralda. NEGADO'
    elif a >= 16 and a < 18:
        return f'Vc tem {a} anos, você pode votar, mas não é necessário. OPCIONAL'
    else:
        return f'Já era, vc tem {a} anos, vá votar seu falido'


nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(nasc))