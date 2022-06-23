final = list() #lista que será printada
pesado = leve = 0
cont = 0
while True:
    dados = list() #apenas para digitar
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    final.append(dados[:])
    if len(final) == 1 or dados[1] > pesado:
        pesado = dados[1] 
    if len(final) == 1 or dados[1] < leve:
        leve = dados[1] 
    dados.clear()
    cont += 1
    esc = str(input('Deseja continuar? S/N ')).lower().strip()[0]
    if esc == 'n':
        break
print(f'O total de registros foi de {cont}')
print(f'O menor peso registrado foi {leve}')
print(f'O maior peso registrado foi {pesado}')
