word = str(input('Digite uma palavra: ')).strip().upper()
lupa = word.count('A')
print('A letra A aparece {} vezes'.format(lupa))
print('A primeira letra A apareceu na posicao {}'.format(word.find('A')+1))
print('A ultima letra A apareceu na posicao {} '.format(word.rfind('A')+1))
