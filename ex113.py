def leiaInt(msg):
    ok = False
    while not ok:
        try:
            n = int(input(msg))
        except Exception as erro:
            print('ERRO, FAVOR DIGITE UM NÚMERO INTEIRO')
            print(erro.__class__)
        else:
            ok = True

def leiaFloat(msg):
    ok = False
    while not ok:
        try:
            n = float(input(msg))
        except Exception as erro:
            print('ERRO, FAVOR DIGITE UM NÚMERO REAL')
            print(erro.__class__)
        else:
            ok = True


nInt = leiaInt('Digite um número inteiro: ')
nFloat = leiaFloat('Digite um número real: ')