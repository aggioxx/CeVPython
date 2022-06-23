from operator import truediv


cidade = str (input('Digite o nome de uma cidade: ')).strip()
saint = cidade.find('Santo')
if saint == 0:
    print('Sua cidade comeca com nome santo')
else:
    print('Sua cidade nao comeca com nome santo')

