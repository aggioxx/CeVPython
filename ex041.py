import datetime
nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = datetime.date.today().year
idade = atual - nasc
if idade <=9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade > 19 and idade <= 25:
    print('Senior')
else: 
    print('Master')

