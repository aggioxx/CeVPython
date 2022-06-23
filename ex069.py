homi = maior = muiemenor = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = 'a'
    while sexo not in 'mf':
        sexo = str(input('digite o sexo [M/F] ')).strip().lower()[0]
    if sexo == 'm':
        homi += 1
    if sexo == 'f' and idade < 20:
        muiemenor += 1
    if idade >= 18:
        maior += 1 
    esc = ''
    while esc not in 'sn':
        esc = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if esc == 'n':
        break
print(f'No grupo digitado temos:\n{maior} maiores de 18\n{homi} homens\n{muiemenor} mulheres com menos de 18 anos')
