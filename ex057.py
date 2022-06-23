sexo = str(input('Digite o sexo escolhido M/F: ')).lower().strip()[0]
while sexo != 'm' and sexo != 'f':
    sexo = str(input(' Essa não é uma das opções, selecione M ou N: ')).lower().strip()[0]
print('Sexo {} registrado'.format(sexo))
