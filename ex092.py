import datetime
date = datetime.date.today().year
persona = dict()
persona['pessoa'] = str(input('Nome: '))
persona['idade'] = date - int(input('Ano de nascimento: '))
persona['CTPS'] = int(input('Carteira de trabalho (0 não possui): '))
if persona['CTPS'] != 0:
    persona['sal'] = float(input('Digite o seu salário: '))
    persona['anoc'] = int(input('Digite o ano em que foi contratado: '))
    persona['aposentadoria'] = 65 - persona['idade']
for k, v in persona.items():
    print(f'{k} tem o valor de {v}')



