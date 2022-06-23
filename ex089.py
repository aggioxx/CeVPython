alunos = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    esc = str(input('Deseja continuar? [S/N]')).strip()
    if esc in 'Nn':
        break
for i, l in enumerate(alunos):
    media = (l[1] + l[2]) / 2
    print(f'{i+1:<4}',f'{l[0]:<10}',f'{media}')
while True:
    opc = int(input('Deseja saber as notas de qual aluno? (999 interrompe): ')) -1
    if opc == 998:
        print('ENCERRANDO...')
        break
    if opc <=len(alunos) - 1:
        print(f'As notas de {alunos[opc][0]} são {alunos[opc][1]} e {alunos[opc][2]}')