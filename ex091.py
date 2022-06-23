from random import randint
from time import sleep
from operator import itemgetter
c = 1
dados = { 'jogador 1': randint(1,6), 'jogador 2': randint(1,6), 'jogador 3': randint(1,6), 'jogador 4': randint(1,6)}
rank = list()
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
    c += 1
rank = sorted(dados.items(), key= itemgetter(1), reverse = True)
for i,v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')