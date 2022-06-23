from datetime import date
ano = int(input('Digite um ano (0 sera o ano atual): '))
calc1 = ano % 4 
calc2 = ano % 100
if ano == 0:
    ano = date.today().year
if calc1 == 0 and calc2 !=0 or ano % 400 == 0:
    print('O ano {} e bissexto'.format(ano))
else: 
    print('O ano {} nao e bissexto'.format(ano))