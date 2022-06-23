def ficha(nj = '<desconhecido>', gols = 0):
     print(f'O {nj} fez {gols} gols no campeonato')


nome = str(input('Digite o nome do jogador: ')).strip().capitalize()
ngols = str(input('Quantos gols ele fez no campeonato: ')).strip()
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if nome == '':
    ficha(gols = ngols)
else:
    ficha(nome, ngols)
