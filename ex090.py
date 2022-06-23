ficha = dict()
ficha['nome'] = str(input('Nome: ')).strip()
ficha['media'] = float(input('Média: '))
if ficha['media'] <5:
    ficha['situação'] = 'Reprovado'
else:
    ficha['sit'] = 'Aprovado'
for k, v in ficha.items():
    print(f'{k} é igual a {v}')