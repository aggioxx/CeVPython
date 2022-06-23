import datetime
nasc = int(input('Digite o ano em que voce nasceu: '))
date = datetime.date.today().year
dezoito = nasc + 18
print(dezoito)
if dezoito < date:
    print('Lamento te dizer, mas vc ja deveria ter se alistado ha {} anos'.format(date - dezoito))
elif dezoito == date:
    print('Xiiiii fiote, corre la alistar')
else:
    print('Calma jovem, ainda falta {} anos para voce se alistar'.format(dezoito - date))
