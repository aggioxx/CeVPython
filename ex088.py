from random import randint
from time import sleep
jogos = list()
mega = list()
esc = int(input('Deseja que o computador faça quantos jogos para você? '))
print('-'*5, f'Sorteando {esc} jogos','-'*5)
while esc != 0:
        for c in range(0, 6):
                ale = randint(1, 60)
                mega.append(ale)
        jogos.append(mega[:]) 
        mega.clear()
        esc -= 1
for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        sleep(1)
