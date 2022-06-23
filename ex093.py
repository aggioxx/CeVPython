jogador = dict()
golspar= list()
jogador['nome'] = str(input('Nome: '))
a = jogador['partidas'] = int(input('Número de partidas: '))
for c in range (0, a):
    golspar.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}? ')))
jogador['gols'] = golspar[:]
jogador['total'] = sum(golspar)
print('-=-'*50)
for i, v in enumerate(golspar):
    print(f'Na partida {i+1} ele marcou {v} gols')
print(f'\nNo total, {jogador["nome"]} marcou {jogador["total"]} gols')