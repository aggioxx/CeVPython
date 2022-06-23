primeiro = int (input('Digite o primeiro termo da PA: '))
razao = int (input('Digite a razao da PA: '))
termo = primeiro
a = 1
esc = 10
total = 0 
while esc !=0:
    total += esc    
    while a <= total:
        print('{} '.format(termo), end='')
        termo += razao
        a += 1
    esc = int(input('\nQuer calcular mais quantos termos? '))
print('Chegamos ao fim, foram exibidos {} termos'.format(total))

