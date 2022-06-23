#termo = int(input('Digitre o primeiro termo da PA: '))
#razao = int(input('Digite a razao da PA: '))
#ultimo = termo + (10 - 1) * razao
#for c in range (termo , ultimo + razao, razao):
#    print('{}  '.format(c), end='')
#print('\nAcabou')

termo = int (input('Digite o primeiro termo da PA: '))
razao = int (input('Digite a razao da PA: '))
a = 0
while a <10:
    termo = termo + razao
    print('{} '.format(termo - razao), end='')
    a += 1
