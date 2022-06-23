nome = str(input('Digite seu nome completo: ')).strip()
res = nome.upper().find('SILVA')
if res == -1:
    print('Seu nome nao tem Silva')
else:
    print('Seu nome tem Silva')