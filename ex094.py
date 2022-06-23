import math
pessoa = dict()
galera = list() 
totpessoa = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('Erro, escolha apenas [M/F]')
    galera.append(pessoa.copy())
    while True:
        esc = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
        if esc in 'sn':
            break
        print('Erro, escolha apenas [S/N]')
    if esc == 'n':
        break 
print('_' * 50)
print(f'Foram cadastradas {len(galera)} pessoas')
for c in range (0, len(galera)):
    totpessoa += galera[c]['idade']
med = totpessoa / len(galera)
print(f'A média de idade é {med}')
print('As mulheres registradas foram: ')
for p in galera:
    if p['sexo'] == 'f':
        print(p['nome'],' | ', end=' ')
print('\nAcima da média, temos:')
for c in galera:
    if c['idade'] > med:
        print(' ')
        for k, v in c.items():
            print(f'{k} = {v} ', end=' ')
        print()
print('<<ENCERRANDO...')